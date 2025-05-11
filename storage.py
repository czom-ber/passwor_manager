import json
import os

DATA_FILE = "passwords.json"

def save_encrypted_entry(site, username, encrypted_password):
    data = load_data()
    data[site] = {
        "username": username,
        "password": encrypted_password
    }
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
