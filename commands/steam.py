import nextcord
import httpx
import dotenv
import os
from loggerthyst import info, warn, error, fatal
from nextcord.ext import commands
from steamgrid import SteamGridDB


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        dotenv.load_dotenv()
        self.sgdb = SteamGridDB(os.getenv("STEAM_GRID_API"))

    # PING
    @nextcord.slash_command(name="game", description="Check the bots latencys")
    async def game(self, interaction: nextcord.Interaction, game):
        result = self.sgdb.search_game(game)
        embed = nextcord.Embed(title=f"Result: {result}", color=0x3346D1)
        await interaction.response.send_message(embed=embed)
        info(command="Game", interaction=interaction)
