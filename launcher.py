# pylint: disable=import-error, missing-function-docstring
"""Launcher script for the bot"""
import os

import discord
from dotenv import load_dotenv

from src import MinimalBot

load_dotenv()


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = MinimalBot(
        intents=intents,
        command_prefix=os.environ.get("BOT_CMD_PREFIX"),
    )
    bot.run(os.environ.get("BOT_DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
