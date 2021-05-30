# Open in WhatsApp

## Why?

> I was using an [android open source app](https://github.com/subhamtyagi/openinwa/) for that specific purpose, but I was rarely using it, so I uninstalled it from my phone to free up some space (and memory?), then searched telegram a bot that does the same job but couldn't find any so decided to make a new one.

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

### Some lessons I learned while developing this, I should have used polling in dev environment then after everthing works ok, push to cloud.