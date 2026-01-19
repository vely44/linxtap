using System;
using System.Net;
using System.Net.Sockets;
using System.Net.NetworkInformation;
using System.Linq;
using System.Text.RegularExpressions;

namespace LinxTap
{
    public static class NetworkUtils
    {
        /// <summary>
        /// Get the local network IP address of this device
        /// </summary>
        public static string GetLocalIp()
        {
            try
            {
                // Get the host name
                string hostName = Dns.GetHostName();

                // Get IP addresses
                var addresses = Dns.GetHostAddresses(hostName);

                // Find the first IPv4 address that's not loopback
                var localIp = addresses.FirstOrDefault(ip =>
                    ip.AddressFamily == AddressFamily.InterNetwork &&
                    !IPAddress.IsLoopback(ip));

                return localIp?.ToString() ?? "Unknown";
            }
            catch
            {
                return "Unknown";
            }
        }

        /// <summary>
        /// Get the hostname of this device
        /// </summary>
        public static string GetHostname()
        {
            try
            {
                return Dns.GetHostName();
            }
            catch
            {
                return "Unknown";
            }
        }

        /// <summary>
        /// Get the default gateway IP address
        /// </summary>
        public static string? GetDefaultGateway()
        {
            try
            {
                var gateway = NetworkInterface
                    .GetAllNetworkInterfaces()
                    .Where(n => n.OperationalStatus == OperationalStatus.Up)
                    .Where(n => n.NetworkInterfaceType != NetworkInterfaceType.Loopback)
                    .SelectMany(n => n.GetIPProperties()?.GatewayAddresses)
                    .Select(g => g?.Address)
                    .Where(a => a != null && a.AddressFamily == AddressFamily.InterNetwork)
                    .FirstOrDefault();

                return gateway?.ToString();
            }
            catch
            {
                return null;
            }
        }

        /// <summary>
        /// Detect OS based on TTL value
        /// Different operating systems use different default TTL values
        /// </summary>
        public static string DetectOsFromTtl(int ttl)
        {
            if (ttl <= 64)
            {
                if (ttl > 32)
                    return "Linux/Unix";
                else
                    return "Unknown";
            }
            else if (ttl <= 128)
            {
                return "Windows";
            }
            else if (ttl <= 255)
            {
                return "Cisco/Network Device";
            }
            else
            {
                return "Unknown";
            }
        }

        /// <summary>
        /// Get TTL value from a remote host using ping
        /// </summary>
        public static int? GetRemoteTtl(string ip, int timeout = 2000)
        {
            try
            {
                using (var ping = new Ping())
                {
                    var reply = ping.Send(ip, timeout);
                    if (reply.Status == IPStatus.Success)
                    {
                        return reply.Options?.Ttl;
                    }
                }
            }
            catch
            {
                // Ignore errors
            }

            return null;
        }

        /// <summary>
        /// Check if the given IP address is the default gateway
        /// </summary>
        public static bool IsGateway(string ip)
        {
            var gateway = GetDefaultGateway();
            if (gateway == null)
                return false;

            return ip == gateway;
        }
    }
}
