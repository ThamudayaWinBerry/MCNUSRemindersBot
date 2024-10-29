# MCNUSRemindersBot

This Telegram bot automatically sends special day messages, such as birthdays and holidays, to a designated chat. It reads dates and messages from a CSV file and posts them on the specified days. The bot is powered by the [python-telegram-bot](https://python-telegram-bot.readthedocs.io/) library and utilizes a virtual environment for isolated dependency management.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [CSV File Structure](#csv-file-structure)
5. [Getting Chat ID](#getting-chat-id)
6. [Configuration](#configuration)
7. [Contributing](#contributing)
8. [License](#license)

---

### Prerequisites

- Python 3.x
- [Telegram Bot Token](https://core.telegram.org/bots#botfather)
  
To get started, ensure you have a Telegram bot token, which can be obtained from the [BotFather](https://t.me/BotFather) on Telegram.

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Set up a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Configure your environment variables**:
   - Create a `.env` file in the project directory with the following content:

     ```plaintext
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token
     TARGET_CHAT_ID=your_telegram_chat_id
     TOPIC_ID=your_telegram_chat_topic_id
     ```

2. **Add your special days**:
   - Update `special_days.csv` with the dates and messages for special days.
   
3. **Run the bot**:

   ```bash
   python bot.py
   ```

The bot will now run and send scheduled messages to the specified chat on the dates listed in the CSV. Currently, it's using Github actions under .github/workflows for continuous deployment.

### CSV File Structure

The `special_days.csv` file should contain the following columns:

- `name`: The name of the intended recipient
- `message`: The content of the message to be sent
- `date`: The date to send the message (in `YYYY-MM-DD` format)


### Getting Chat ID

To send messages to a specific chat, you’ll need the chat ID. You can retrieve it using `getChatID.py`:

```bash
python getChatID.py
```

This will print the chat ID for any messages sent to your bot, which you can use in the `.env` file.