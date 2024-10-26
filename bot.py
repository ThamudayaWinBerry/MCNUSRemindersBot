import os
import pandas as pd
import asyncio
from datetime import datetime
from telegram import Bot
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the bot with the token from .env
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=bot_token)

# Load group chat ID and topic ID from environment variables
target_chat_id = os.getenv("TARGET_CHAT_ID")
topic_id = int(os.getenv("TOPIC_ID"))  # Convert to integer if stored as string in .env

async def send_special_day_messages():
    # Load CSV data
    data = pd.read_csv("special_days.csv")
    print("Loaded CSV data:", data)  # Debug print

    # Get today's date
    today = datetime.today().strftime('%Y-%m-%d')
    print("Today's date:", today)  # Debug print

    # Filter messages for today
    today_data = data[data['date'] == today]
    print("Today's matching data:", today_data)  # Debug print

    # Send messages for each entry matching today's date in the specified topic
    if not today_data.empty:
        for index, row in today_data.iterrows():
            message = f"{row['message']}, {row['name']}!"
            await bot.send_message(chat_id=target_chat_id, text=message, message_thread_id=topic_id)
            print(f"Sent message: {message}")
    else:
        print("No messages to send today.")

# Run the async function
if __name__ == "__main__":
    asyncio.run(send_special_day_messages())
