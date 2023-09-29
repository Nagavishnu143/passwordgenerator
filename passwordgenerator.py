import string
import secrets

def generate_password(length=12):
    # Define characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

# Usage: Change the length parameter as needed
password = generate_password(16)
print("Random Password:", password)
