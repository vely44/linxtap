# LinxTap User Manual

Welcome to LinxTap! This manual will guide you through using the application.

## Table of Contents

1. [Getting Started](#getting-started)
2. [System Requirements](#system-requirements)
3. [Installation](#installation)
4. [Using LinxTap](#using-linxtap)
5. [Troubleshooting](#troubleshooting)
6. [FAQ](#faq)

## Getting Started

LinxTap is a Linux desktop application built with Qt (PySide6). It provides a simple, user-friendly interface for connecting to network servers via TCP/IP. You can use it to test network connectivity, verify server availability, or establish connections to remote services.

### What You'll Need

- A Linux computer with a desktop environment
- Graphics support (X11 or Wayland)
- No Python installation required (when using the pre-built executable)

## System Requirements

### Minimum Requirements

- **Operating System**: Linux (64-bit)
  - Ubuntu 24.04 or newer
  - Debian 11+ (Bullseye and newer)
  - Fedora 36+
  - Arch Linux or derivatives
  - Other modern Linux distributions with glibc 2.31+

- **Architecture**: x86_64 (64-bit Intel/AMD processors)

- **Display Server**: X11 or Wayland

- **System Libraries**:
  - libEGL (OpenGL rendering)
  - libGL (OpenGL)
  - libxkbcommon (keyboard handling)
  - libdbus (system communication)

### Installing Missing Libraries

Most Linux distributions include these libraries by default. If you encounter errors, install them:

**Ubuntu/Debian:**
```bash
sudo apt-get install libegl1 libgl1 libxkbcommon0 libdbus-1-3
```

**Fedora/RHEL:**
```bash
sudo dnf install mesa-libEGL mesa-libGL libxkbcommon dbus-libs
```

**Arch Linux:**
```bash
sudo pacman -S libgl libxkbcommon dbus
```

## Installation

### Option 1: Pre-compiled Executable (Recommended)

1. **Download** the latest release from the releases page
2. **Extract** the archive to a location of your choice:
   ```bash
   tar -xzf LinxTap-linux-x64.tar.gz
   cd LinxTap
   ```
3. **Run** the application:
   ```bash
   ./LinxTap
   ```

That's it! No installation or configuration needed.

### Option 2: Running from Source

If you prefer to run from source code:

1. **Clone the repository** or download the source code
2. **Install dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python main.py
   ```

## Using LinxTap

### Launching the Application

**From File Manager:**
- Navigate to the LinxTap folder
- Double-click the `LinxTap` executable

**From Terminal:**
```bash
cd /path/to/LinxTap
./LinxTap
```

### Main Window

When you launch LinxTap, you'll see the main application window:

![LinxTap UI Screenshot](screenshots/linxtap-ui.png)

The window contains:

- **Title**: Shows "LinxTap" at the top
- **Connection Settings**: Input fields for IP address and port
- **Status Display**: Shows connection status (Not connected, Connected, or Error messages)
- **Connect Button**: Click to connect or disconnect from the server
- **Remote Device Information**: (Appears when connected) Shows detected OS and device type
- **Send Message**: (Appears when connected) Message input and log for TCP communication
- **Local Device Information**: Shows your device's hostname and local network IP address

### Basic Operations

#### Connecting to a Server

1. **Enter IP Address**: Type the IP address of the server you want to connect to
   - Default: `127.0.0.1` (localhost)
   - Example: `192.168.1.100`

2. **Enter Port**: Type the port number
   - Default: `8080`
   - Valid range: 1-65535

3. **Click Connect**: Press the "Connect" button to establish the connection

**Status Messages:**

- **Not connected** (Gray): Initial state, no connection established
- **Connected to [IP:Port]** (Green): Successfully connected to the server
- **Error messages** (Red): Connection failed with specific error details

#### Disconnecting from a Server

When connected, the "Connect" button changes to "Disconnect":

1. Click the **Disconnect** button
2. The connection will be closed
3. Status will show "Disconnected from [IP:Port]"

#### Sending Messages to Connected Devices

When you successfully connect to a server, a "Send Message" section appears, allowing you to send TCP messages:

**Message Log:**
- Shows a timestamped log of all sent messages and responses
- Color-coded for easy reading:
  - **Blue**: Sent messages
  - **Green**: Responses from remote device
  - **Gray**: Confirmations (bytes sent)
  - **Red**: Errors
  - **Bold Gray**: System messages (connect/disconnect)

**Sending a Message:**
1. Type your message in the text input field
2. Click "Send" button or press Enter
3. The message is sent via TCP to the connected device
4. You'll see confirmation showing how many bytes were sent
5. If the remote device responds, the response appears in the log

**Message Confirmations:**
- After sending, you'll see: "✓ Sent X bytes"
- This confirms the message left your device successfully
- If the remote device sends a response, it will appear as "RESPONSE: [text]"
- Note: Not all servers send responses; confirmation of sending does not mean the server processed your message

**Example Log:**
```
[14:30:15] Connected to 192.168.1.100:8080
[14:30:20] SENT: Hello, server!
[14:30:20] ✓ Sent 14 bytes (no response)
[14:30:25] SENT: GET /status
[14:30:25] ✓ Sent 11 bytes
[14:30:25] RESPONSE: Status: OK
```

**Important Notes:**
- Messages are sent as UTF-8 encoded text
- Maximum response size is 4096 bytes
- Response timeout is 1 second
- If connection breaks while sending, you'll see an error message

#### Viewing Remote Device Information

When you successfully connect to a server, a "Remote Device Information" section appears showing:

- **Detected OS**: The operating system of the remote device
  - Linux/Unix
  - Windows
  - Cisco/Network Device
  - Unknown (if detection fails)

- **Device Type**: Whether the device is your gateway or a regular network device
  - **Gateway (Router)** (displayed in orange): The device is your default gateway/router
  - **Network Device**: Any other device on the network

**How does OS detection work?**

LinxTap uses TTL (Time To Live) analysis to detect the remote operating system:
- Linux/Unix systems typically use TTL 64
- Windows systems typically use TTL 128
- Network devices typically use TTL 255

**Note**: OS detection is a best-guess based on TTL values and may not always be 100% accurate, especially if the device is behind NAT or uses custom TTL values.

**Why is gateway detection useful?**
- Quickly identify if you're connecting to your router
- Useful for network diagnostics and troubleshooting
- Helps understand your network topology

#### Viewing Local Device Information

At the bottom of the window, you can see information about your local device:

- **Hostname**: The name of your computer on the network
- **Local IP**: Your device's IP address on the local network (displayed in blue)

**Why is this useful?**
- Know your own IP address when setting up server connections
- Share your IP with others who need to connect to your device
- Verify you're on the correct network
- Troubleshoot network connectivity issues

**Note**: If your device has multiple network interfaces (WiFi, Ethernet, VPN), the displayed IP will be the one used for outgoing internet connections.

#### Common Error Messages

- **"Error: IP address and port are required"** - You must fill in both fields
- **"Error: Port must be a valid number"** - Port contains non-numeric characters
- **"Error: Port must be between 1 and 65535"** - Port number is out of valid range
- **"Error: Connection refused"** - Server is not accepting connections on that port
- **"Error: Connection timeout"** - Server didn't respond within 5 seconds
- **"Error: Invalid IP address"** - The IP address format is incorrect

#### Window Controls

- **Minimize**: Click the minimize button in the window title bar
- **Maximize**: Click the maximize button to expand to full screen
- **Close**: Click the X button or press `Alt+F4` to close the application
- **Resize**: Drag the window edges or corners to resize (minimum size: 500x650 pixels)

### Keyboard Shortcuts

- `Alt+F4` - Close the application
- `Tab` - Navigate between interface elements
- `Enter` - Send message (when in message input field) or activate focused button
- `Space` - Activate focused button

## Troubleshooting

### Application Won't Start

**Problem**: Double-clicking does nothing or shows an error

**Solutions:**
1. Open a terminal and try running: `./LinxTap`
2. Check for error messages in the terminal
3. Ensure the file has executable permissions:
   ```bash
   chmod +x LinxTap
   ```

### Missing Library Errors

**Problem**: Error message about missing `.so` files

**Solution**: Install the required system libraries (see [System Requirements](#system-requirements))

### Graphics/Display Issues

**Problem**: Application crashes or shows graphical glitches

**Solutions:**
1. Update your graphics drivers
2. Try running with software rendering:
   ```bash
   QT_QPA_PLATFORM=offscreen ./LinxTap
   ```
3. Check that your desktop environment is running properly

### Application Runs Slowly

**Possible Causes:**
- First launch may take 2-3 seconds while Qt initializes
- Subsequent launches will be faster
- Check system resources (CPU, RAM) aren't maxed out

### Permission Denied Errors

**Problem**: "Permission denied" when trying to run

**Solution**: Make the file executable:
```bash
chmod +x LinxTap
```

## FAQ

### Do I need Python installed?

**No.** The pre-compiled executable bundles everything needed. Python is only required if you're running from source code.

### How much disk space does it need?

Approximately 170 MB for the complete installation (executable + bundled libraries).

### Can I run this on a different Linux distribution?

Yes! LinxTap works on most modern Linux distributions. See [System Requirements](#system-requirements) for the full list.

### Can I run this on a headless server?

The application requires a display server (X11 or Wayland). For testing purposes, you can use an offscreen platform, but normal operation requires a GUI environment.

### Does it work on ARM processors (like Raspberry Pi)?

The pre-built executable is for x86_64 architecture. For ARM systems, you'll need to build from source on the ARM device.

### How do I uninstall LinxTap?

Simply delete the LinxTap folder. There are no system files, registry entries, or hidden configurations to clean up.

### Where are my settings stored?

Currently, connection settings (IP and port) are not persisted between sessions. All state is temporary and resets when you close the application.

### What happens to my connection when I close the app?

Any active connections are automatically closed when you exit LinxTap. The application cleans up all network resources properly.

### Can I connect to multiple servers at once?

Currently, LinxTap supports one connection at a time. If you try to connect while already connected, it will disconnect from the current server first.

### What is the connection timeout?

LinxTap waits 5 seconds for a server to respond before timing out. This prevents the application from hanging indefinitely.

### Why does it show my local IP address?

LinxTap displays your local network IP address so you can:
- Easily share your IP with others who need to connect to your device
- Verify you're connected to the correct network
- Know which IP to use when setting up local servers

The IP address shown is automatically detected from your active network interface.

### What if my Local IP shows "Unknown"?

If the local IP shows "Unknown", it means:
- Your device might not be connected to any network
- You might be using a complex network setup
- Network permissions might be restricted

Try connecting to a network (WiFi or Ethernet) and restarting the application.

### How accurate is the OS detection?

OS detection is based on TTL (Time To Live) values and provides a best-guess estimate. It's generally accurate for:
- Direct connections on the same network
- Standard operating systems with default TTL values

It may be less accurate when:
- The device is behind NAT or multiple routers (TTL decreases)
- The remote system uses custom TTL values
- VPNs or proxies are involved

Think of it as a helpful hint rather than a definitive identification.

### What if the OS shows "Unknown"?

If the OS detection shows "Unknown", it could mean:
- The TTL value couldn't be determined
- The remote device uses an uncommon TTL value
- Network conditions prevented TTL detection
- The device uses custom network configurations

This doesn't affect the connection functionality - it's just informational.

### How does LinxTap know if a device is the gateway?

LinxTap reads your system's routing table to find the default gateway IP address, then compares it to the IP you're connecting to. If they match, the device is identified as your gateway (router).

### Can I send binary data or special characters?

Currently, LinxTap sends messages as UTF-8 encoded text. You can send most text and special characters, but binary data is not directly supported. The focus is on text-based protocol testing (HTTP, telnet, etc.).

### What does "Sent X bytes (no response)" mean?

This means your message was successfully sent to the remote device, but the device didn't send any data back within 1 second. This is normal for many servers that don't echo back responses, or for one-way protocols.

### Why don't I see a response from the server?

Several reasons:
- The server might not send responses for the type of message you sent
- The server needs a specific protocol format (e.g., HTTP headers)
- The response timeout (1 second) was too short
- The server closed the connection
- The server is designed to only listen, not respond

### What happens if the connection breaks while sending?

If the connection is lost while sending or waiting for a response, you'll see an error message in the log. The UI will update to show "Connection lost" and the message/remote device sections will be hidden.

### Is my data safe?

LinxTap only establishes TCP connections to the servers you specify. It doesn't send any data automatically. The application is designed for testing connectivity and establishing connections.

### How do I report bugs or request features?

Please visit the project's GitHub repository and open an issue with:
- Your Linux distribution and version
- Steps to reproduce the problem
- Any error messages you see

### Can I contribute to LinxTap?

Yes! LinxTap is open source. Check the repository for contribution guidelines.

---

**Version**: 1.0
**Last Updated**: January 2026

For technical documentation, see [TESTING.md](TESTING.md).
For development information, see [README.md](README.md).
