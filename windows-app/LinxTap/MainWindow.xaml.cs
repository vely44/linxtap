using System;
using System.Net.Sockets;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using Microsoft.Win32;
using System.IO;
using System.Threading.Tasks;

namespace LinxTap
{
    public partial class MainWindow : Window
    {
        private TcpClient? _client;
        private NetworkStream? _stream;
        private bool _isConnected = false;
        private string _currentIp = "";
        private int _currentPort = 0;

        public MainWindow()
        {
            InitializeComponent();
            LoadLocalDeviceInfo();
        }

        private void LoadLocalDeviceInfo()
        {
            HostnameLabel.Text = NetworkUtils.GetHostname();
            LocalIpLabel.Text = NetworkUtils.GetLocalIp();
        }

        private async void ConnectButton_Click(object sender, RoutedEventArgs e)
        {
            if (_isConnected)
            {
                // Disconnect
                Disconnect();
            }
            else
            {
                // Connect
                await ConnectAsync();
            }
        }

        private async Task ConnectAsync()
        {
            string ip = IpInput.Text.Trim();
            string portText = PortInput.Text.Trim();

            // Validate inputs
            if (string.IsNullOrEmpty(ip) || string.IsNullOrEmpty(portText))
            {
                UpdateStatus("✗ IP address and port are required", StatusType.Error);
                return;
            }

            if (!int.TryParse(portText, out int port) || port < 1 || port > 65535)
            {
                UpdateStatus("✗ Port must be between 1 and 65535", StatusType.Error);
                return;
            }

            try
            {
                ConnectButton.IsEnabled = false;
                UpdateStatus($"Connecting to {ip}:{port}...", StatusType.Normal);

                _client = new TcpClient();
                await _client.ConnectAsync(ip, port);
                _stream = _client.GetStream();
                _isConnected = true;
                _currentIp = ip;
                _currentPort = port;

                // Detect OS and gateway
                string remoteOs = "Unknown";
                bool isGateway = NetworkUtils.IsGateway(ip);

                int? ttl = await Task.Run(() => NetworkUtils.GetRemoteTtl(ip));
                if (ttl.HasValue)
                {
                    remoteOs = NetworkUtils.DetectOsFromTtl(ttl.Value);
                }

                // Update UI
                UpdateStatus($"● Connected to {ip}:{port}", StatusType.Connected);
                ConnectButton.Content = "⚠ DISCONNECT";
                ConnectButton.Background = new SolidColorBrush(Color.FromRgb(139, 0, 0)); // Dark red

                // Show remote device info
                RemoteOsLabel.Text = remoteOs;
                if (isGateway)
                {
                    GatewayLabel.Text = "Gateway (Router)";
                    GatewayLabel.Foreground = new SolidColorBrush(Color.FromRgb(255, 152, 0)); // Orange
                }
                else
                {
                    GatewayLabel.Text = "Network Device";
                    GatewayLabel.Foreground = new SolidColorBrush(Color.FromRgb(212, 212, 212));
                }

                RemoteInfoPanel.Visibility = Visibility.Visible;
                MessagePanel.Visibility = Visibility.Visible;

                LogMessage($"Connected to {ip}:{port}", MessageType.System);
            }
            catch (SocketException ex)
            {
                UpdateStatus($"✗ Connection refused: {ex.Message}", StatusType.Error);
            }
            catch (Exception ex)
            {
                UpdateStatus($"✗ Error: {ex.Message}", StatusType.Error);
            }
            finally
            {
                ConnectButton.IsEnabled = true;
            }
        }

        private void Disconnect()
        {
            try
            {
                _stream?.Close();
                _client?.Close();
            }
            catch { }

            _isConnected = false;
            _client = null;
            _stream = null;

            UpdateStatus("○ Not connected", StatusType.Normal);
            ConnectButton.Content = "⚡ CONNECT";
            ConnectButton.Background = new SolidColorBrush(Color.FromRgb(14, 99, 156)); // Blue

            RemoteInfoPanel.Visibility = Visibility.Collapsed;
            MessagePanel.Visibility = Visibility.Collapsed;

            LogMessage("Disconnected", MessageType.System);
        }

        private async void SendButton_Click(object sender, RoutedEventArgs e)
        {
            await SendMessageAsync();
        }

        private async void MessageInput_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Enter)
            {
                await SendMessageAsync();
            }
        }

        private async Task SendMessageAsync()
        {
            if (!_isConnected || _stream == null)
            {
                LogMessage("✗ Not connected to any device", MessageType.Error);
                return;
            }

            string message = MessageInput.Text.Trim();
            if (string.IsNullOrEmpty(message))
            {
                return;
            }

            try
            {
                // Send message
                byte[] data = Encoding.UTF8.GetBytes(message);
                await _stream.WriteAsync(data, 0, data.Length);

                LogMessage($"SENT: {message}", MessageType.Sent);
                LogMessage($"✓ Sent {data.Length} bytes", MessageType.Confirm);

                // Try to read response (with timeout)
                _stream.ReadTimeout = 1000;
                byte[] buffer = new byte[4096];

                try
                {
                    int bytesRead = await _stream.ReadAsync(buffer, 0, buffer.Length);
                    if (bytesRead > 0)
                    {
                        string response = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                        LogMessage($"RESPONSE: {response}", MessageType.Response);
                    }
                }
                catch (IOException)
                {
                    // No response or timeout - this is normal
                }

                MessageInput.Clear();
            }
            catch (Exception ex)
            {
                LogMessage($"✗ Send failed: {ex.Message}", MessageType.Error);

                // Connection might be broken
                if (!_client!.Connected)
                {
                    Disconnect();
                    UpdateStatus("✗ Connection lost", StatusType.Error);
                }
            }
        }

        private void ExportButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                var dialog = new SaveFileDialog
                {
                    FileName = $"linxtap_log_{DateTime.Now:yyyyMMdd_HHmmss}.txt",
                    Filter = "Text Files (*.txt)|*.txt|All Files (*.*)|*.*"
                };

                if (dialog.ShowDialog() == true)
                {
                    // Extract text from RichTextBox
                    TextRange textRange = new TextRange(
                        MessageLog.Document.ContentStart,
                        MessageLog.Document.ContentEnd);

                    File.WriteAllText(dialog.FileName, textRange.Text);
                    LogMessage($"Log exported to {dialog.FileName}", MessageType.System);
                }
            }
            catch (Exception ex)
            {
                LogMessage($"Export failed: {ex.Message}", MessageType.Error);
            }
        }

        private void UpdateStatus(string text, StatusType type)
        {
            StatusLabel.Text = text;

            switch (type)
            {
                case StatusType.Connected:
                    StatusBorder.Background = new SolidColorBrush(Color.FromRgb(45, 80, 22)); // Dark green
                    StatusLabel.Foreground = new SolidColorBrush(Color.FromRgb(143, 212, 96)); // Light green
                    break;
                case StatusType.Error:
                    StatusBorder.Background = new SolidColorBrush(Color.FromRgb(90, 29, 29)); // Dark red
                    StatusLabel.Foreground = new SolidColorBrush(Color.FromRgb(244, 135, 113)); // Light red
                    break;
                default:
                    StatusBorder.Background = new SolidColorBrush(Color.FromRgb(60, 60, 60)); // Gray
                    StatusLabel.Foreground = new SolidColorBrush(Color.FromRgb(133, 133, 133)); // Light gray
                    break;
            }
        }

        private void LogMessage(string message, MessageType type)
        {
            string timestamp = DateTime.Now.ToString("HH:mm:ss");
            Paragraph para = new Paragraph();

            Run run = new Run($"[{timestamp}] {message}");

            switch (type)
            {
                case MessageType.Sent:
                    run.Foreground = new SolidColorBrush(Color.FromRgb(86, 156, 214)); // Blue
                    break;
                case MessageType.Response:
                    run.Foreground = new SolidColorBrush(Color.FromRgb(78, 201, 176)); // Cyan
                    break;
                case MessageType.Confirm:
                    run.Foreground = new SolidColorBrush(Color.FromRgb(106, 153, 85)); // Green
                    break;
                case MessageType.Error:
                    run.Foreground = new SolidColorBrush(Color.FromRgb(244, 135, 113)); // Red
                    break;
                case MessageType.System:
                    run.Foreground = new SolidColorBrush(Color.FromRgb(156, 220, 254)); // Light blue
                    run.FontWeight = FontWeights.Bold;
                    break;
                default:
                    run.Foreground = new SolidColorBrush(Color.FromRgb(212, 212, 212)); // White
                    break;
            }

            para.Inlines.Add(run);
            MessageLog.Document.Blocks.Add(para);

            // Auto-scroll to bottom
            MessageLog.ScrollToEnd();
        }

        protected override void OnClosed(EventArgs e)
        {
            if (_isConnected)
            {
                Disconnect();
            }
            base.OnClosed(e);
        }

        private enum StatusType
        {
            Normal,
            Connected,
            Error
        }

        private enum MessageType
        {
            Sent,
            Response,
            Confirm,
            Error,
            System,
            Info
        }
    }
}
