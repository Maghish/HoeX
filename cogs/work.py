import discord
from discord.ext import commands
from datetime import datetime
from fun_config import *

class Work(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def sleep(self, ctx):
        # Get the data as users
        users = await get_inventory_data()
        # Check the user's max energy
        max_energy = int(users[str(ctx.author.id)]['Stats']['MaxEnergy'])
        users[str(ctx.author.id)]['Stats']['Energy'] = max_energy

        with open(inventory_json_file, "w") as json_file:
            json.dump(users, json_file, indent=1)

        await ctx.reply("You slept and refilled your energy!")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Work(client))
