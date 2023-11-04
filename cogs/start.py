from discord.ext import commands
from fun_config import *


class Start(commands.Cog):
    
    def __init__(self, client: commands.Bot):
        self.client = client 

    @commands.command()
    async def start(self, ctx):
        await create_inventory(ctx.author)
    
async def setup(client: commands.Bot) -> None:
    await client.add_cog(Start(client))