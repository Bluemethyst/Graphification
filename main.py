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

# Prepare .env for token
dotenv.load_dotenv()
# Define Intents
intents = nextcord.Intents.all()
# Define bot object
bot = commands.Bot(intents=intents)
# Add cogs (external classes)
bot.add_cog(Utils(bot))
bot.add_cog(Weather(bot))
bot.add_cog(Currency(bot))


# Runs when the bots starts
@bot.event
async def on_ready():
    info(f"Logged in as {bot.user}")
    shared_data = SharedData()
    # Set the start time of the bot
    shared_data.set_bot_start_time(datetime.datetime.now())


# Run the bot
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
