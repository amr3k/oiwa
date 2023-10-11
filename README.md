# Open in WhatsApp

![LICENSE](https://img.shields.io/github/license/amr3k/oiwa?style=flat&color=ff0000)
![GitHub issues](https://img.shields.io/github/issues/amr3k/oiwa?color=fdf629)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/amr3k/oiwa?color=c4fff9&label=Repo%20size)
![Lines of code](https://img.shields.io/tokei/lines/github/amr3k/oiwa?color=e63977)
[![Hits-of-Code](https://hitsofcode.com/github/amr3k/oiwa?branch=main)](https://hitsofcode.com/github/amr3k/oiwa/view?branch=main)


<div align="center" width="100%">
<img width=200 src="logo.png">
</div>

> I was using a great [app](https://github.com/subhamtyagi/openinwa/) to open a whatsapp chat with a given number directly without saving that number in my contact list, but I felt it was overkill and uninstalled it, then searched telegram for a bot doint the same job but couldn't find so decided to make a new one.

## [See it in action](https://t.me/OiWA_bot)


## Deploy your own bot to vercel with one click

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Famr3k%2Foiwa&env=DOMAIN,BOT_TOKEN&project-name=open-in-whatsapp&repo-name=open-in-whatsapp)

### Setup webhook URL
- Just visit this url `https://<your-app>/vercel.app/setwebhook-f443dc992ba6`


## Docker

- I added docker support but due to the big differences in the codebase, I implemented it in the [`docker` branch](https://github.com/amr3k/oiwa/tree/docker)

## Development
**Make sure you have Python `3.9` and [poetry](https://python-poetry.org/) installed.**

- Clone this repo
  - `git clone https://github.com/amr3k/oiwa`
  - `cd oiwa`
- Run
  - `poetry shell && poetry install`
  - `uvicorn main:app`


###### Logo was designed by [dtafalonso](https://iconarchive.com/artist/dtafalonso.html) - [deviantart](https://www.deviantart.com/dtafalonso)
