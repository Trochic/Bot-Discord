import discord
from discord.ext import commands

class ClearMouloud(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clm(self, ctx, nbr):
        chann = ctx.channel
        async for message in chann.history(limit=int(nbr)):
            if message.author.id == 776084233512681502:
                await message.delete()

    @commands.command()
    async def clearchat(self, ctx, nbr):
        chann = ctx.channel
        if ctx.author.id == 132918827594809344 or ctx.author.id == 176021766240468992:
            async for message in chann.history(limit=int(nbr)):
                await message.delete()
        else:
            await ctx.send("Pas les perms bg contacte trochic ou skew si vraiment needed")

    @commands.command()
    async def fetch(self, ctx):
        user = self.client.get_user(ctx.author.id)
        print(role = discord.utils.get(user.guild.roles, id=789950997521760256))

def setup(client):
    client.add_cog(ClearMouloud(client))