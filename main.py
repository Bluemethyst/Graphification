import dotenv
import os
import nextcord
import datetime
from commands.utils import Utils
from commands.weather import Weather
from commands.currency import Currency
from loggerthyst import error, info, fatal, warn
from nextcord.ext import commands
from helpers.shared_data import SharedData

dotenv.load_dotenv()
intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)
bot.add_cog(Utils(bot))
bot.add_cog(Weather(bot))
bot.add_cog(Currency(bot))


@bot.event
async def on_ready():
    info(f"Logged in as {bot.user}")
    shared_data = SharedData()
    shared_data.set_bot_start_time(datetime.datetime.now())


bot.run(os.getenv("DISCORD_BOT_TOKEN"))
