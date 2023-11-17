import discord
from discord.ext import commands
from fun_config import *
from datetime import datetime


class Inventory(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.command()
    async def stats(self, ctx):
        # Get the data as users
        users = await get_inventory_data()
        # Check if the user has already started
        if str(ctx.author.id) in users:
            # If so, create the user's stats embed
            embed = discord.Embed(
                title=f"{ctx.author.global_name}'s Stats",
                description="Here you can view your Health, Energy and your level in Farming, Fishing, Mining, Animals and Combat",
                color= 0x7F4E4E,
                timestamp= datetime.utcnow()
            )
            embed.add_field(name="\n", value="\n", inline=False)
            # Create a string for the embed
            the_str = ""
            # add all the data to the string
            the_str = the_str + f"Health - {await make_bar(users[str(ctx.author.id)]['Stats']['Health'], users[str(ctx.author.id)]['Stats']['MaxHealth'], '🟥', '⬛')}\n"
            the_str = the_str + f"Energy - {await make_bar(users[str(ctx.author.id)]['Stats']['Energy'], users[str(ctx.author.id)]['Stats']['MaxEnergy'], '🟩', '⬛')}\n"
            the_str = the_str + "\n"
            the_str = the_str + f"Farming - {await make_bar(users[str(ctx.author.id)]['Stats']['Farming'], 10, '🟨', '⬛')}\n"
            the_str = the_str + f"Fishing - {await make_bar(users[str(ctx.author.id)]['Stats']['Fishing'], 10, '🟨', '⬛')}\n"
            the_str = the_str + f"Mining - {await make_bar(users[str(ctx.author.id)]['Stats']['Mining'], 10, '🟨', '⬛')}\n"
            the_str = the_str + f"Animals - {await make_bar(users[str(ctx.author.id)]['Stats']['Animals'], 10, '🟨', '⬛')}\n"
            the_str = the_str + f"Combat - {await make_bar(users[str(ctx.author.id)]['Stats']['Combat'], 10, '🟨', '⬛')}\n" 
            # add the field 
            embed.add_field(name="\n", value=the_str, inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.global_name}", icon_url=ctx.author.display_avatar)
            # Send the embed
            await ctx.reply(embed=embed)
        else:
            # If not, send an alert indicating that
            await ctx.reply("You have to start first! Use `x start`")   


class Economy(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(aliases=["bal"])
    async def balance(self, ctx, user: discord.Member = None):
        # If the user didn't specify the user
        if user == None:
            # Then the user must be wanting to view their balance, so the user is the ctx.author 
            user = ctx.author
        
        # Create the embed
        embed = discord.Embed(
            title=f"{user.global_name}'s Balance",
            description="This is your balance! To deposit money from your wallet to bank use `x deposit [amount]` and use `x withdraw [amount]` to withdraw money from your bank to wallet",
            color=0x7F4E4E,
            timestamp= datetime.utcnow()
        )

    
        # Get the inventory data as users
        users = await get_inventory_data()
        
        embed.add_field(name="Wallet 👜", value=f'💵 {int(users[str(user.id)]["Money"]["Wallet"]):,}', inline= True)
        embed.add_field(name="Bank 💳", value=f'💵 {int(users[str(user.id)]["Money"]["Bank"]):,}', inline= True)
        embed.set_footer(text=f"Requested by {ctx.author.global_name}", icon_url=ctx.author.display_avatar)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.command()
    async def deposit(self, ctx, amount: int):    
        # Get the inventory data as users
        users = await get_inventory_data()

        # Check if the user has that much money in their wallet
        if int(users[str(ctx.author.id)]["Money"]["Wallet"]) >= amount:
            # Then subtract the amount from the wallet 
            await update_money(ctx.author, -1*amount, "Wallet")
            # Then add the amount to the bank
            await update_money(ctx.author, amount, "Bank")
            # Send the response
            await ctx.reply(f"Successfully deposited 💵 {amount} to Bank")
        else:
            # Send the response
            await ctx.reply("You don't have that much money!")

    @commands.command()
    async def withdraw(self, ctx, amount: int):    
        # Get the inventory data as users
        users = await get_inventory_data()

        # Check if the user has that much money in their bank
        if int(users[str(ctx.author.id)]["Money"]["Bank"]) >= amount:
            # Then subtract the amount from the bank
            await update_money(ctx.author, -1*amount, "Bank")
            # Then add the amount to the wallet
            await update_money(ctx.author, amount, "Wallet")
            # Send the response
            await ctx.reply(f"Successfully withdrawed 💵 {amount} from Bank")
        else:
            # Send the response
            await ctx.reply("You don't have that much money!")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Inventory(client))
    await client.add_cog(Economy(client))