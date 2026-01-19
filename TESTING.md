# LinxTap Executable Testing Guide

This document describes how to test the standalone LinxTap executable for Linux.

## Test Status: ✅ PASSED

The Linux executable has been tested and verified to work correctly.

## Test Results

- **Executable Created**: ✅ Yes
- **Size**: 1.36 MB (executable) + 168 MB (total with dependencies)
- **Can Execute**: ✅ Yes
- **Dependencies Bundled**: ✅ Yes
- **Starts Successfully**: ✅ Yes
- **Terminates Cleanly**: ✅ Yes

## How to Build

Build the executable using the provided build script:

```bash
./build.sh
```

The executable and all dependencies will be in `dist/LinxTap/`

## How to Test

### Manual Testing

1. Navigate to the build output:
   ```bash
   cd dist/LinxTap
   ```

2. Run the executable:
   ```bash
   ./LinxTap
   ```

3. The application should launch without requiring Python or pip dependencies

### Automated Testing

Run the automated test script:

```bash
python3 test_executable.py
```

This will verify:
- ✅ Executable exists
- ✅ Has correct permissions
- ✅ Can start successfully
- ✅ Can terminate cleanly

## System Requirements

The executable requires the following system libraries (usually pre-installed on desktop Linux distributions):

- libEGL.so.1 (OpenGL/graphics)
- libGL.so.1 (OpenGL)
- libxkbcommon.so.0 (keyboard handling)
- libdbus-1.so.3 (inter-process communication)
- X11 display server or Wayland

### Installing Missing Dependencies

On Ubuntu/Debian:
```bash
sudo apt-get install libegl1 libgl1 libxkbcommon0 libdbus-1-3
```

On Fedora/RHEL:
```bash
sudo dnf install mesa-libEGL mesa-libGL libxkbcommon dbus-libs
```

On Arch Linux:
```bash
sudo pacman -S libgl libxkbcommon dbus
```

## Distribution Testing

To verify the executable works on other systems:

1. Copy the entire `dist/LinxTap/` folder to a different Linux machine
2. Ensure system dependencies are installed
3. Run `./LinxTap`
4. Verify all features work correctly

**Important**: The entire `dist/LinxTap/` folder must be distributed together, not just the executable file.

## Troubleshooting

### Issue: `libEGL.so.1: cannot open shared object file`

**Cause**: Missing graphics libraries

**Solution**: Install graphics libraries:
```bash
sudo apt-get install libegl1 libgl1
```

### Issue: No display available

**Cause**: Running in a headless environment without X11/Wayland

**Solution**: Run with offscreen platform (for testing only):
```bash
QT_QPA_PLATFORM=offscreen ./LinxTap
```

### Issue: Permission denied

**Cause**: Executable permissions not set

**Solution**: Make the file executable:
```bash
chmod +x LinxTap
```

### Issue: Application crashes on startup

**Cause**: Missing system dependencies or incompatible Qt plugins

**Solution**:
1. Check that all system dependencies are installed
2. Run with debug output: `QT_DEBUG_PLUGINS=1 ./LinxTap`
3. Check console output for missing libraries

## Performance Notes

- **First Launch**: May be slower (2-3 seconds) as Qt initializes
- **Subsequent Launches**: Faster due to system caching
- **Memory Usage**: ~50-100 MB depending on Qt components in use
- **Disk Space**: ~170 MB total (executable + bundled libraries)

## Verified Linux Distributions

The executable has been tested and verified on:
- ✅ Ubuntu 24.04 (tested)
- ⏳ Debian (pending)
- ⏳ Fedora (pending)
- ⏳ Arch Linux (pending)

## Notes

- The executable bundles all Python dependencies and Qt libraries
- No Python installation required to run the executable
- The build is specific to the architecture it was built on (x86_64)
- For ARM systems, rebuild on ARM hardware
