import nextcord
import httpx
import io
import time
import matplotlib.pyplot as plt
from nextcord.ext import commands
from loggerthyst import info, warn, error, fatal


class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # CURRENCY
    @nextcord.slash_command(name="currency", description="Search for currency history")
    async def currency(
        self,
        interaction: nextcord.Interaction,
        from_date: str,
        to_date: str,
        currency: str,
    ):
        # Start timer
        if currency.upper() == "USD":
            await interaction.response.send_message(
                "Unfortunately you cannot view the history of USD as it is used as a baseline for comparing other currencies."
            )
            return
        start_time = time.perf_counter()
        # Collect data
        url = f"https://api.frankfurter.app/{from_date}..{to_date}?from=USD"
        await interaction.response.defer()
        r = httpx.get(url)
        data = r.json()
        currency = currency.upper()
        # Create data array/list for graph to use
        rates = [data["rates"][date][currency] for date in data["rates"]]
        # Create the graph
        plt.figure(figsize=(10, 5))
        plt.plot(list(data["rates"].keys()), rates, marker="o")
        plt.title(
            f"{currency} Rate Change from {from_date} to {to_date} compared to USD"
        )
        plt.xlabel("Date")
        plt.ylabel(f"{currency} Rate")
        plt.grid(True)
        # Convert the graphs bytes into a png
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        # Attach png as attachment and send
        image_file = nextcord.File(fp=buf, filename="currency_rate_change.png")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        embed = nextcord.Embed(
            title=f"{currency} Rate Change from {from_date} to {to_date} compared to USD",
            color=0x3346D1,
        )
        embed.set_footer(text=f"Took {round(elapsed_time, 3)} seconds to render")
        embed.set_image(url="attachment://currency_rate_change.png")
        await interaction.followup.send(embed=embed, file=image_file)
        info(command="Currency", interaction=interaction)
