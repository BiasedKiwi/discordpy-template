# pylint: disable=missing-function-docstring, useless-super-delegation, import-error
"""File containing the bot constructor class."""
import os
import sys

from discord.ext import commands


class MinimalBot(commands.Bot):
    """Constructor class for the bot."""

    def __init__(self, *args, **kwargs):
        self.prefix = kwargs["command_prefix"]
        super().__init__(
            *args, **kwargs
        )  # Initialise a `Bot` instance with the parameters passed in the constructor.

    async def setup_hook(self):
        await self.load_cogs(client=self, directory="./src/cogs")

    async def load_cogs(self, client, directory: str, subdir: str = "") -> None:
        """Load all cogs in a given directory in a recursive fashion."""
        os.chdir(directory)
        base = os.getcwd()
        for file in os.listdir():  # Iterate through all the files in a directory
            if file.endswith(".py"):
                if subdir != "":
                    await client.load_extension(
                        f"src.cogs.{subdir}.{file[:-3]}"
                    )  # As of Discord.py 2.0, `load_extension` is a coroutine.
                else:
                    await client.load_extension(
                        f"src.cogs.{file[:-3]}"
                    )  # Refer to comment on line 61.
            elif os.path.isdir(os.path.join(base, file)):
                os.chdir(os.path.join(base, file))
                await self.load_cogs(client, os.getcwd(), subdir=file)  # Recursive call
                os.chdir(base)

    async def on_ready(self):
        """Method called when the `ready` event has been dispatched."""
        print("------")
        print("Logged in as")
        print(f"User: {self.user.name}")
        print(f"ID: {self.user.id}")
        print(f"Prefix: {self.prefix}")
        print("------")


if __name__ == "__main__":
    print("Please run \033[1m../launcher.py\033[0m instead of this file.")
    sys.exit(1)  # Exit the program where 1 is the exit code.
