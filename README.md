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


## Deploy with docker

### Requirements

- [docker-compose](https://github.com/docker/compose)

### Steps

- Edit `docker-compose.yml`
- Run `docker-compose up -d`

## Development
**Make sure you have Python `3.12` and [poetry](https://python-poetry.org/) installed.**

- Clone this repo
  - `git clone https://github.com/amr3k/oiwa`
  - `cd oiwa`
- Run
  - `poetry shell && poetry install`
  - `python main.py`
- Build
  - `docker buildx build --platform linux/amd64,linux/arm64 --load -t oiwa:latest .`
- Run a docker container from the built image
  - `docker run -d --name oiwa -e BOT_TOKEN=you_bot_token oiwa`


###### Logo was designed by [dtafalonso](https://iconarchive.com/artist/dtafalonso.html) - [deviantart](https://www.deviantart.com/dtafalonso)
