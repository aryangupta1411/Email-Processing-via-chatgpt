import os

# Database configuration
DATABASE_PATH = os.environ.get('DATABASE_PATH', 'email_data.db')

# SMTP settings for email operations
SMTP_SETTINGS = {
    'server': os.environ.get('SMTP_SERVER', 'smtp.example.com'),
    'port': int(os.environ.get('SMTP_PORT', 587)),
    'user': os.environ.get('SMTP_USER', 'user@example.com'),
    'password': os.environ.get('SMTP_PASSWORD', 'password'),
    'sender': os.environ.get('SMTP_SENDER', 'sender@example.com')
}

# Email of the internal review team
INTERNAL_TEAM_EMAIL = os.environ.get('INTERNAL_TEAM_EMAIL', 'team@example.com')

# Configuration for ChatGPT interaction
CHATGPT_ENDPOINT = os.environ.get('CHATGPT_ENDPOINT', 'https://api.openai.com/v2/completions')
CHATGPT_API_KEY = os.environ.get('CHATGPT_API_KEY', 'YOUR_API_KEY')

# Tokenization secret key
SECRET_KEY = os.environ.get('TOKEN_SECRET_KEY', 'your_secret_key_here')
