import dotenv
import os
import nextcord
from commands.ping import Ping
from loggerthyst import error, info, fatal, warn
from nextcord.ext import commands


bot = commands.Bot()
bot.add_cog(Ping(bot))
dotenv.load_dotenv()


@bot.event
async def on_ready():
    info(f"Logged in as {bot.user}")


bot.run(os.getenv("DISCORD_BOT_TOKEN"))
