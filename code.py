import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1, generated_passwords=None):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    if generated_passwords is None:
        generated_passwords = set()

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
        ) and password not in generated_passwords:
            generated_passwords.add(password)
            break

    return password, generated_passwords


if __name__ == '__main__':
    generated_passwords = set()
    for _ in range(10):  # Generate 10 passwords
        new_password, generated_passwords = generate_password(generated_passwords=generated_passwords)
        print('Generated password:', new_password)



new version with pre list already on 

import re
import secrets
import string


def generate_password(length=6, nums=6, special_chars=0, uppercase=0, lowercase=0, generated_passwords=None):
    # Define the possible characters for the password (only digits)
    digits = string.digits

    if generated_passwords is None:
        generated_passwords = set()

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(digits)

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{string.punctuation}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
        ) and password not in generated_passwords:
            generated_passwords.add(password)
            break

    return password, generated_passwords


if __name__ == '__main__':
    # Pre-set list of passwords that are already in use
    pre_existing_passwords = {'', '', ''}

    # Initialize the generated passwords set with pre-existing passwords
    generated_passwords = pre_existing_passwords.copy()

    for _ in range(10):  # Generate 10 new passwords
        new_password, generated_passwords = generate_password(length=6, generated_passwords=generated_passwords)
        print('Generated password:', new_password)

    # Print all passwords in the set
    print("\nAll passwords in the set:")
    for password in generated_passwords:
        print(password)
