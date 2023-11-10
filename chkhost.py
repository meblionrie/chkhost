import subprocess
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update

# Telegram bot token (replace 'YOUR_BOT_TOKEN' with your actual bot token)
BOT_TOKEN = '6432853196:AAGXjzRkMXZdBEwCcCSLhWo9-K-uaJ4iv1s'

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am Website Ping Bot. Send me a website URL, and I will check if it\'s working.')

# Function to handle the /ping command
def ping(update: Update, context: CallbackContext) -> None:
    website_url = context.args[0]  # Extract website URL from command arguments
    try:
        # Run the ping command in the shell and capture the output
        ping_output = subprocess.check_output(['ping', '-c', '4', website_url]).decode('utf-8')
        update.message.reply_text(f'Ping details for {website_url}:\n{ping_output}')
    except Exception as e:
        update.message.reply_text(f'Error: {str(e)}. Unable to ping {website_url}.')

# Function to handle incoming messages and check website status
def check_website(update: Update, context: CallbackContext) -> None:
    website_url = update.message.text
    try:
        response = requests.get(website_url)
        if response.status_code == 200:
            update.message.reply_text(f'The website {website_url} is working fine! Status code: {response.status_code}')
        else:
            update.message.reply_text(f'The website {website_url} is not working. Status code: {response.status_code}')
    except Exception as e:
        update.message.reply_text(f'Error: {str(e)}. Unable to check the website {website_url}.')

# Main function to start the bot
def main() -> None:
    # Initialize the Updater and pass your bot token
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ping", ping))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, check_website))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
