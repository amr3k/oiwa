import re
from os import environ

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from telegram.bot import Bot
from telegram.chataction import ChatAction
from telegram.parsemode import ParseMode
from telegram.update import Update
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram.Error import Unauthorized

DOMAIN = environ.get("DOMAIN")
BOT_TOKEN = environ.get("BOT_TOKEN")
bot = Bot(BOT_TOKEN)

app = FastAPI()


@app.get("/robots.txt")
async def robots():
    return HTMLResponse("User-agent: *\nDisallow: /")


async def cmd_start(update: Update):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hello {update.effective_user.full_name} 👋🏻\nPlease send a phone number you want to chat with including international code",
        parse_mode=ParseMode.MARKDOWN_V2,
    )


async def cmd_help(update: Update):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="You can send the phone number you want to chat with **including international code** \(eg \+447419651046\)",
        parse_mode=ParseMode.MARKDOWN_V2,
    )


async def wrong_number(update: Update):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="❌ Wrong number",
        parse_mode=ParseMode.MARKDOWN_V2,
    )


async def phone_handler(update: Update):
    bot.send_message(
        text="ok",
        chat_id=update.effective_chat.id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🔗 Open chat",
                        url=f"https://api.whatsapp.com/send?phone={update.effective_message.text.replace(' ','').replace('-','')}",
                    )
                ]
            ]
        ),
    )


async def update_handler(update: Update):
    try:
        if update.effective_message.text:
            bot.send_chat_action(
                chat_id=update.effective_chat.id, action=ChatAction.TYPING
            )
            if update.effective_message.text == "/start":
                await cmd_start(update=update)
            elif update.effective_message.text == "/help":
                await cmd_help(update=update)
            elif re.fullmatch("\+[0-9\s?\-?]{5,20}", update.effective_message.text):
                await phone_handler(update=update)
            else:
                await wrong_number(update=update)
        else:
            cmd_help(update=update)
    except (Unauthorized, AttributeError):
        pass


@app.post("/telegram-update-4e1cb6")
async def webhook_handler(request: Request):
    data = await request.json()
    upcoming_update = Update.de_json(data, bot=bot)
    await update_handler(upcoming_update)
    return "ok"


@app.get("/setwebhook-f443dc992ba6")
async def set_webhook():
    s = bot.set_webhook(url=f"{DOMAIN}/telegram-update-4e1cb6")
    if s:
        return HTMLResponse("ok")
    else:
        return HTMLResponse("Error!")
