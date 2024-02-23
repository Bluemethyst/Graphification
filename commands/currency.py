import nextcord
import httpx
import dotenv
import os
import json
import matplotlib.pyplot as plt
import io
from helpers import graph
from loggerthyst import info, warn, error, fatal
from nextcord.ext import commands
from PIL import Image


class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # PING
    @nextcord.slash_command(name="currency", description="Search for currency history")
    async def currency(
        self, interaction: nextcord.Interaction, year: int, month: int, day: int
    ):
        if month < 10 and day < 10:
            url = f"https://api.frankfurter.app/{year}-0{month}-0{day}?from=USD"
        elif month < 10:
            url = f"https://api.frankfurter.app/{year}-0{month}-{day}?from=USD"
        elif day < 10:
            url = f"https://api.frankfurter.app/{year}-{month}-0{day}?from=USD"
        print(url)
        data = httpx.get(url)
        print(data.text)
        data_json = data.json()
        rates = data_json["rates"]
        currencies = list(rates.keys())
        values = list(rates.values())
        plt.figure(figsize=(10, 5))
        plt.bar(currencies, values)
        plt.title("Currency Rates on " + data_json["date"])
        plt.xlabel("Currency")
        plt.ylabel("Rate")
        plt.xticks(rotation=45)
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        image_file = nextcord.File(fp=buf, filename="currency_rates.png")
        embed = nextcord.Embed(
            title=f"Currency Rates on {data_json['date']}", color=0x3346D1
        )
        embed.set_image(url="attachment://currency_rates.png")
        await interaction.response.send_message(embed=embed, file=image_file)

        info(command="Currency", interaction=interaction)
