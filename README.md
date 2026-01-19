# LinxTap

Modern TCP/IP network client with OS detection and gateway identification. Available for **Linux** and **Windows**.

![LinxTap UI](screenshots/linxtap-ui.png)

## Features

- ⚡ Real-time TCP connection testing
- 📤 Send/receive messages with confirmation
- 🖥️ Automatic OS detection (Linux/Windows/Cisco)
- 🌐 Gateway/router identification
- 📝 Color-coded message log with export
- 💾 Portable - no installation required

## Platform Support

### 🐧 Linux Version
- **Language**: Python + PySide6 (Qt)
- **Size**: ~170MB executable
- **Distros**: Ubuntu 24.04+, Debian 11+, Fedora 36+, Arch
- **[Linux Guide →](USER_MANUAL.md)**

### 🪟 Windows Version
- **Language**: C# + WPF
- **Size**: ~25-30MB executable
- **OS**: Windows 10 (1809+) or Windows 11
- **[Windows Guide →](windows-app/README.md)**

Both versions have **identical UI and functionality** - modern terminal style, same features.

## Quick Start

### Linux
```bash
# Extract and run
tar -xzf LinxTap-linux-x64.tar.gz
cd LinxTap
./LinxTap
```

### Windows
```cmd
# Just double-click
LinxTap.exe
```

No dependencies required for either version!

## Development

### Linux (Python)
```bash
# Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
python main.py

# Test
pytest tests/

# Build
./build.sh
```

### Windows (C#)
```cmd
# Build
cd windows-app
build.bat

# Or with .NET CLI
cd windows-app/LinxTap
dotnet run
```

## Project Structure

```
linxtap/
├── src/              # Linux version (Python + Qt)
│   ├── core/         # Connection logic
│   ├── ui/           # Modern terminal UI
│   └── utils/        # Network utilities
├── tests/            # Python tests
└── windows-app/      # Windows version (C# + WPF)
    └── LinxTap/      # WPF project
        ├── MainWindow.xaml
        ├── MainWindow.xaml.cs
        └── NetworkUtils.cs
```

---

**Version 1.0** | Linux (Python 3.10+ / Qt) | Windows (C# / WPF)
