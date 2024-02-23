import nextcord
from loggerthyst import info, warn, error, fatal
from nextcord.ext import commands
from helpers import graph
import httpx


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Weather
    @nextcord.slash_command(description="Get the latency from the bot to Discords servers")
    async def weather(self, interaction: nextcord.Interaction, lat: float = 40.9006, long: float = 174.8860):
        # fetch api stuff
        raw = httpx.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m&timezone=Pacific%2FAuckland&forecast_days=14")
        data = raw.json()

        temperature_2m = data["hourly"]["temperature_2m"]
        image = graph.graph("tewmperwaturwe", temperature_2m)

        embed = nextcord.Embed(title=f"Temperature data", color=0x3346D1)
        embed.set_image(nextcord.File(image))
        await interaction.response.send_message(embed=embed)

        info(command="Weather", interaction=interaction)
