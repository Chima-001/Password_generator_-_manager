# Password Generator & Manager





A Python project with two command-line tools: a **password strength checker & generator** and a **secure password manager** with Fernet encryption.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [1. Password Generator (`passwords.py`)](#1-password-generator-passwordspy)
- [2. Password Manager (`passwords_manager.py`)](#2-password-manager-passwords_managerpy)
- [Running Tests](#running-tests)
- [Security Disclaimer](#security-disclaimer)
- [License](#license)
- [Author](#author)

## Features

### Password Generator (`passwords.py`)
- Check the strength of any password you enter
- Generate strong, random passwords (16 characters by default) containing uppercase, lowercase, digits, and special characters
- Password strength scoring based on character complexity and length
- Detects weak/dictionary and commonly used passwords

### Password Manager (`passwords_manager.py`)
- Add, view, edit, and delete stored passwords
- Case-insensitive duplicate service prevention
- **Fernet encryption** for secure at-rest storage (via the `cryptography` package)
- Master password protection with encrypted master-password file
- Automatic encryption key generation and storage
- Save/load passwords to/from a file (`passwords.txt`)
- Option to generate a strong password when adding/editing an entry

## Project Structure

```
Password_generator_-_manager/
├── README.md
├── LICENSE                      # GNU General Public License v3.0
├── passwords.py                 # Password strength checker & generator
├── passwords_manager.py         # Command-line password manager (imports passwords.py)
├── test_passwords_manager.py    # Pytest test suite for the password manager
├── secret.key                   # Auto-generated Fernet encryption key (created at runtime)
├── master.txt                   # Auto-generated encrypted master password (created at runtime)
└── passwords.txt                # Auto-generated encrypted password store (created at runtime)
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Chima-001/Passwords_generator_manager.git
cd Passwords_generator_manager
```

2. Install the required dependency (the password manager needs the `cryptography` package for Fernet encryption):

```bash
pip install cryptography
```

No other external dependencies are required. `passwords.py` uses only Python standard-library modules (`random`, `string`).










## 1. Password Generator (`passwords.py`)

A simple script to test password strength and generate strong, random passwords.

### How to run

```bash
python passwords.py
```

### Usage

When prompted, enter one of the following:

| Input | Action |
|-------|--------|
| Any password | Tests and prints the strength score of that password |
| `g` | Generates a 16-character strong password, prints it, and tests its strength |
| `q` | Quits the program |

### Key functions

- `generate_password(length=16)` — Generates a random password guaranteed to include at least one uppercase letter, one lowercase letter, one digit, and one special character.
- `password_strength(password, min_length=10, strong_length=16)` — Returns a strength score (0–5) and prints a strength message.
- `word_complexity(word)` — Scores complexity based on presence of lowercase, uppercase, digits, and special characters.
- `main()` — Interactive CLI loop.

## 2. Password Manager (`passwords_manager.py`)

A secure command-line password manager that stores your passwords in an encrypted file, protected by a master password.

### How to run

```bash
python passwords_manager.py
```

### First-time setup

On the first run, you will be asked to create a master password. This password encrypts your stored passwords and the encryption key. **If you lose it, your passwords cannot be recovered.**

### Main menu

After entering your master password, you can choose from:

| Option | Action |
|--------|--------|
| 1. Add Password | Add a new service/username/password entry (type `g` to auto-generate a password) |
| 2. Edit Password | Change the password for an existing service |
| 3. Get Password | Retrieve the stored password for a service |
| 4. List Services | List all stored services alphabetically |
| 5. View All Passwords | Display every stored entry |
| 6. Delete Password | Remove an entry by service name |
| 7. Exit | Quit the program |

Enter `0` at the master-password prompt to quit.

### Classes

- **`Password(service, username, password)`** — Represents a single stored credential.
- **`PasswordVault(master_password)`** — Manages the password list, encryption, file I/O, and all CRUD operations.
  - `add_password(service, username, password)`
  - `get_password(service)`
  - `edit_password(service, new_password)`
  - `delete_password(service)`
  - `list_services()`
  - `gen_password()` — generates a 16-character password
  - `save_to_file(filename='passwords.txt')`
  - `load_from_file(filename='passwords.txt')`
  - `create_master_password()` / `get_master_password()` — master-password setup and retrieval

### Files created at runtime

| File | Purpose |
|------|---------|
| `secret.key` | Fernet encryption key (auto-generated on first run) |
| `master.txt` | Encrypted master password (created during first-time setup) |
| `passwords.txt` | Encrypted storage for all your password entries |

## Running Tests

The project includes a pytest test suite covering the `Password` and `PasswordVault` classes.

```bash
pip install pytest
pytest test_passwords_manager.py
```

> **Note:** Running the tests removes `master.txt` and `secret.key` if they exist. You will need to recreate your master password in `passwords_manager.py` afterward. To stop the cleanup after every test run, comment out or delete the lines 218-223 in the `test_passwords_manager.py`

## Security Disclaimer

This project is for educational and personal use. While it uses Fernet (symmetric encryption) from the `cryptography` package, it is **not a substitute for a professional-grade password manager**. Use at your own risk. Always keep backups of your master password and encryption key.

## License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.

## Author

**Chimamkpam Nnaji** — February 2026
