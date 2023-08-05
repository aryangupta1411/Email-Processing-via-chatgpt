import time
import signal
import logging
from email_processor.email.ops import process_emails
from email_processor.config import CHECK_FREQUENCY, MAX_RETRIES
from email_processor import process_emails
from email_processor.utils.logging_util import logger
import sentry_sdk

sentry_sdk.init("YOUR_SENTRY_DSN")

if __name__ == "__main__":
    try:
        process_emails()
    except Exception as e:
        logger.error(f"Error in main process: {e}")
        # With Sentry initialized, it will also capture and send the exception.



# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

running = True
error_retries = 0

def signal_handler(signum, frame):
    global running
    logging.info("Shutdown signal received. Preparing to exit...")
    running = False

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    while running:
        try:
            process_emails()
            error_retries = 0
            time.sleep(CHECK_FREQUENCY)
        except Exception as e:
            error_retries += 1
            logging.error(f"Error encountered: {e}. Retrying...")

            if error_retries > MAX_RETRIES:
                logging.error(f"Max retries reached. Stopping the service.")
                running = False
            else:
                time.sleep(60 * error_retries)  # Exponential backoff

    logging.info("Email processing service stopped.")
