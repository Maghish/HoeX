import discord
import json
from discord.ext import commands
from fun_config import *
from .util import util1

class Shop(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.group()
    async def shop(self, ctx):
        if ctx.invoked_subcommand == None:
            with open(shop_data_json_file, "r") as json_file:
                data = json.load(json_file)
            
            await util1.Shop(ctx, data).send()



    @commands.command()
    async def buy(self, ctx, shop_index: int, item_index: int, item_amount: int):
        res = await buy(ctx.author, shop_index, item_index, item_amount)


        



async def setup(client:commands.Bot) -> None:
    await client.add_cog(Shop(client))

