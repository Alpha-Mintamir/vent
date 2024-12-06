import os
import csv
import logging
from dotenv import load_dotenv
from telethon import TelegramClient

# Set the absolute path to save the scraped data
scrapped_data_dir = r'C:\Templates\vent\data'

# Ensure the scrapped_data directory exists
if not os.path.exists(scrapped_data_dir):
    os.makedirs(scrapped_data_dir)

# Set up logging configuration
logging.basicConfig(
    filename=os.path.join(scrapped_data_dir, 'scraper.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Load environment variables from .env file
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('PHONE')  # Unused but can be added if needed
channel_username = os.getenv('CHANNEL_USERNAME')  # Add channel username in .env

# Check if API credentials and channel username are available
if not api_id or not api_hash or not channel_username:
    logging.error("Missing API ID, API Hash, or Channel Username in environment variables.")
    raise ValueError("Please set TG_API_ID, TG_API_HASH, and CHANNEL_USERNAME in your .env file.")

# Initialize Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def scrape_telegram_channel():
    async with client:
        try:
            # Open CSV file to save messages
            csv_file_path = os.path.join(scrapped_data_dir, 'telegram_messages.csv')
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['date', 'message']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                # Loop through all messages and write to CSV
                async for message in client.iter_messages(channel_username):
                    writer.writerow({
                        'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
                        'message': message.text or '[Media or Non-Text Message]'
                    })

            logging.info("Messages scraped successfully!")
            print("Messages scraped successfully! File saved at:", csv_file_path)

        except Exception as e:
            logging.error(f"Error scraping channel: {str(e)}")
            print(f"Error scraping channel: {str(e)}")

# Run the script
if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(scrape_telegram_channel())
