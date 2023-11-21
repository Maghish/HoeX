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
        if not res[0]:
            if res[1] == 1:
                await ctx.reply("Shop not found, Please checkout `x shop` again and provide the right index")
            elif res[1] == 2:
                await ctx.reply("Item not found in the shop, Please checkout the shop again and provide the right index")
            elif res[1] == 3:
                await ctx.reply("You don't have enough money in your wallet to buy this item")
        else:
            await ctx.reply(f"You bought {res[2]}x {res[1]} from {res[3]}")


        



async def setup(client:commands.Bot) -> None:
    await client.add_cog(Shop(client))

