# LinxTap

Desktop utility application for Linux.

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
