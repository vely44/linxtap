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
- **Resize**: Drag the window edges or corners to resize (minimum size: 450x450 pixels)

### Keyboard Shortcuts

- `Alt+F4` - Close the application
- `Tab` - Navigate between interface elements (IP field → Port field → Connect button)
- `Enter` - Activate the Connect/Disconnect button when focused
- `Space` - Activate the Connect/Disconnect button when focused

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
