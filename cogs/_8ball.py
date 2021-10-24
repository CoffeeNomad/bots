import discord
import random
from discord.ext import commands


class EightBall(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     "Don’t count on it.",
                     'Yes, but do it drunk as FUCK.',
                     'My sources say no, but they also said Hillary would win.',
                     'R U Crazy?',
                     "Don't be Stupid.",
                     'Im code, not a miracle worker.',
                     "You're adopted.",
                     'Leave me alone.',
                     'Beat it, kid.',
                     'DRINK!',
                     'You, Fuck Off.', ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


def setup(client):
    client.add_cog(EightBall(client))
