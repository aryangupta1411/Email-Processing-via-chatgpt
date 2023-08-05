# email_processor/email/ops.py

import smtplib
from email.message import EmailMessage

from email_processor.token.ops import tokenize_email
from email_processor.chatgpt.ops import interact_with_chatgpt
from email_processor.config import SMTP_SETTINGS, INTERNAL_TEAM_EMAIL

def fetch_emails():
    """Fetch new emails from the server."""
    # Implement your email fetching logic here.
    # This will heavily depend on the email server you're working with.
    # Consider using libraries like 'imaplib' for IMAP-based fetching.

def process_emails():
    """Main processing logic for handling emails."""
    emails = fetch_emails()  # Get the new emails

    for email in emails:
        # Tokenize the sender's email address
        token = tokenize_email(email.sender)

        # Send the email content to ChatGPT and get a response
        response = interact_with_chatgpt(email.content)

        # Forward the response to the internal team for review
        forward_to_team(token, response)

def forward_to_team(token, response):
    """Forward the processed email to the internal team."""
    msg = EmailMessage()
    msg.set_content(response)
    msg['Subject'] = "ChatGPT Response Review"
    msg['From'] = SMTP_SETTINGS['sender']
    msg['To'] = INTERNAL_TEAM_EMAIL
    msg.add_header('X-Email-Token', token)

    with smtplib.SMTP(SMTP_SETTINGS['server'], SMTP_SETTINGS['port']) as server:
        server.login(SMTP_SETTINGS['user'], SMTP_SETTINGS['password'])
        server.send_message(msg)
