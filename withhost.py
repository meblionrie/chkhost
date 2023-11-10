import requests
import socket
import ping3
import subprocess
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6432853196:AAGXjzRkMXZdBEwCcCSLhWo9-K-uaJ4iv1s'
IPINFO_API_KEY = 'a3b6afcea3d006'  # Replace with your IPinfo API key

# Command handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    welcome_message = "Welcome to the Ping and IP Information Bot!\n\n" \
                      "You can use Commands Like Ping, Ipinfo, host, for detailed info do /help:" 
    update.message.reply_text(welcome_message)

# Command handler for the /help command
def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Available commands:\n"
        "/ping <website>: Ping a website 4 times.\n"
        "/host <hostname>: Get information about a host.\n"
        "/ipinfo <ip_address>: Get information about an IP address.\n"
        "/help: Show this help message."
    )
    update.message.reply_text(help_text)

# Command handler for the /ping command
def ping(update: Update, context: CallbackContext) -> None:
    website_url = context.args[0] if context.args else None

    if website_url:
        try:
            result = subprocess.run(['ping', '-c', '4', website_url], capture_output=True, text=True)
            output = result.stdout
        except Exception as e:
            output = f"Error: {e}"
    else:
        output = "Please provide a website URL to ping."

    update.message.reply_text(output)

# Command handler for the /host command
def host(update: Update, context: CallbackContext) -> None:
    host_name = context.args[0] if context.args else None

    if host_name:
        try:
            ip_address = socket.gethostbyname(host_name)
            host_info = f"Host: {host_name}\nIP Address: {ip_address}"
        except Exception as e:
            host_info = f"Error: {e}"
    else:
        host_info = "Please provide a valid host name or IP address."

    update.message.reply_text(host_info)

# Command handler for the /ipinfo command
def ipinfo(update: Update, context: CallbackContext) -> None:
    ip_address = context.args[0] if context.args else None

    if ip_address:
        try:
            # Request IPinfo API for IP address information
            response = requests.get(f'https://ipinfo.io/{ip_address}?token={IPINFO_API_KEY}')
            ip_info = response.json()
            
            info_text = f"IP Address: {ip_info.get('ip')}\n"
            info_text += f"Hostname: {ip_info.get('hostname')}\n"
            info_text += f"City: {ip_info.get('city')}\n"
            info_text += f"Region: {ip_info.get('region')}\n"
            info_text += f"Country: {ip_info.get('country')}\n"
            info_text += f"Location: {ip_info.get('loc')}\n"
            info_text += f"Timezone: {ip_info.get('timezone')}\n"
            info_text += f"Internet Provider: {ip_info.get('org')}\n"
            info_text += f"AS Number: {ip_info.get('asn')}\n"
            info_text += f"AS Name: {ip_info.get('as')}\n"

        except Exception as e:
            info_text = f"Error: {e}"
    else:
        info_text = "Please provide a valid IP address."

    update.message.reply_text(info_text)

    import telegram
    from telegram.ext import Updater, CommandHandler, CallbackContext
    import whois

    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    bot_token = 'YOUR_BOT_TOKEN'

    # Initialize the Telegram bot
    bot = telegram.Bot(token=bot_token)
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Define the /whois command handler
    def whois_lookup(updntext):
        if len(context.args) == 0:
                update.message.reply_text("Please provide a domain name for the WHOIS lookup.")
                    else:
                            domain_name = context.args[0]
                                    try:
                                                w = whois.whois(domain_name)
                                                            response = "Detailed WHOIS Lookup Results for {}:\n".format(domain_name)
                                                                        
                                                                                    # Iterate over WHOIS properties and add them to the response
                                                                                                for key, value in w.items():
                                                                                                                response += "{}: {}\n".format(key, value)

                                                                                                                            update.message.reply_text(response)
                                                                                                                                    except Exception as e:
                                                                                                                                                update.message.reply_text("An error occurred during the WHOIS lookup: {}".format(str(e)))

                                                                                                                                                # Add the /whois command handler to the dispatcher
                                                                                                                                                dispatcher.add_handler(CommandHandler('whois', whois_lookup, pass_args=True))

                                                                                                                            
                                                                                                                
if
# Main function to start the bot
def main() -> None:
    updater = Updater(TOKEN)

    # Register the /ping, /host, and /ipinfo command handlers
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('ping', ping))
    updater.dispatcher.add_handler(CommandHandler('host', host))
    updater.dispatcher.add_handler(CommandHandler('ipinfo', ipinfo))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
