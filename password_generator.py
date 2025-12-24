import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    special_chars = string.punctuation

    all_chars = ''
    if use_uppercase:
        all_chars += uppercase_chars
    if use_numbers:
        all_chars += digit_chars
    if use_special_chars:
        all_chars += special_chars
    all_chars += lowercase_chars

    if not all_chars:
        return "Error: No character type selected."

    password = []
    if use_uppercase:
        password.append(random.choice(uppercase_chars))
    if use_numbers:
        password.append(random.choice(digit_chars))
    if use_special_chars:
        password.append(random.choice(special_chars))
    password.append(random.choice(lowercase_chars))

    for i  in range(length - len(password)):
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

def main():
    length = int(input("Enter the password length (minimum 8): "))
    while length < 8:
        length = int(input("Password length must be at least 8. Please try again: "))
    use_uppercase = input("Include uppercase letters? (y/n): ") == "y".lower()
    use_numbers = input("Include numbers? (y/n): ") == "y".lower()
    use_special_chars = input("Include special characters? (y/n): ") == "y".lower()

    if not (use_uppercase or use_special_chars or use_numbers):
        print("Please select at least one character type.")
    else:
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print("Generated password:", password)

if __name__ == "__main__":
    main()