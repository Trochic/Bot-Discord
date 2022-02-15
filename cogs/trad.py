import discord
from discord.ext import commands
import random
"""from googletrans import Translator"""

class Traduction(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    @commands.command(aliases=['8ball', 'test'])
    async def _8ball(self, ctx, *, question):
        translt = Translator()
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        res = random.choice(responses)
        await ctx.send(f'Question: {question} \n Answer: {res}')

"""    @commands.command(aliases=['tard', 'trans', 'translate', 'tra', 'traduct', 'traduction',])
    async def trad(self, ctx, *, message):
        translt = Translator()
        traduct = translt.translate(f'{message}', dest='fr')
        trs = traduct.text
        await ctx.send(trs)

    @commands.command()
    async def tradto(self, ctx, lang, *, message):
        translt = Translator()
        traducto = translt.translate(f'{message}', dest=f'{lang}')
        tro = traducto.text
        await ctx.send(tro)
"""



def setup(client):
    client.add_cog(Traduction(client))