# password_manager
A simple yet functional password manager built with Python. It allows you to generate strong passwords, encrypt them using AES, and store them locally in a secure, encrypted JSON file. The application features a graphical user interface (GUI) using Tkinter.

🚀 Features

    ✅ Strong, random password generation

    ✅ Secure local storage using AES encryption

    ✅ Encrypted password file (passwords.json)

    ✅ Simple graphical interface (Tkinter)

    ✅ Master password authentication

    ✅ Ability to view stored login data
    

🛠️ Technologies Used

    Python 3

    tkinter – GUI

    cryptography – AES encryption (via Fernet)

    json – Local data storage

💾 Data Storage

All credentials are stored locally in an encrypted JSON file named passwords.json.
Passwords are encrypted using a key derived from your master password (via PBKDF2HMAC + Fernet).

Example structure:
{
  "example.com": {
    "username": "user-user",
    "password": "gAAAAABi..."
  }
}
