import discord
from discord import app_commands
from discord.ext import commands
from fun_config import *
from datetime import datetime


class Inventory(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client
    
    @app_commands.command(name="stats", description="Shows the stats of the user")
    async def stats(self, interaction: discord.Interaction) -> None:
        # Get the data as users
        users = await get_inventory_data()
        # Check if the user has already started
        if str(interaction.user.id) in users:
            # If so, create the user's stats embed
            embed = discord.Embed(
                title=f"{interaction.user.global_name}'s Stats",
                description="Here you can view your Health, Energy and your level in Farming, Fishing, Mining, Animals and Combat",
                color= 0x7F4E4E,
                timestamp= datetime.utcnow()
            )
            embed.add_field(name="\n", value="\n", inline=False)
            # Create a string for the embed
            the_str = ""
            # add all the data to the string
            the_str = the_str + f"Health - {await make_bar(users[str(interaction.user.id)]['Stats']['Health'], users[str(interaction.user.id)]['Stats']['MaxHealth'], '🟥', '⬛')}\n"
            the_str = the_str + f"Energy - {await make_bar(users[str(interaction.user.id)]['Stats']['Energy'], users[str(interaction.user.id)]['Stats']['MaxEnergy'], '🟩', '⬛')}\n"
            the_str = the_str + "\n"
            the_str = the_str + f"Farming - {await make_bar(users[str(interaction.user.id)]['Stats']['Farming'], 10, '🟨', '⬛')}\n"
            the_str = the_str + f"Fishing - {await make_bar(users[str(interaction.user.id)]['Stats']['Fishing'], 10, '🟨', '⬛')}\n"
            the_str = the_str + f"Mining - {await make_bar(users[str(interaction.user.id)]['Stats']['Mining'], 10, '🟨', '⬛')}\n"
            the_str = the_str + f"Animals - {await make_bar(users[str(interaction.user.id)]['Stats']['Animals'], 10, '🟨', '⬛')}\n"
            the_str = the_str + f"Combat - {await make_bar(users[str(interaction.user.id)]['Stats']['Combat'], 10, '🟨', '⬛')}\n" 
            # add the field 
            embed.add_field(name="\n", value=the_str, inline=False)
            embed.set_footer(text=f"Requested by {interaction.user.global_name}", icon_url=interaction.user.display_avatar)
            # Send the embed
            await interaction.response.send_message(embed=embed)
        else:
            # If not, send an alert indicating that
            await interaction.response.send_message("You have to start first! Use `x start`")   


class Economy(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="balance", description="Shows the balance of the user")
    async def balance(self, interaction: discord.Interaction, user: discord.Member = None) -> None:
        if user is None:
            user = interaction.user
        
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
        embed.set_footer(text=f"Requested by {interaction.user.global_name}", icon_url=interaction.user.display_avatar)

        # Send the embed
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="deposit", description="Deposit the money from the wallet to bank")
    async def deposit(self, interaction: discord.Interaction, amount: int):    
        # Get the inventory data as users
        users = await get_inventory_data()

        # Check if the user has that much money in their wallet
        if int(users[str(interaction.user.id)]["Money"]["Wallet"]) >= amount:
            # Then subtract the amount from the wallet 
            await update_money(interaction.user, -1*amount, "Wallet")
            # Then add the amount to the bank
            await update_money(interaction.user, amount, "Bank")
            # Send the response
            await interaction.response.send_message(f"Successfully deposited 💵 {amount} to Bank")
        else:
            # Send the response
            await interaction.response.send_message("You don't have that much money!")

    @app_commands.command(name="withdraw", description="Withdraw the money from the bank to wallet")
    async def withdraw(self, interaction: discord.Interaction, amount: int):    
        # Get the inventory data as users
        users = await get_inventory_data()

        # Check if the user has that much money in their bank
        if int(users[str(interaction.user.id)]["Money"]["Bank"]) >= amount:
            # Then subtract the amount from the bank
            await update_money(interaction.user, -1*amount, "Bank")
            # Then add the amount to the wallet
            await update_money(interaction.user, amount, "Wallet")
            # Send the response
            await interaction.response.send_message(f"Successfully withdrawed 💵 {amount} from Bank")
        else: 
            # Send the response
            await interaction.response.send_message("You don't have that much money!")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Inventory(client))
    await client.add_cog(Economy(client))