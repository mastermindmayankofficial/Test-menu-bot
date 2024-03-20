from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define the /start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Menu Button Builder bot! Use /menu to create a menu.')

# Define the /menu command handler
def menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        ['Button 1', 'Button 2'],
        ['Button 3', 'Button 4']
    ]
    reply_markup = {"keyboard": keyboard, "resize_keyboard": True, "one_time_keyboard": True}
    update.message.reply_text('Here is your menu:', reply_markup=reply_markup)

def main() -> None:
    # Initialize the updater with your bot token
    updater = Updater("7046342417:AAHON_KjJl3HOBmvM5TDwF9eh0Z-YbogZVw")
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("menu", menu))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
