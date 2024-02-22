import dotenv
import os
import nextcord
from loggerthyst import error, info, fatal, warn
from nextcord.ext import commands


bot = commands.Bot()
dotenv.load_dotenv()


@bot.event
async def on_ready():
    info(f"Logged in as {bot.user}")


bot.run(os.getenv("DISCORD_BOT_TOKEN"))

# this is a comment
