import asyncio
import logging
import time
from pyrogram import Client
from config import *

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

# Introduce a delay to allow Heroku's clock to sync
time.sleep(5)

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
        retry_count = 5  # Maximum retry attempts
        delay = 5  # Delay between retries in seconds

        for attempt in range(retry_count):
            try:
                await super().start()
                me = await self.get_me()
                self.LOGGER.info(f"Bot @{me.username} started successfully!")
                break  # Exit loop if successful
            except Exception as e:
                self.LOGGER.error(f"Start attempt {attempt + 1} failed: {e}")
                if attempt < retry_count - 1:
                    self.LOGGER.info(f"Retrying in {delay} seconds...")
                    await asyncio.sleep(delay)
                else:
                    self.LOGGER.critical("Max retries reached. Exiting.")
                    return

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped. Bye.")

app = Bot()

if __name__ == "__main__":
    app.run()
