#!/usr/bin/python3
import discord
import random
import giphy_client
import os
from dotenv import load_dotenv
from discord.ext import commands
from giphy_client.rest import ApiException
giphy_token = os.getenv('GIPHY_TOKEN')

api_instance = giphy_client.DefaultApi()
config = {
    'api_key': giphy_token,
    'limit': 5,
    'rating': "r"
}


class Giphy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def giphy(self, ctx, *, query):
        try:
            response = api_instance.gifs_search_get(
                giphy_token, query, limit=5, rating='r')
            lst = list(response.data)
            gif = random.choices(lst)
            await ctx.send(gif[0].url)

        except ApiException as e:
            return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e


def setup(client):
    client.add_cog(Giphy(client))
