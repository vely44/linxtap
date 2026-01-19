@echo off
REM Build script for creating standalone executable on Windows

echo Building LinxTap executable...

REM Create venv if it doesn't exist
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
call venv\Scripts\activate.bat

REM Install build dependencies
echo Installing dependencies...
pip install -q -r requirements-build.txt

REM Clean previous builds
echo Cleaning previous builds...
if exist "build\" rmdir /s /q build
if exist "dist\" rmdir /s /q dist

REM Build executable
echo Building executable with PyInstaller...
pyinstaller --clean --noconfirm linxtap.spec

echo.
echo Build complete! Executable is in dist\LinxTap\
echo To test: cd dist\LinxTap ^&^& LinxTap.exe
