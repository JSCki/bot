import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Path to the folder containing random images
IMAGE_FOLDER = "images"

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Refresh", callback_data="refresh")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Click 'Refresh' to receive a random image!", reply_markup=reply_markup
    )

# Function to send a random image
def send_random_image(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    # Select a random image
    image_path = random.choice(os.listdir(IMAGE_FOLDER))
    full_path = os.path.join(IMAGE_FOLDER, image_path)

    # Send the image
    query.message.reply_photo(photo=open(full_path, "rb"))

    # Add the "Refresh" button
    keyboard = [[InlineKeyboardButton("Refresh", callback_data="refresh")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_caption(caption="Here's a random image!", reply_markup=reply_markup)

def main():
    # Replace 'YOUR_BOT_TOKEN' with your Telegram bot token
    updater = Updater("7629367266:AAGK-Qcv0xmFHctTtTm1SM_SihDYOkj-2uw")

    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(send_random_image))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
  
