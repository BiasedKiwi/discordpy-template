# pylint: disable=no-self-use, import-error, too-few-public-methods
"""Cog containing all miscellaneous commands."""
import discord
from discord.ext import commands


class Miscellaneous(commands.Cog):
    """Cog class containing all miscellaneous commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_load(self):
        """Method called when the cog has been fully loaded."""
        print("The Miscellaneous cog is loaded.")

    @commands.command(
        name="ping", description="Get the current latency of the bot."
    )  # This could be implemented as a slash command.
    async def ping(self, ctx: commands.Context):
        """Get the current latency of the bot."""
        await ctx.channel.send(
            embed=discord.Embed(
                title="Pong!",
                description=f"The current latency of the bot is {round(self.bot.latency * 1000, 1)}ms.",  # pylint: disable=line-too-long
            )
        )


async def setup(bot: commands.Bot):  # pylint: disable=missing-function-docstring
    await bot.add_cog(Miscellaneous(bot))
