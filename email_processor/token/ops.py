# email_processor/token/ops.py

import hashlib

SECRET_KEY = "your_secret_key_here"  # Change this to a secure random string!

def tokenize_email(email_address):
    """Generate a token for an email address."""
    return hashlib.sha256((email_address + SECRET_KEY).encode()).hexdigest()
