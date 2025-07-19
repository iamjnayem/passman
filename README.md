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

## How It Works
You provide a master password (not stored anywhere).

A symmetric encryption key is derived using base64 encoding.

Credentials are encrypted and saved in ~/.cli_passman_config.

## Concepts Used
CLI design with sys.argv

Secure password input with getpass

Key derivation for encryption

Fernet symmetric encryption

File I/O and JSON config management

Basic software security practices

# Example
```bash
$ python passman.py add
Master Password: ********
Site: github.com
Username: john_doe
Password: ********
[+] Password saved.
```
```bash
$ python passman.py get
Master Password: ********
Site: github.com
Username: john_doe
Password: my_secure_password
```

## Security Note
This project is for learning/demo purposes.
Do not use in production without proper key derivation (e.g., PBKDF2).

## 
Want enhancements like:
- AES with PBKDF2 + salt
- TUI (Text UI) with `rich` or `prompt_toolkit`
- Tests with `pytest`
- Dependency injection
- GitHub Actions CI?

Let me know — happy to upgrade this into a portfolio-grade project.
