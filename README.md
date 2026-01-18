# LinxTap

Cross-platform desktop utility application for Windows and Linux.

## Requirements

- Python 3.10+
- PySide6

## Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Tests

```bash
pytest tests/
```

## Project Structure

```
linxtap/
├── main.py              # Application entry point
├── src/
│   ├── core/            # Business logic
│   ├── ui/              # Qt widgets and windows
│   └── utils/           # Helper functions
├── tests/               # pytest tests
└── resources/           # Icons, assets
```
