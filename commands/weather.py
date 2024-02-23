import nextcord
from .. import loggerthyst
from loggerthyst import info, warn, error, fatal
from nextcord.ext import commands

import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Weather
    @nextcord.slash_command(description="Get the latency from the bot to Discords servers")
    async def weather(self, interaction: nextcord.Interaction):
        # fetch api stuff
        raw = httpx.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&timezone=Pacific%2FAuckland&forecast_days=14")
        print(raw)

        embed = nextcord.Embed(title=f"Latency: {latency}MS", color=0x3346D1)
        await interaction.response.send_message(embed=embed)

        info(command="Ping", interaction=interaction)
