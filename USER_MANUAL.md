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

LinxTap is a Linux desktop application built with Qt (PySide6). It provides a simple, user-friendly interface for desktop utility functions.

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

When you launch LinxTap, you'll see the main application window with:

- **Title Bar**: Shows "LinxTap" as the window title
- **Status Display**: Shows current status and feedback
- **Action Button**: Click to interact with the application

### Basic Operations

#### Clicking the Button

1. Look for the "Click Me" button in the center of the window
2. Click the button with your mouse
3. The status display will update to show the number of times you've clicked

**Example:**
- First click: "Button clicked 1 time(s)"
- Second click: "Button clicked 2 time(s)"
- And so on...

#### Window Controls

- **Minimize**: Click the minimize button in the window title bar
- **Maximize**: Click the maximize button to expand to full screen
- **Close**: Click the X button or press `Alt+F4` to close the application
- **Resize**: Drag the window edges or corners to resize (minimum size: 400x300 pixels)

### Keyboard Shortcuts

- `Alt+F4` - Close the application
- `Tab` - Navigate between interface elements
- `Space` or `Enter` - Activate focused button

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

Currently, settings are not persisted between sessions. All state is temporary and resets when you close the application.

### Is my data safe?

LinxTap runs entirely locally on your computer. No data is sent to external servers or the internet.

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
