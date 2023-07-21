from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default="22500719", cast=int)
API_HASH = config("API_HASH", default="be0327edf200116b39eee7bd89582792")
BOT_TOKEN = config("BOT_TOKEN", default="6333358225:AAFPvhLljhwPuG2R2va4jH1223cLy7MPkb0")
BOT_UN = config("BOT_UN", default="Convart_Bot")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
