import discord
from discord.ext import commands
import random
"""from googletrans import Translator"""

class Poopy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def giveup(self, ctx):
        with open('./giveupping.mp4', 'rb') as fp:
            await ctx.send(file=discord.File(fp, 'giveup.mp4'))

    @commands.command(aliases = ["anniv"])
    async def anniversaire(self, ctx):
        rand = [1,2]
        files = [
                "./anniversaire.jpg",
                "./anniversaire1.jpg"]
        reps = random.choice(rand)
        if reps == 1:
            with open('./images/anniversaire.jpg', 'rb') as fp:
                await ctx.send(file=discord.File(fp, 'anniversaire.jpg'))
        else:
            with open('./images/anniversaire1.jpg', 'rb') as fp:
                await ctx.send(file=discord.File(fp, 'anniversaire.jpg'))

    @commands.command()
    async def denis(self, ctx):
        for i in range(5):
            await ctx.send("D E N I S P R E S I D E N T  A N T I K Y T H E R A La politique anti-blanche A N T I K Y T H E R A")

    @commands.command(aliases = ["zemour", "zem", "zamour"])
    async def zemmour(self, ctx):
        await ctx.send(" Il est bien ce Zemmour finalement, enfin quelqu'un pour claquer le beignet de l'auteur du \"Barrez-vous\" ! #zenpp #barrezvous")
    
    @commands.command()
    async def spam(self, ctx, *, pseudal):
        for _ in range(5):
            await ctx.send(f'{pseudal}')

    @commands.command()
    async def nick(self, ctx, user, nickname): 
        if ctx.author.id == 132918827594809344:
            print(user)
            member = discord.utils.get(ctx.guild.members, id=user.id)
            await member.edit(nick=nickname)


def setup(client):
    client.add_cog(Poopy(client))