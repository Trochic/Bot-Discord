import discord
from discord.ext import commands
import random
import os

class Dubois(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dubois(self, ctx, *, nom):
        rep = [
                """Bonjour {nome}, tu peux partager ton écran s\'il te plait ?""",
                """Bonjour {nome}, je peux voir ton écran s\'il te plait ?""",
                """Alors {nome}, il en est où ce partage d\'écran ?""",
                """{nome} ton écran s\'il te plait""",
                """Bah alors {nome}, tu veux pas partager ton écran c'est ça""",
                """{nome}, il arrive ce partage d\'écran ?""",
                """Bon {nome} tu te dépêches s\'il te plait ?"""
                ]
        files = [
            "./dubois/cursed1.png",
            "./dubois/dubois-kun.jpg",
            "./dubois/duboisfast.png",
            "./dubois/jcd.jpg",
            "./dubois/Ton_ecran.png"
        ]
        reps = random.choice(rep).format(nome=f'{nom}')
        filrand = random.choice(files)
        await ctx.send(f'{reps}')
        with open(f'{filrand}', 'rb') as fp:
            await ctx.send(file=discord.File(fp, 'jcd.jpg'))

    


def setup(client):
    client.add_cog(Dubois(client))