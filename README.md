# Password_generator_&_manager






#   1. Password Generator

A simple Python script to generate secure, random passwords based on user preferences.

## Features
- Customizable password length (minimum 8 characters)
- Option to include uppercase letters, numbers, and special characters
- At least one character type required
- Randomly generated passwords

## Usage
1. Run the script
2. Enter the desired password length (minimum 8)
3. Choose character types to include (uppercase, numbers, special characters)
4. Get your generated password!

## Code Structure
- `generate_password(length, use_uppercase, use_numbers, use_special_chars)`: generates a password based on inputs
- `main()`: handles user input and output

## Requirements
- Python 3.x
- `random` and `string` libraries (built-in)










#   2. Password Manager

A simple command-line password manager written in Python.

## Features
- Secure password storage with base64 encryption
- Generate strong, random passwords
- Add, retrieve, list, and delete passwords
- Save and load passwords from a file

## Usage
1. Run the script
2. Enter the master password (default: 'master')
3. Choose an option from the menu:
   - Add Password: add a new password
   - Get Password: retrieve a password
   - List Services: list stored services
   - Generate Password: generate a strong password
   - View All Passwords: view all stored passwords
   - Delete Password: delete a password
   - Save Password: save passwords to file
   - Exit: quit the program

## Code Structure
- `Password`: represents a password with service, username, and password
- `PasswordVault`: manages a list of passwords and provides encryption/decryption
- `main()`: handles user input and output

## Requirements
- Python 3.x
- `base64` library (built-in)
- `password_generator` module (separate file)
