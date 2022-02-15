import discord
from discord.ext import commands
import requests
import shutil
import time
import os
from PIL import Image

class ImageProcessing(commands.Cog):
    def __init__(self, client):
        self.client = client    

    @commands.command()
    async def wide(self, ctx):
        chan = ctx.channel
        async for message in chan.history(limit=10):
            if message.attachments:
                lien = message.attachments[0].url
                nomfic = lien.split("/")[-1]
                req = requests.get(lien, stream=True)

                if req.status_code == 200:

                    req.raw.decode_content = True

                    with open(f'./img/{nomfic}', "wb") as imag:
                        shutil.copyfileobj(req.raw, imag)

                    imagre = Image.open(f"./img/{nomfic}")
                    if imagre.width <= 4000 and imagre.height <= 4000:
                        hei = imagre.height
                        wid = imagre.width * 2.5
                    else:
                        await ctx.send("*Pas un fichier aussi grand petit chenapan UwU*")
                        hei = imagre.height
                        wid = imagre.width / 2.5
                    wideimg = imagre.resize((int(wid), hei))
                    wideimg.save(f"./img/wide{nomfic}")
                    with open(f'./img/wide{nomfic}', 'rb') as widen:
                        await ctx.send(file=discord.File(widen, f'{nomfic}'))
                for files in os.listdir("./img"):
                    os.remove(f'./img/{files}')
                return
        await ctx.send("*J'ai pas trouvé d'image dans les 10 derniers posts désolé UwU*")

    @commands.command()
    async def high(self, ctx):
        chan = ctx.channel
        async for message in chan.history(limit=10):
            if message.attachments:
                lien = message.attachments[0].url
                nomfic = lien.split("/")[-1]
                if nomfic[:-4] == '.mp4':
                    await ctx.send("*C'est une vidéo UwU*")
                    return
                req = requests.get(lien, stream=True)

                if req.status_code == 200:

                    req.raw.decode_content = True

                    with open(f'./img/{nomfic}', "wb") as imag:
                        shutil.copyfileobj(req.raw, imag)

                    imagre = Image.open(f"./img/{nomfic}")
                    if imagre.width <= 4000 and imagre.height <= 4000:
                        hei = imagre.height * 2.5
                        wid = imagre.width
                    else:
                        await ctx.send("*Pas un fichier aussi grand petit chenapan UwU*")
                        hei = imagre.height / 2.5
                        wid = imagre.width
                    heiimg = imagre.resize((int(wid), int(hei)))
                    heiimg.save(f"./img/wide{nomfic}")
                    with open(f'./img/wide{nomfic}', 'rb') as widen:
                        await ctx.send(file=discord.File(widen, f'{nomfic}'))

                    for files in os.listdir("./img"):
                        os.remove(f'./img/{files}')
                    return
        await ctx.send("*J'ai pas trouvé d'image dans les 10 derniers posts désolé UwU*")

    @commands.command()
    async def unhigh(self, ctx):
        chan = ctx.channel
        async for message in chan.history(limit=10):
            if message.attachments:
                lien = message.attachments[0].url
                nomfic = lien.split("/")[-1]
                if nomfic[:-4] == '.mp4':
                    await ctx.send("*C'est une vidéo UwU*")
                    return
                req = requests.get(lien, stream=True)

                if req.status_code == 200:

                    req.raw.decode_content = True

                    with open(f'./img/{nomfic}', "wb") as imag:
                        shutil.copyfileobj(req.raw, imag)

                    imagre = Image.open(f"./img/{nomfic}")
                    hei = imagre.height / 2.5
                    wid = imagre.width
                    heiimg = imagre.resize((int(wid), int(hei)))
                    heiimg.save(f"./img/wide{nomfic}")
                    with open(f'./img/wide{nomfic}', 'rb') as widen:
                        await ctx.send(file=discord.File(widen, f'{nomfic}'))
                    for files in os.listdir("./img"):
                        os.remove(f'./img/{files}')
                    return        
        await ctx.send("*J'ai pas trouvé d'image dans les 10 derniers posts désolé UwU*")

    @commands.command()
    async def unwide(self, ctx):
        chan = ctx.channel
        async for message in chan.history(limit=10):
            if message.attachments:
                lien = message.attachments[0].url
                nomfic = lien.split("/")[-1]
                req = requests.get(lien, stream=True)

                if req.status_code == 200:

                    req.raw.decode_content = True

                    with open(f'./img/{nomfic}', "wb") as imag:
                        shutil.copyfileobj(req.raw, imag)

                    imagre = Image.open(f"./img/{nomfic}")
                    hei = imagre.height
                    wid = imagre.width / 2.5
                    wideimg = imagre.resize((int(wid), hei))
                    wideimg.save(f"./img/wide{nomfic}")
                    with open(f'./img/wide{nomfic}', 'rb') as widen:
                        await ctx.send(file=discord.File(widen, f'{nomfic}'))
                for files in os.listdir("./img"):
                    os.remove(f'./img/{files}')
                return
        await ctx.send("*J'ai pas trouvé d'image dans les 10 derniers posts désolé UwU*")
    
    @commands.command()
    async def rotate(self,ctx, nbr):
        nbr = int(nbr)
        chan = ctx.channel
        async for message in chan.history(limit=40):
            if message.attachments:
                lien = message.attachments[0].url
                nomfic = lien.split("/")[-1]
                req = requests.get(lien, stream=True)
                if req.status_code == 200:
                    req.raw.decode_content = True
                    with open(f'./img/{nomfic}', "wb") as imag:
                        shutil.copyfileobj(req.raw, imag)
                    image = Image.open(f"./img/{nomfic}")
                    rotated  = image.rotate(nbr, expand=True)
                    rotated.save(f"./img/rot{nomfic}")
                    with open(f'./img/rot{nomfic}', 'rb') as widen:
                        await ctx.send(file=discord.File(widen, f'{nomfic}'))
                        for files in os.listdir("./img"):
                            os.remove(f'./img/{files}')
                        return
    


    @wide.error
    async def wide_error(self, ctx, error): 
        await ctx.send("*J'ai bugué OwO*")

    @high.error
    async def high_error(self, ctx, error): 
        await ctx.send("*J'ai bugué OwO*")

    @unhigh.error
    async def unhigh_error(self, ctx, error): 
        await ctx.send("*J'ai bugué OwO*")
    
    @unwide.error
    async def high_error(self, ctx, error): 
        await ctx.send("*J'ai bugué OwO*")

def setup(client):
    client.add_cog(ImageProcessing(client))