from discord.ext import commands
from datetime import timedelta


class HelpCog(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"Pong! {round(self.client.latency)}")

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