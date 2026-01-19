#!/bin/bash
# Build script for creating standalone executable

set -e

echo "Building LinxTap executable..."

# Create venv if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install build dependencies
echo "Installing dependencies..."
pip install -q -r requirements-build.txt

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist

# Build executable
echo "Building executable with PyInstaller..."
pyinstaller --clean --noconfirm linxtap.spec

echo ""
echo "Build complete! Executable is in dist/LinxTap/"
echo "To test: cd dist/LinxTap && ./LinxTap"
