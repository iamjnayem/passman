#  CLI Password Manager

A minimal and secure command-line password manager built with Python. Store and retrieve site credentials securely using encryption.

## Features

- AES encryption via `cryptography.Fernet`
- CLI commands: `add`, `get`, `list`
- Stores encrypted credentials locally
- Uses master password to derive encryption key

##  Requirements

- Python 3.7+
- `cryptography` library

```bash
pip install cryptography
```

## Usage
- ```bash python passman.py add ```     # Add new credential
- ```bash python passman.py get ```    # Retrieve credential
- ```bash python passman.py list ```   # List all saved sites
