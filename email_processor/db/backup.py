import shutil

def backup_db():
    shutil.copy2('email_data.db', 'email_data_backup.db')
