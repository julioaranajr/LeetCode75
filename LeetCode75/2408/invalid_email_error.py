"""
Module for demonstrating custom exceptions in Python.
"""

class InvalidEmailError(BaseException):
    """
    Custom exception class for representing an invalid email error.
    """


invalid_chars = [
    "@", " ", "!", "#", "$", "%", "^", "&", "*",
    "(", ")", "+", "=", "[", "]", "{", "}", "|", "\\",
    ":", ";", "'", "\"", "<", ">", ",", "?", "/"
    ]

EMAIL = None
USERNAME = None

def create_email(username):
    """
    Creates an email address based on the given username.
    Args:
        username (str): The username to be used in the email address.
    Raises:
        InvalidEmailError: If the username contains special characters.
    Returns:
        str: The generated email address.
    """

    if any(char in invalid_chars for char in username):
        raise InvalidEmailError("Username cannot contain special characters")
    else:
        email = f"{username}@python.org"
        return email

try:
    print('Example using: "john doe"')
    create_email("john doe") # Output: Username cannot contain special characters
    print(create_email("john doe"))
except InvalidEmailError as e:
    print(f'Error: {e}')
    print("Please try again. i.e. john.doe")
finally:
    username1 = input("Enter username: ").lower()
    print(create_email(username1))
    print("Email created successfully!")
