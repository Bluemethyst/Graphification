import dotenv
import os
import nextcord
from commands.utils import Utils
from commands.weather import Weather
from commands.currency import Currency
from loggerthyst import error, info, fatal, warn
from nextcord.ext import commands

dotenv.load_dotenv()
intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)
bot.add_cog(Utils(bot))
bot.add_cog(Weather(bot))
bot.add_cog(Currency(bot))


@bot.event
async def on_ready():
    info(f"Logged in as {bot.user}")


bot.run(os.getenv("DISCORD_BOT_TOKEN"))

# this is a comment
