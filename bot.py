from pyrogram import Client
from config import *
import time
time.sleep(5)  # Wait 5 seconds before starting Pyrogram to allow time sync

class Bot(Client):
    def __init__(self):
        super().__init__(
            "compress-pdf-tg-bot",
            bot_token=Config.TG_BOT_TOKEN,
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            plugins={"root": "plugins"}
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.LOGGER.info(f"@{me.username} started!")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped. Bye.")

app = Bot()
app.run()
