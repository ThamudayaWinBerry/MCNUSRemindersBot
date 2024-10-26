import os
from telegram import Update, Bot
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the bot with the token from .env
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
application = Application.builder().token(bot_token).build()

# Define a function to print topic (thread) ID when a message is received
async def get_topic_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    topic_id = update.message.message_thread_id
    print("Group Chat ID:", chat_id)
    print("Topic ID:", topic_id)
    await update.message.reply_text(f"Group Chat ID: {chat_id}, Topic ID: {topic_id}")

# Add a handler for text messages
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_topic_id))

# Run the bot to capture topic ID
if __name__ == "__main__":
    application.run_polling()

