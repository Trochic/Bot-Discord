import discord
from discord.ext import commands
import csv
import sqlite3

class Testing(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def testing(self, ctx):
        if str(ctx.author.id) == "132918827594809344":
            with open("./rolessub.csv", "r") as rolessub:
                rolessubr = csv.DictReader(rolessub)
                for roles in rolessubr:
                    rolee = discord.utils.get(ctx.guild.roles, id=int((roles["idrole"]))).name
                    print(rolee)

    @commands.command()
    async def aaa(self, ctx):
        if str(ctx.author.id) == "132918827594809344":
            for roles in ctx.guild.roles:
                print(roles.id)

       
    @commands.command()
    async def paow(self, ctx):
        if str(ctx.author.id) == "132918827594809344":
            liste_roles_nouveau = []
            liste_roles_guilde = ctx.guild.roles
            with open("./cogs/roles.csv", "r") as rolestxt:
                rolestxtr = csv.DictReader(rolestxt)
                for roles_mouloud in rolestxtr:
                    for roles in liste_roles_guilde:
                        if str(roles_mouloud["idrole"]) == str(roles.id):
                            liste_roles_nouveau.append(str(roles.id))

            rolestxt.close()

            with open("./cogs/roles.csv", "r") as rolestxt:
                rolestxtr = csv.DictReader(rolestxt)
                with open("./rolessub.csv","w") as rolesnouveau:
                    newrow = csv.writer(rolesnouveau, delimiter=',')

                    for ancien_roles in rolestxtr:
                        for newrole in liste_roles_nouveau:
                            if str(ancien_roles["idrole"]) == str(newrole):
                                newrow.writerow([f'{ancien_roles["idmessage"]}',f'{ancien_roles["idrole"]}']) 

"""
    @commands.command()
    async def hop(self, ctx):
        if str(ctx.author.id) == "132918827594809344":
            with open("./roles.csv", "r") as rolestxt:
                rolestxtr = csv.Dictreader(rolestxt)
                with open("./rolessub.csv","w"): rolesnouveau:
                    newrow = csv.writer(rolesnouveau, delimiter=',')

                    for ancien_roles in rolestxtr:
                        for newrole in liste_roles_nouveau:
                        if str(ancien_roles["idrole"]) == str(newrole):
                            newrow.writerow([f'{ancien_roles["idmessage"]}',f'{ancien_roles["idrole"]}'])
"""
                    


def setup(client):
    client.add_cog(Testing(client))