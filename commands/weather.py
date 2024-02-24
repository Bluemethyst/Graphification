# @formatter:off
import nextcord
from loggerthyst import info, warn, error, fatal
from nextcord.ext import commands
from helpers import graph
import httpx


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # WEATHER
    @nextcord.slash_command(description="Get the weather forecast for the next 24 hours")
    async def hourly_forecast(self, interaction: nextcord.Interaction, lat: float = 40.9006, long: float = 174.8860):
        await interaction.response.defer()

        raw = httpx.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,relative_humidity_2m,dew_point_2m,apparent_temperature,precipitation,rain,showers,snowfall&forecast_days=1")
        data = raw.json()

        timestamps = data["hourly"]["time"]
        temperature = data["hourly"]["temperature_2m"]
        apparent_temperature = data["hourly"]["apparent_temperature"]
        dewpoint = data["hourly"]["dew_point_2m"]
        humidity = data["hourly"]["relative_humidity_2m"]
        precipitation = data["hourly"]["precipitation"]
        rainfall = data["hourly"]["rain"]
        showers = data["hourly"]["showers"]
        snowfall = data["hourly"]["snowfall"]
        elevation = data["elevation"]

        image = graph.hourly_weather_graph(timestamps, temperature, apparent_temperature, dewpoint, humidity, precipitation, rainfall, showers, snowfall)

        embed = nextcord.Embed(title=f"24-hour forecast", description="Data pulled from `open-meteo.com`", color=0x3346D1)
        embed.add_field(name="Latitude", value=f"{lat}° S", inline=True)
        embed.add_field(name="Longitude", value=f"{long}° E", inline=True)
        embed.add_field(name="Elevation", value=f"{elevation}m", inline=True)
        embed.set_image(url="attachment://file.png")

        await interaction.followup.send(embed=embed, file=nextcord.File(image, filename="file.png"))
        info(command="Weather", interaction=interaction)
