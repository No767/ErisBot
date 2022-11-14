import discord
import numpy as np
from discord import app_commands
from discord.ext import commands
from numpy.random import default_rng


class Fun(commands.Cog):
    """Fun small commands"""

    def __init__(self, bot):
        self.bot = bot

    fun = app_commands.Group(name="fun", description="Fun commands")

    @fun.command(name="8ball")
    async def magic8Ball(self, interaction: discord.Interaction, *, question: str):
        """A magic 8 ball...

        Args:
            interaction (discord.Interaction): Base interaction
            question (str): The question to ask
        """
        responses = np.array(
            [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful.",
            ]
        )
        rng = default_rng()
        answer = rng.choice(responses, replace=True)
        await interaction.response.send_message(
            f"Question: {question} \nAnswer: {answer}"
        )


async def setup(bot):
    await bot.add_cog(Fun(bot))
