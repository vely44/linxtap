# 📥 Download Pre-Built Executables

## 🪟 Windows

### Download Ready-to-Run .exe

**Option 1: GitHub Actions Artifacts** (Recommended)

1. Go to: https://github.com/vely44/linxtap/actions
2. Click on the latest **"Build Windows Executable"** workflow
3. Scroll down to **"Artifacts"**
4. Download **"LinxTap-Windows"**
5. Extract the .zip file
6. **Double-click `LinxTap.exe`** - Done! No installation needed!

**Option 2: Releases** (When available)

1. Go to: https://github.com/vely44/linxtap/releases
2. Download `LinxTap.exe` from the latest release
3. **Double-click to run** - No installation needed!

### First Run

When you first run LinxTap.exe:

1. **Windows SmartScreen** might appear → Click "More info" → "Run anyway"
2. **Windows Firewall** might ask → Click "Allow access"

That's it! The app will open.

---

## 🐧 Linux

### Download Ready-to-Run Executable

Build is automatic - coming soon!

For now, use:
```bash
./build.sh
./dist/LinxTap/LinxTap
```

---

## ⚙️ How Auto-Build Works

Every time code is pushed:
1. GitHub Actions automatically builds the Windows .exe
2. The .exe is uploaded as an artifact
3. You can download it anytime (no building needed!)

The .exe is:
- ✅ Self-contained (no .NET installation required)
- ✅ Single file (~25-30 MB)
- ✅ Just double-click to run
- ✅ Works on Windows 10 (1809+) and Windows 11

---

## 🚨 Important

**Never commit .exe files to git!** They are:
- Too large for version control
- Binary files (hard to diff)
- Platform-specific

Instead, we auto-build them and provide downloads.
