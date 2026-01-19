# LinxTap Quick Start Guide (Windows)

LinxTap is a modern TCP/IP network client for Windows with OS detection and gateway identification.

## Installation

### Pre-built Executable (Recommended)

1. Download `LinxTap.exe`
2. Save to any folder (no installation needed)
3. Double-click to run

### From Source

Requires .NET 8.0 SDK ([Download](https://dotnet.microsoft.com/download))

```cmd
cd windows-app/LinxTap
dotnet run
```

## System Requirements

- **Windows**: 10 (1809+) or Windows 11
- **Architecture**: x64 (64-bit)
- **.NET Runtime**: Not required (self-contained)

## Usage

### Connecting to a Device

1. Enter **IP address** (e.g., `192.168.1.100`)
2. Enter **Port** (e.g., `8080`)
3. Click **⚡ CONNECT**

### Sending Messages

When connected:
- Type message in input field
- Press **Enter** or click **→ Send**
- View responses in message log
- Click **💾 Export** to save log

### Understanding the Information

**Status Indicators:**
- ○ Not connected (Gray)
- ● Connected (Green)
- ✗ Error/Lost (Red)

**Remote Device:**
- **OS Detection**: Based on TTL values (Linux=64, Windows=128, Cisco=255)
- **Device Type**: Shows if device is your gateway/router (orange) or network device

**Local Device:**
- **Host**: Your computer's network name
- **IP**: Your local network IP address

## Keyboard Shortcuts

- **Enter**: Send message (when in message field)
- **Alt+F4**: Close application
- **Tab**: Navigate between fields

## Troubleshooting

**App won't start:**
- Check Windows version (Windows 10 1809+ required)
- Run from Command Prompt to see errors
- Try running as Administrator

**Connection refused:**
- Verify server is running
- Check IP address and port
- Check Windows Firewall settings

**Slow startup:**
- First launch may take 2-3 seconds
- Subsequent launches are faster
- Windows Defender may scan the file initially

## Technical Details

- **Message Format**: UTF-8 encoded text
- **Max Response Size**: 4096 bytes
- **Response Timeout**: 1 second
- **Connection Timeout**: System default

## Windows Firewall

LinxTap may trigger Windows Firewall on first run:
1. Click "Allow access" when prompted
2. Or manually add exception in Windows Security
3. Required for network operations

---

**Version**: 1.0 | For development info, see [README.md](README.md)
