import logging
import os

import discord
from dotenv import load_dotenv
from eriscore import ErisCore

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] | %(asctime)s >> %(message)s",
    datefmt="[%m/%d/%Y] [%I:%M:%S %p %Z]",
)

DEV_GUILD = discord.Object(id=978546162745348116)
ERIS_TOKEN = os.getenv("ERIS_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = ErisCore(
    testing_guild_id=DEV_GUILD.id,
    intents=intents,
    command_prefix=".",
    help_command=None,
)

if __name__ == "__main__":
    bot.run(ERIS_TOKEN, log_handler=None)
