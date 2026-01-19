# LinxTap for Windows

Native C# WPF application with modern terminal-style UI. Same functionality as the Linux version with full Windows integration.

![LinxTap Windows](../screenshots/linxtap-ui.png)

## Features

- ⚡ Real-time TCP connection testing
- 📤 Send/receive messages with confirmation
- 🖥️ Automatic OS detection (Linux/Windows/Cisco)
- 🌐 Gateway/router identification
- 📝 Color-coded message log with export
- 💾 Portable - single EXE, no installation

## System Requirements

- **OS**: Windows 10 (1809+) or Windows 11
- **Arch**: x64 (64-bit)
- **.NET**: Not required (self-contained executable)

## Quick Start

### Pre-built Executable

1. Download `LinxTap.exe`
2. Double-click to run
3. No installation needed!

### Building from Source

**Prerequisites:**
- .NET 8.0 SDK ([Download](https://dotnet.microsoft.com/download))
- Visual Studio 2022 (optional, for development)

**Build:**
```cmd
cd windows-app
build.bat
```

**Run from source:**
```cmd
cd LinxTap
dotnet run
```

## Build Configuration

The application builds as a **self-contained single-file executable**:
- ~25-30MB file size
- No .NET runtime required on target machine
- Includes all dependencies
- Native Windows integration

### Manual Build Commands

```cmd
cd LinxTap
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true
```

Output: `bin\Release\net8.0-windows\win-x64\publish\LinxTap.exe`

## Project Structure

```
windows-app/
├── LinxTap/
│   ├── App.xaml              # Application entry
│   ├── App.xaml.cs
│   ├── MainWindow.xaml       # Main UI (WPF)
│   ├── MainWindow.xaml.cs    # UI logic
│   ├── NetworkUtils.cs       # Network utilities
│   └── LinxTap.csproj        # Project file
├── build.bat                 # Build script
└── README.md                 # This file
```

## Development

### Opening in Visual Studio

1. Open `LinxTap.sln` or `LinxTap.csproj`
2. Press F5 to run
3. Build → Publish to create executable

### VS Code

1. Install C# Dev Kit extension
2. Open `windows-app` folder
3. Press F5 to debug

## Technical Details

- **Framework**: .NET 8.0 Windows
- **UI**: WPF (Windows Presentation Foundation)
- **Styling**: Modern dark terminal theme (VS Code inspired)
- **Networking**: System.Net.Sockets, System.Net.NetworkInformation
- **OS Detection**: TTL-based via System.Net.NetworkInformation.Ping
- **Gateway Detection**: NetworkInterface API

## Differences from Linux Version

- Native Windows APIs for gateway detection
- WPF instead of Qt/PySide6
- Smaller executable size (~25-30MB vs ~170MB)
- Better Windows integration
- Same UI design and color scheme
- Same functionality and features

## Troubleshooting

**App won't start:**
- Check Windows version (Windows 10 1809+ required)
- Check architecture (64-bit required)
- Run from Command Prompt to see errors

**Connection issues:**
- Check Windows Firewall
- Run as Administrator if needed
- Verify server is running and accessible

**Build errors:**
- Ensure .NET 8.0 SDK is installed: `dotnet --version`
- Clean and rebuild: `dotnet clean && dotnet build`

---

**Version 1.0** | Windows 10+ | .NET 8.0 | C# WPF
