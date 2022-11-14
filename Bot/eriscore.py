import logging
import os
from pathlib import Path

import discord
from discord.ext import commands


class ErisCore(commands.Bot):
    """The Core of Eris"""

    def __init__(self, testing_guild_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.testing_guild_id = testing_guild_id

    async def setup_hook(self) -> None:
        currPath = Path(__file__).parents[0]
        cogsList = os.listdir(os.path.join(str(currPath), "Cogs"))
        for cog in cogsList:
            if cog.endswith(".py"):
                await self.load_extension(f"Cogs.{cog[:-3]}")
        if self.testing_guild_id:
            guild = discord.Object(self.testing_guild_id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)

    async def on_ready(self) -> None:
        logging.info(f"{self.user.name} is ready")
        await self.change_presence(activity=discord.Game(name="/help for commands"))
