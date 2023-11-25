import discord
from discord import app_commands
from discord.ext import commands
from datetime import timedelta
from typing import Literal, Optional

class HelpCog(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
        if not guilds:
            if spec == "~":
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "*":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "^":
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
                synced = []
            else:
                synced = await ctx.bot.tree.sync()

            await ctx.send(
                f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
            )
            return

        ret = 0
        for guild in guilds:
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException:
                pass
            else:
                ret += 1

        await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

    
    @app_commands.command(name="help", description="Sends the details of all commands and categories")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message("The command is under development!", ephemeral=True)


    @app_commands.command(name="ping", description="Sends the latency of the bot!")
    async def ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Pong! {round(self.client.latency)}ms", ephemeral=True)

    @commands.Cog.listener()
    async def on_command_error(self, message, error):
        if isinstance(error, commands.MissingPermissions):
            await message.send("I don't have enough permissions to execute that command!")
        elif isinstance(error, commands.CommandNotFound):
            await message.send("No such command")
        elif isinstance(error, commands.CommandOnCooldown):
            seconds = round(error.retry_after)
            time_delta = timedelta(seconds=seconds)
            time_str = str(time_delta)
            if time_str.startswith("0:"): 
                time_str = time_str[2:]
            await message.send(f"Command on cooldown! Please try after {time_str}")
        else:
            await message.send("Unexpected error occurred, Please try again later!")
            raise error


async def setup(client: commands.Bot) -> None:
    await client.add_cog(HelpCog(client))