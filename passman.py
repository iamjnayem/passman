import os
import sys
import base64
import json
import getpass
from cryptography.fernet import Fernet
from pathlib import Path

CONFIG_PATH = Path.home() / ".cli_passman_config"


def generate_key(master_password):
    return base64.urlsafe_b64encode(master_password.ljust(32)[:32].encode())


def load_config():
    if not CONFIG_PATH.exists():
        return {}
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)


def save_config(data):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(data, f)


def encrypt_data(key, data):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()


def decrypt_data(key, token):
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()


def add_password(master_key):
    config = load_config()
    site = input("Site: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    entry = {
        "username": encrypt_data(master_key, username),
        "password": encrypt_data(master_key, password)
    }
    config[site] = entry
    save_config(config)
    print("[+] Password saved.")


def get_password(master_key):
    config = load_config()
    site = input("Site: ")
    if site not in config:
        print("[-] No entry for this site.")
        return
    entry = config[site]
    username = decrypt_data(master_key, entry["username"])
    password = decrypt_data(master_key, entry["password"])
    print(f"Username: {username}\nPassword: {password}")


def list_sites():
    config = load_config()
    for site in config:
        print(f"- {site}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python passman.py [add|get|list]")
        return

    command = sys.argv[1]
    master_password = getpass.getpass("Master Password: ")
    key = generate_key(master_password)

    if command == "add":
        add_password(key)
    elif command == "get":
        get_password(key)
    elif command == "list":
        list_sites()
    else:
        print("Unknown command")


if __name__ == '__main__':
    main()

