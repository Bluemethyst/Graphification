import nextcord
from loggerthyst import info, warn, error, fatal
from nextcord.ext import commands
import httpx


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Weather
    @nextcord.slash_command(
        description="Get the latency from the bot to Discords servers"
    )
    async def weather(
        self,
        interaction: nextcord.Interaction,
        lat: int = 40.9006,
        long: int = 174.8860,
    ):
        # fetch api stuff
        raw = httpx.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m&timezone=Pacific%2FAuckland&forecast_days=14"
        )
        data = raw.json()

        temperature_2m = data["temperature_2m"]

        embed = nextcord.Embed(
            title=f"Temperature data",
            description=f"'''{temperature_2m}'''",
            color=0x3346D1,
        )
        await interaction.response.send_message(embed=embed)

        info(command="Weather", interaction=interaction)
