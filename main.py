import logging
import re
from os import environ
from random import sample

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)
from telegram.constants import ParseMode, ChatAction
from telegram.error import TelegramError

from dotenv import load_dotenv


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    blue = "\x1b[34;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: blue + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger("OiWA")
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)


load_dotenv()  # take environment variables from .env.

BOT_TOKEN = environ.get("BOT_TOKEN")

try:
    assert BOT_TOKEN != None
except AssertionError:
    logger.critical("Please set the environment variables")
    exit(1)

GREATINGS = [
    "Great! Here's your link:",
    "Sure thing! Take a look at this:",
    "Alright! You can find your link here:",
    "Here you go! Just click on the link below:",
    "No problem! I've got your link ready:",
    "Ready to go! Here's the link you need:",
    "Perfect! Your link is just a click away:",
    "Fantastic! You'll find your link right here:",
    "Alrighty! Look no further, your link awaits:",
    "Voilà! Here's the link you've been waiting for:",
    "Ta-da! Your link is all set up and ready:",
    "Behold! Your link is at your fingertips:",
    "Mission accomplished! Your link is here:",
    "Mission success! Here's the link you requested:",
    "Drumroll, please! Your link is here:",
    "Without further ado, here's your link:",
    "Your wish is my command! Here's your link:",
    "Eureka! I've found your link. Take a look:",
    "Look what I found! Your link is right here:",
    "And there you have it! Your link is ready to use:",
]


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hello {update.effective_user.full_name} 👋🏻\nPlease send a phone number you want to chat with",
    )


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="You can send the phone number you want to chat with (eg +447419651046)",
        parse_mode=ParseMode.HTML,
    )


async def wrong_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="❌ Wrong number",
    )


async def main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id, action=ChatAction.TYPING
    )
    try:
        phone_number_regex = re.compile(
            "(\+?( |-|\.)?\d{1,2}( |-|\.)?)?(\(?\d{3}\)?|\d{3})( |-|\.)?(\d{3}( |-|\.)?\d{4})"
        )
        extracted_phone_number = re.sub(r"[^\d]", "", update.effective_message.text)
        if extracted_phone_number:
            await phone_handler(update, context, extracted_phone_number)
        else:
            await wrong_number(update, context)
    except (AttributeError, TelegramError) as err:
        logging.error(f"🔴 Exception!: {err}\nupdate: {update}")


async def phone_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE, phone_number: str
):
    await context.bot.send_message(
        text=sample(GREATINGS, 1)[0],
        chat_id=update.effective_chat.id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🔗 Open chat",
                        url=f"https://api.whatsapp.com/send?phone={phone_number}&text=",
                    )
                ]
            ]
        ),
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    text_handler = MessageHandler(filters.TEXT, main)
    start_handler = CommandHandler("start", cmd_start)
    help_handler = CommandHandler("help", cmd_help)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(text_handler)

    application.run_polling()
