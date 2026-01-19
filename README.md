# LinxTap

Desktop utility application for Linux.

## Supported Linux Distributions

The pre-compiled executable works on most modern Linux distributions with a desktop environment:

**Verified:**
- ✅ Ubuntu 24.04 and newer
- ✅ Ubuntu-based distributions (Linux Mint, Pop!_OS, elementary OS)

**Compatible (requires standard system libraries):**
- Debian 11+ (Bullseye and newer)
- Fedora 36+
- openSUSE Leap 15.4+
- Arch Linux (and derivatives like Manjaro)
- Any distribution with glibc 2.31+ and Qt system libraries

**System Requirements:**
- x86_64 architecture (64-bit)
- X11 or Wayland display server
- Standard graphics libraries (libEGL, libGL, libxkbcommon, libdbus)

For installation instructions for missing libraries, see [TESTING.md](TESTING.md).

## Quick Start (Pre-compiled Executable)

**The easiest way to test the application is to use the pre-built executable:**

1. Download the latest release from the releases page
2. Extract the archive
3. Run the executable: `./LinxTap` (or double-click)

No Python installation or dependencies required!

## Development Setup

### Requirements

- Python 3.10+
- PySide6

### Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run from Source

```bash
python main.py
```

Or use the convenience script:
```bash
./run.sh
```

## Tests

```bash
pytest tests/
```

## Building Executable

To create a standalone executable for distribution:

```bash
./build.sh
```

The executable will be created in `dist/LinxTap/`

### Distribution

After building, you can distribute the entire `dist/LinxTap/` folder. Users can run the application without installing Python or any dependencies.

## Project Structure

```
linxtap/
├── main.py              # Application entry point
├── build.sh             # Build script for creating executable
├── linxtap.spec         # PyInstaller configuration
├── src/
│   ├── core/            # Business logic
│   ├── ui/              # Qt widgets and windows
│   └── utils/           # Helper functions
├── tests/               # pytest tests
└── resources/           # Icons, assets
```
