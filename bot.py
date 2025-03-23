import os
from pyrogram import Client


if bool(os.environ.get("ENV", False)):
    from config.py import LOGGER


class Bot(Client):
    def __init__(self):
        super().__init__(
            "compress-pdf-tg-bot",
            bot_token=Config.py TG_BOT_TOKEN,
            api_id=Config.py APP_ID,
            api_hash=Config.py API_HASH,
            plugins={
                "root": "plugins"
            },
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{me.username}  started! "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")


app = Bot()
app.run()

