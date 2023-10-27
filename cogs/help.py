from discord.ext import commands


class HelpCog(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"Pong! {round(self.client.latency)}")
    
async def setup(client: commands.Bot) -> None:
    await client.add_cog(HelpCog(client))