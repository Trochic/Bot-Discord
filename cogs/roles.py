import discord
from discord.ext import commands
import csv
import requests
import shutil
import time
import os
from PIL import Image
import numpy as np
"""from spellchecker import SpellChecker"""
import unidecode
import random


class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def manage_reactions(self, reaction, guild, messageid, user, added: bool):
        
        with open("./cogs/roles.csv", "r") as rolestxt:
            rolestxtr = csv.DictReader(rolestxt)
            for row in rolestxtr:
                if int(messageid) == int(row["idmessage"]):
                    messageID = int(messageid)
                    if reaction == "✅":
                        member = discord.utils.get(guild.members, id=user.id)
                        role = discord.utils.get(guild.roles, id=int(row["idrole"]))
                        if added:       
                            await member.add_roles(role)
                        else:
                            await member.remove_roles(role)
                    else:
                        print("Non")


    @commands.Cog.listener()
    async def on_message(self, message):
        chanel = 788559533005209620
        if message.channel.id == chanel:
            await message.add_reaction("✅")
        """
        if message.author.id != 776084233512681502:
            spell = SpellChecker()
            spell.word_frequency.load_words(["raciste","bordel","billard","s'arreter", "saoule", "arreter","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
            gofurkei = unidecode.unidecode(message.content).split()
            misspelled = spell.unknown(gofurkei)
            monsieur = ""
            for word in misspelled:
                await message.channel.send(f'{word} :sunglasses:')
        """
        
        """if message.attachments:
            lien = message.attachments[0].url
            nomfic = lien.split("/")[-1]
            req = requests.get(lien, stream=True)

            if req.status_code == 200:

                req.raw.decode_content = True

                with open(f'./img/{nomfic}', "wb") as imag:
                    shutil.copyfileobj(req.raw, imag)

                imagre = Image.open(f"./img/{nomfic}")
                screen = Image.open("./randomimage.png")

                iar = np.asarray(imagre)
                noscreen = np.asarray(screen)
                if np.allclose(noscreen, iar):
                    print("yessay")
                    await message.delete()
        """
        
    @commands.command()
    async def guildd(self, ctx):
        for roles in ctx.guild.roles:
            print(roles.id)
    
    @commands.command()
    async def intialize(self, ctx):
        if ctx.author.id == 132918827594809344:
            channel = ctx.channel
            async for message in channel.history(limit=100):
                await message.add_reaction("✅")

    @commands.command()
    async def separators(self, ctx):
        if ctx.author.id == 132918827594809344:
            for member in ctx.guild.members:
                role = discord.utils.get(ctx.guild.roles, id=789950997521760256)
                role1 = discord.utils.get(ctx.guild.roles, id=785821683477905408)
                role2 = discord.utils.get(ctx.guild.roles, id=789949834538385448)
                role3 = discord.utils.get(ctx.guild.roles, id=785821819092729889)
                await member.add_roles(role)
                await member.add_roles(role1)
                await member.add_roles(role2)
                await member.add_roles(role3)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, id=789950997521760256)
        role1 = discord.utils.get(member.guild.roles, id=785821683477905408)
        role2 = discord.utils.get(member.guild.roles, id=789949834538385448)
        role3 = discord.utils.get(member.guild.roles, id=785821819092729889)
        await member.add_roles(role)
        await member.add_roles(role1)
        await member.add_roles(role2)
        await member.add_roles(role3)
    
    
    @commands.command()
    async def addrole(self, ctx, idmess, idrol):
        modos = ["655121505935556611", "176021766240468992", "132918827594809344", "267339295264604170","295192769012695050","225651853210288129"]
        if str(ctx.author.id) in modos:
            with open("./cogs/roles.csv", "a") as rolestxt:
                newrow = csv.writer(rolestxt, delimiter=',')
                newrow.writerow([f'{idmess}', f'{idrol}'])

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        messageid = payload.message_id
        reaction = str(payload.emoji)
        guild = self.client.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)
        await self.manage_reactions(reaction, guild,  messageid, user, True)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        messageid = payload.message_id
        reaction = str(payload.emoji)
        guild = self.client.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)
        await self.manage_reactions(reaction, guild,  messageid, user, False)

def setup(client):
    client.add_cog(Roles(client))
