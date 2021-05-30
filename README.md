# Open in WhatsApp
<div align="center" width="100%">
<img width=200 src="logo.png">
</div>

> I was using a great [app](https://github.com/subhamtyagi/openinwa/) to open a whatsapp chat with a given number directly without saving that number in my contact list, but I felt it was overkill and uninstalled it, then searched telegram for a bot doint the same job but couldn't find so decided to make a new one.

## [See it in action](https://t.me/OiWA_bot)


## Requirements

- Python 3.6+

## Installation
- Clone this repo
  - `git clone https://github.com/416d72/oiwa`
  - `cd oiwa`

- Install requirements
  - `pip install -r requirements.txt`

- Create a new telegram bot using [Botfather](https://t.me/BotFather)

## Deploy to vercel
- Create a free account on [vercel](https://vercel.com)
- Create a new application
- Create required environment variable
  - DOMAIN: your vercel application URL
  - BOT_TOKEN: The token you received from botfather
- Use [vercel cli](https://vercel.com/cli) to upload to your application

## Setup webhook URL
- Just visit this url `https://<your-app>/vercel.app/setwebhook-f443dc992ba6`


##### Logo was designed by [dtafalonso](https://iconarchive.com/artist/dtafalonso.html) - [deviantart](https://www.deviantart.com/dtafalonso)
