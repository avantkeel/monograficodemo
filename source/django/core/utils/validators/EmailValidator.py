"""
This module provides a utility for validating email addresses. 
It leverages the `email-validator` library to ensure that emails 
meet standard formatting rules and have valid domain records.

Requires
idna==3.11
dnspython==2.8.0
email-validator==2.3.0

"""
from email_validator import validate_email, EmailNotValidError, EmailSyntaxError, EmailUndeliverableError

def is_email_valid(email_str: str):
    """
    Validates an email and returns either True or the error string.

    Example usage:
    ```
    result = is_email_valid("test@avantkeel.com")

    if result is True:
        print("Email is valid!")
    else:
        print(f"Validation failed: {result}")

    ```

    EMAIL-VALIDATOR ERROR CLASSES (Hierarchy)
    
    All specific errors inherit from EmailNotValidError.

    Here is the hierarchy organized as a clean, indented list:

    * **EmailNotValidError** (Base class for all validation errors)
        * **EmailSyntaxError** (The structure is wrong)
            * "The email address is empty."
            * "An email address must have exactly one @-sign."
            * "The domain name [...] contains invalid characters."
        * **EmailUndeliverableError** (The structure is OK, but the domain fails)
            * "The domain name [...] does not exist." (DNS check)
            * "The domain name [...] does not accept email." (No MX records)
    """
    check_dns: bool = True # check the internet if email is a valid domain

    try:
        validate_email(email_str, check_deliverability=check_dns)
        return True    
    except EmailNotValidError as error:
        return str(error)




