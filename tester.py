import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define your bot token here
TOKEN = '6432853196:AAGXjzRkMXZdBEwCcCSLhWo9-K-uaJ4iv1s'

# Define the ping function
def ping_website(update: Update, context: CallbackContext) -> None:
    website_url = 'http://example.com'  # Replace this with the URL you want to ping
    ping_results = []

    for _ in range(4):
        try:
            response = requests.get(website_url)
            ping_results.append(f'Status Code: {response.status_code}, Response Time: {response.elapsed.total_seconds()} seconds')
        except requests.RequestException as e:
            ping_results.append(f'Error: {e}')

    # Send ping results as a message to the Telegram chat
    update.message.reply_text('\n'.join(ping_results))

# Create the Updater and pass it your bot's token
updater = Updater(token=TOKEN)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register the /ping command handler
dispatcher.add_handler(CommandHandler("ping", ping_website))

# Start the Bot
updater.start_polling()

# Run the bot until you press Ctrl-C
updater.idle()
