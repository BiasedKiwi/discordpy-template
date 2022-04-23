# discordpy-template
A minimal template for a Discord.py bot.

# Getting Started

To get started with this template, you will have to get your bot [token](https://docs.discordbotstudio.org/setting-up-dbs/finding-your-bot-token).

Once you have your token, you need to set the variable "BOT_DISCORD_TOKEN" in the file ".env" (It doesn't exist, create it.) Your ".env" file should look like this:

```shell
BOT_DISCORD_TOKEN=<your token>
```
You will also need to set the "BOT_CMD_PREFIX" variable in the same file.

```shell
BOT_DISCORD_TOKEN=<your token>
BOT_CMD_PREFIX=<your prefix>
```

Then, you can run the bot with the command:

```shell
python3 launcher.py
```
