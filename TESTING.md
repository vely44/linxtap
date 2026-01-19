# Testing Guide for LinxTap Executables

This document describes how to test the standalone executables on different platforms.

## Linux Testing

### Test Status: ✅ PASSED

The Linux executable has been tested and verified to work correctly.

### Test Results

- **Executable Created**: ✅ Yes
- **Size**: 1.36 MB (executable) + 168 MB (total with dependencies)
- **Can Execute**: ✅ Yes
- **Dependencies Bundled**: ✅ Yes
- **Starts Successfully**: ✅ Yes

### How to Test on Linux

1. Build the executable:
   ```bash
   ./build.sh
   ```

2. The executable will be in `dist/LinxTap/`

3. Test the executable:
   ```bash
   cd dist/LinxTap
   ./LinxTap
   ```

4. The application should launch without requiring Python or pip dependencies

### System Requirements (Linux)

The executable requires the following system libraries (usually pre-installed on desktop Linux):
- libEGL.so.1
- libGL.so.1
- libxkbcommon.so.0
- libdbus-1.so.3
- X11 display server (or Wayland)

On Ubuntu/Debian, install missing libraries with:
```bash
sudo apt-get install libegl1 libgl1 libxkbcommon0 libdbus-1-3
```

## Windows Testing

### Test Status: ⏳ PENDING

Windows testing needs to be performed on an actual Windows machine.

### How to Test on Windows

1. On a Windows machine with Python 3.10+ installed, build the executable:
   ```cmd
   build.bat
   ```

   Or manually:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements-build.txt
   pyinstaller --clean --noconfirm linxtap.spec
   ```

2. The executable will be in `dist\LinxTap\`

3. Test the executable:
   ```cmd
   cd dist\LinxTap
   LinxTap.exe
   ```

4. The application should launch without requiring Python installation

### Expected Results for Windows

- [ ] Executable builds without errors
- [ ] Executable runs without requiring Python
- [ ] Application window opens
- [ ] Application functions correctly
- [ ] No missing DLL errors

### System Requirements (Windows)

- Windows 10 or later
- No Python installation required for running the executable
- Visual C++ Redistributable (usually already installed)

## Distribution Testing

After building the executable, test distribution by:

1. Copying the entire `dist/LinxTap/` folder to a different machine
2. Running the executable on a machine without Python installed
3. Verifying all features work correctly

## Automated Testing

Run the automated test script (Linux only):
```bash
python3 test_executable.py
```

This will verify:
- Executable exists
- Has correct permissions
- Can start successfully
- Can terminate cleanly

## Notes

- The executable includes all Python dependencies
- The entire `dist/LinxTap/` folder must be distributed together (not just the executable)
- First launch may be slower as Qt initializes
- The executable is platform-specific (Linux builds run on Linux, Windows builds run on Windows)

## Troubleshooting

### Linux

**Issue**: `libEGL.so.1: cannot open shared object file`
**Solution**: Install graphics libraries:
```bash
sudo apt-get install libegl1 libgl1
```

**Issue**: No display available
**Solution**: Ensure X11 or Wayland is running, or run with:
```bash
QT_QPA_PLATFORM=offscreen ./LinxTap
```

### Windows

**Issue**: Missing DLL errors
**Solution**: Install Visual C++ Redistributable from Microsoft

**Issue**: Windows Defender blocks the executable
**Solution**: This is normal for unsigned executables. Add an exception or sign the executable with a code signing certificate.
