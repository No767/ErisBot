import discord
from discord import app_commands
from discord.ext import commands


class HelpSelect(discord.ui.Select):
    def __init__(self, bot) -> None:
        self.bot = bot
        options = [
            discord.SelectOption(label=cog_name, description=cog.__doc__)
            for cog_name, cog in sorted(bot.cogs.items())
        ]
        super().__init__(
            placeholder="Select a category",
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        cog = self.bot.get_cog(self.values[0])
        embed = discord.Embed(
            title=f"{cog.__cog_name__} Commands",
            description="\n".join(
                f"`/{command.qualified_name}`: {command.description}"
                for command in cog.walk_app_commands()
            ),
            color=discord.Color.from_rgb(255, 145, 244),
            timestamp=discord.utils.utcnow(),
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


class Help(commands.Cog):
    """Commands for getting commands and their info for ErisBot"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="The help page for ErisBot")
    async def erisHelp(self, interaction: discord.Interaction):
        """The help page for ErisBot
        Args:
            interaction (discord.Interaction): Interaction to respond to
        """
        embed = discord.Embed()
        embed.title = self.bot.user.name
        embed.description = f"{self.bot.user.name} is a bot that is not like others..."
        embed.add_field(name="Server Count", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="User Count", value=len(self.bot.users), inline=True)
        embed.add_field(
            name="Total Categories",
            value=str(len([cogs for cogs in self.bot.cogs])),
            inline=True,
        )
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        view = discord.ui.View().add_item(HelpSelect(self.bot))
        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Help(bot))
