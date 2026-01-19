# LinxTap

Modern TCP/IP network client for Linux with OS detection and gateway identification.

![LinxTap UI](screenshots/linxtap-ui.png)

## Features

- ⚡ Real-time TCP connection testing
- 📤 Send/receive messages with confirmation
- 🖥️ Automatic OS detection (Linux/Windows/Cisco)
- 🌐 Gateway/router identification
- 📝 Color-coded message log with export
- 💾 Portable - no installation required

## Quick Start

```bash
# Extract and run
tar -xzf LinxTap-linux-x64.tar.gz
cd LinxTap
./LinxTap
```

No Python or dependencies needed. **[Full guide →](USER_MANUAL.md)**

## System Requirements

- **Linux**: Ubuntu 24.04+, Debian 11+, Fedora 36+, Arch
- **Arch**: x86_64 (64-bit)
- **Display**: X11 or Wayland

## Development

```bash
# Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
python main.py

# Test
pytest tests/

# Build executable
./build.sh
```

## Project Structure

```
src/
├── core/          # Connection logic, OS detection
├── ui/            # Modern terminal-style Qt interface
└── utils/         # Network utilities (TTL, gateway)
tests/             # Full test coverage
```

---

**Version 1.0** | Linux only | Python 3.10+ | PySide6
