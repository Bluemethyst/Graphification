import nextcord
import httpx
import io
import time
import matplotlib.pyplot as plt
from nextcord.ext import commands
from loggerthyst import info


class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="currency", description="Search for currency history")
    async def currency(
        self,
        interaction: nextcord.Interaction,
        from_date: str,
        to_date: str,
        currency: str,
    ):
        start_time = time.perf_counter()
        url = f"https://api.frankfurter.app/{from_date}..{to_date}?from=USD"
        await interaction.response.defer()
        data = httpx.get(url).json()
        currency = currency.upper()
        rates = [data["rates"][date][currency] for date in data["rates"]]

        plt.figure(figsize=(10, 5))
        plt.plot(list(data["rates"].keys()), rates, marker="o")
        plt.title(
            f"{currency} Rate Change from {from_date} to {to_date} compared to USD"
        )
        plt.xlabel("Date")
        plt.ylabel(f"{currency} Rate")
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)

        image_file = nextcord.File(fp=buf, filename="currency_rate_change.png")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        embed = nextcord.Embed(
            title=f"{currency} Rate Change from {from_date} to {to_date}",
            color=0x3346D1,
        )
        embed.set_footer(text=f"{elapsed_time}")
        embed.set_image(url="attachment://currency_rate_change.png")
        await interaction.followup.send(embed=embed, file=image_file)
        info(command="Currency", interaction=interaction)
