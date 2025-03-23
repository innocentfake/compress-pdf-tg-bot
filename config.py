import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7957115059:AAEH2NMjbx1SV7SitAbLnsJ1ABt9AHnrMwM")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "28738604"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "d6c3504a2e44088fefd045f9cbfcfae8")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
