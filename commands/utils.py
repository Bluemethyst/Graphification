import nextcord
import psutil
import cpuinfo
from helpers.shared_data import SharedData
from loggerthyst import info, warn, error, fatal
from nextcord.ext import commands


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # PING
    @nextcord.slash_command(name="ping", description="Check the bots latency")
    async def ping(self, interaction: nextcord.Interaction):
        latency = round(self.bot.latency * 1000, 0)
        embed = nextcord.Embed(title=f"Latency: {latency}MS", color=0x3346D1)
        await interaction.response.send_message(embed=embed)
        info(command="Ping", interaction=interaction)

    # INFO
    @nextcord.slash_command(description="Get information about the bot")
    async def info(self, interaction: nextcord.Interaction):
        cpu_info = cpuinfo.get_cpu_info()
        cpu_name = cpu_info["brand_raw"]
        python_version = cpu_info["python_version"]
        architecture = cpu_info["arch"]

        memory = psutil.virtual_memory()
        memory_used_gb = memory.used / (1024**3)
        memory_total_gb = memory.total / (1024**3)
        memory_percentage = memory.percent
        cpu = psutil.cpu_percent()

        shared_data = SharedData()
        bot_start_time = shared_data.get_bot_start_time()
        unix_timestamp = int(bot_start_time.timestamp())

        embed = nextcord.Embed(title="Info", color=0x3346D1)
        embed.add_field(
            name="Bot",
            value="Written in Python using the Nextcord wrapper for the Discord API and hosted on an OVH VPS\n[Source](https://github.com/Bluemethyst/Graphification)",
        )
        embed.add_field(name="CPU", value=f"{cpu_name}\n{cpu.real}% in use")
        embed.add_field(name="Architecture", value=architecture)
        embed.add_field(
            name="Memory",
            value=f"{memory_used_gb:.2f}GB/{memory_total_gb:.2f}GB\n{memory_percentage}% in use",
        )
        embed.add_field(name="Python", value=python_version)
        embed.add_field(name="Startup Time", value=f"<t:{unix_timestamp}:R>")

        await interaction.response.send_message(embed=embed)
        info(command="Info", interaction=interaction)
