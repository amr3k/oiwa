import logging
import re
from os import environ
from random import sample

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, Response
from telegram.bot import Bot
from telegram.chataction import ChatAction
from telegram.parsemode import ParseMode
from telegram.update import Update
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram.error import TelegramError

from dotenv import load_dotenv

from helpers import logger

load_dotenv()  # take environment variables from .env.

DOMAIN = environ.get("DOMAIN")
BOT_TOKEN = environ.get("BOT_TOKEN")

try:
    assert DOMAIN != None
    assert BOT_TOKEN != None
except AssertionError:
    logger.critical("Please set the environment variables")
    exit(1)

try:
    bot = Bot(BOT_TOKEN)
except (TypeError, TelegramError):
    logger.critical("⚠️ Invalid bot token")
    exit(1)

app = FastAPI()
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


@app.get("/")
async def index():
    return HTMLResponse('<a href="/setwebhook">Setup webhook</a>')


@app.get("/robots.txt")
async def robots():
    return HTMLResponse("User-agent: *\nDisallow: /")


@app.get("/favicon.ico")
async def favicon():
    with open("favicon.png", "rb") as f:
        return Response(content=f.read(), media_type="image/png")


async def cmd_start(update: Update):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hello {update.effective_user.full_name} 👋🏻<br>Please send a phone number you want to chat with including international code",
    )


async def cmd_help(update: Update):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="You can send the phone number you want to chat with <b>including international code</b> (eg +447419651046)",
        parse_mode=ParseMode.HTML,
    )


async def wrong_number(update: Update):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="❌ Wrong number",
    )


async def phone_handler(update: Update):
    bot.send_message(
        text=sample(GREATINGS, 1)[0],
        chat_id=update.effective_chat.id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🔗 Open chat",
                        url=f"https://api.whatsapp.com/send?phone={update.effective_message.text.replace(' ','').replace('-','').replace('+','')}&text=",
                    )
                ]
            ]
        ),
    )


async def update_handler(update: Update):
    try:
        if update.effective_message and update.effective_message.text:
            bot.send_chat_action(
                chat_id=update.effective_chat.id, action=ChatAction.TYPING
            )
            if update.effective_message.text == "/start":
                await cmd_start(update)
            elif update.effective_message.text == "/help":
                await cmd_help(update)
            elif re.fullmatch("\+[0-9\s?\-?]{5,20}", update.effective_message.text):
                await phone_handler(update)
            else:
                await wrong_number(update)
        else:
            await cmd_help(update)
    except (AttributeError, TelegramError) as err:
        logging.error(f"🔴 Exception!: {err}\nupdate: {update}")


@app.post("/telegram-update")
async def webhook_handler(request: Request):
    data = await request.json()
    upcoming_update = Update.de_json(data, bot=bot)
    await update_handler(upcoming_update)
    return "ok"


@app.get("/setwebhook")
async def set_webhook():
    s = bot.set_webhook(url=f"{DOMAIN}/telegram-update")
    if s:
        return HTMLResponse("ok")
    else:
        return HTMLResponse("Error!")
