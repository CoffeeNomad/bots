import discord
from discord.ext import commands


class Startup(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    # commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(Startup(client))
