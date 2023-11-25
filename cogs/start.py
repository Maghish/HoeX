import discord
from discord.ext import commands
from discord import app_commands
from fun_config import *


class Start(commands.Cog):
    
    def __init__(self, client: commands.Bot):
        self.client = client 

    @app_commands.command(name="start", description="Use this command to start a new journey!")
    async def start(self, interaction: discord.Interaction) -> None:
        await create_inventory(interaction.user)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Start(client))