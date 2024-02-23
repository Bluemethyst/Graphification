import datetime

import nextcord
from loggerthyst import info, warn, error, fatal
from nextcord.ext import commands
from helpers import graph
import httpx

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Weather
    @nextcord.slash_command(description="Get the weather forecast for the next 24 hours")
    async def hourly_forecast(self, interaction: nextcord.Interaction, lat: float = 40.9006, long: float = 174.8860):
        # fetch api stuff
        raw = httpx.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,relative_humidity_2m,dew_point_2m,rain&timezone=Pacific%2FAuckland&forecast_days=1")
        data = raw.json()

        timestamps = data["hourly"]["time"]
        temperature = data["hourly"]["temperature_2m"]
        humidity = data["hourly"]["relative_humidity_2m"]
        dewpoint = data["hourly"]["dew_point_2m"]
        rainfall = data["hourly"]["rain"]
        elevation = data["elevation"]

        image = graph.weather_graph(timestamps, temperature, humidity, dewpoint, rainfall)

        embed = nextcord.Embed(title=f"24-hour forecast", description="Data pulled from `open-meteo.com`", color=0x3346D1)
        embed.add_field(name="Latitude", value=f"{lat}° S", inline=True)
        embed.add_field(name="Longitude", value=f"{long}° E", inline=True)
        embed.add_field(name="Elevation", value=f"{elevation}m", inline=True)
        embed.set_image(url="attachment://file.png")

        await interaction.response.send_message(embed=embed, file=nextcord.File(image, filename="file.png"))
        info(command="Weather", interaction=interaction)
