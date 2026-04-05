"""
################################################################################
################################################################################

This module provides a utility for validating usernames.
It ensures that usernames follow standard security and formatting rules:
- Minimum and Maximum length
- Character restrictions (Only letters, numbers, and @/./+/-/_)
- No reserved system words

Example usage:
```
result = is_username_valid("henry")

if result is True:
    print("Username is available and valid.")
else:
    print(f"Errors: {', '.join(result)}")
```

################################################################################
################################################################################
"""

import re

def is_username_valid(username: str):
    """
    Validates a username based on Django's default standards.
    Returns True if valid, or a list of error messages if invalid.
    """
    errors = []

    # 1. Length Check
    if len(username) < 3:
        errors.append("Username must be at least 3 characters long.")
    elif len(username) > 150:
        errors.append("Username cannot exceed 150 characters.")

    # 2. Character Set Check (Alphanumeric + @/./+/-/_)
    # Matches Django's ASCIIUsernameValidator logic
    if not re.match(r'^[\w.@+-]+\Z', username):
        errors.append("Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.")

    # 3. Reserved Words
    reserved = ['admin', 'root', 'superuser', 'avantkeel', 'support', 'management']
    if username.lower() in reserved:
        errors.append(f"'{username}' is a reserved word and cannot be used.")

    if not errors:
        return True

    return errors


if __name__ == "__main__":
    test_usernames = ["hi", "admin", "valid_user_123", "user!name"]

    for user in test_usernames:
        res = is_username_valid(user)
        if res is True:
            print(f"[SUCCESS] '{user}' is valid.")
        else:
            print(f"[FAILURE] '{user}': {', '.join(res)}")
