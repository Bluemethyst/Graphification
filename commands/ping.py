import nextcord
from .. import loggerthyst
from loggerthyst import info, warn, error, fatal
from nextcord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # PING
    @nextcord.slash_command(
        description="Get the latency from the bot to Discords servers"
    )
    async def ping(self, interaction: nextcord.Interaction):
        latency = round(self.bot.latency * 1000, 0)
        embed = nextcord.Embed(title=f"Latency: {latency}MS", color=0x3346D1)
        await interaction.response.send_message(embed=embed)
        info(command="Ping", interaction=interaction)
