# Open in WhatsApp

## Why?

> I was using an [android open source app](https://github.com/subhamtyagi/openinwa/) for that specific purpose, but I was rarely using it, so I uninstalled it from my phone to free up some space (and memory?), then searched telegram a bot that does the same job but couldn't find any so decided to make a new one.

## Requirements

- Python 3.6+

## Installation
- Clone this repo
  - `git clone`
  - `cd oiwa`

- Install requirements
  - Using poetry (recommended): `poetry init`
  - Manually:
    - `pip install fastapi python-telegram-bot`

- Create a new telegram bot using [Botfather](@BotFather)

## Deploy to vercel
- Create a free account on [vercel](https://vercel.com)
- Create a new application
- Create required environment variable
  - DOMAIN: your vercel application URL
  - BOT_TOKEN: The token you received from botfather
- Use [vercel cli](https://vercel.com/cli) to upload to your application


Logo was designed by [dtafalonso](https://iconarchive.com/artist/dtafalonso.html) - [deviantart](https://www.deviantart.com/dtafalonso)
