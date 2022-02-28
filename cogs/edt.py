import discord
from discord.ext import commands
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests
import datetime
import asyncio
from asyncio import sleep
from discord.ext import tasks
from discord.ext.tasks import loop
from discord.ext.commands import Bot
import csv

class EmploiDuTemps(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def edth(self, ctx):
        boite=discord.Embed(title=".edt <groupe> <journee>", color=0x3224ff)
        boite.add_field(name="GROUPE : ", value="F1 - F2 / G1 - G2 / H1 - H2 / I1 - I2 / J1 - J2", inline=False)
        boite.add_field(name="JOURNEE", value="lundi - mardi - mercredi - jeudi - vendredi", inline=False)
        await ctx.send(embed=boite)

    @commands.command()
    async def edt(self, ctx, groupe, jour):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("window-size=1400,1500")
        print("bonj")

        driver = webdriver.Chrome(options=options)
        driver.get("https://planning.univ-rennes1.fr/direct/myplanning.jsp")
        try:
            searchUser = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "username"))
                )
        except:
            driver.quit()
            await ctx.send("Site down")
            print("Site down")
            returns

        searchUser.send_keys("ppannetier")
        searchPass = driver.find_element_by_id("password")
        searchPass.send_keys("cestCHIANT123")
        searchPass.send_keys(Keys.RETURN)

        try:
            planning = WebDriverWait(driver, 6).until(
                EC.presence_of_element_located((By.ID, "Planning"))
            )
        except:
            driver.quit()
            await ctx.send("Erreur chargement de page, site surement down")
            print("Charge pas le planning")
            returns
        
        time.sleep(2)
        print("cry")

        if(groupe == 'A1' or groupe == 'a1'):
            link = driver.find_element_by_id("Direct Planning Tree_3484")
        elif(groupe == 'A2' or groupe == 'a2'):
            link = driver.find_element_by_id("Direct Planning Tree_3485")
        elif(groupe == 'B1' or groupe == 'b1'):
            link = driver.find_element_by_id("Direct Planning Tree_3481")
        elif(groupe == 'B2' or groupe == 'b2'):
            link = driver.find_element_by_id("Direct Planning Tree_3482")
        elif(groupe == 'C1' or groupe == 'c1'):
            link = driver.find_element_by_id("Direct Planning Tree_3478")
        elif(groupe == 'C2' or groupe == 'c2'):
            link = driver.find_element_by_id("Direct Planning Tree_3479")
        elif(groupe == 'D1' or groupe == 'd1'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-350").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_3430")
        elif(groupe == 'D2' or groupe == 'd2'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-350").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_2275")
        elif(groupe == 'F1' or groupe == 'f1'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-335").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            driver.find_element_by_id("Direct Planning Tree_x-auto-371").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_3475")
        elif(groupe == 'F2' or groupe == 'f2'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-335").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            driver.find_element_by_id("Direct Planning Tree_x-auto-371").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_3476")
        elif(groupe == 'G1' or groupe == 'g1'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-335").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            driver.find_element_by_id("Direct Planning Tree_x-auto-374").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_3471")
        elif(groupe == 'G2' or groupe == 'g2'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-335").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            driver.find_element_by_id("Direct Planning Tree_x-auto-374").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_3473")
        elif(groupe == 'H1' or groupe == 'h1'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-335").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            driver.find_element_by_id("Direct Planning Tree_x-auto-377").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_3465")
        elif(groupe == 'H2' or groupe == 'h2'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-335").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            driver.find_element_by_id("Direct Planning Tree_x-auto-377").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_3466")
        elif(groupe == 'I1' or groupe == 'i1'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-335").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            driver.find_element_by_id("Direct Planning Tree_x-auto-380").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_3462")
        elif(groupe == 'I2' or groupe == 'i2'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-335").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            driver.find_element_by_id("Direct Planning Tree_x-auto-380").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_3463")
        elif(groupe == 'J1' or groupe == 'j1'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-335").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            driver.find_element_by_id("Direct Planning Tree_x-auto-383").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_3459")
        elif(groupe == 'J2' or groupe == 'j2'):
            driver.find_element_by_id("Direct Planning Tree_x-auto-335").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            driver.find_element_by_id("Direct Planning Tree_x-auto-383").find_element_by_class_name("x-tree3-node-joint").click()
            time.sleep(0.6)
            link = driver.find_element_by_id("Direct Planning Tree_2117")
        else:
            print("Erreur groupe")
            await ctx.send("Erreur groupe")
            driver.quit()
            return

        link.click()
        time.sleep(1.2)
        print("yo")
        driver.find_element_by_id("x-auto-188").click()
        time.sleep(1.5)
        print("yo2")

        if(jour.lower()[:1] == 'l'):
            linkjour = driver.find_element_by_id("x-auto-143")
        elif(jour.lower()[:2] == 'ma'):
            linkjour = driver.find_element_by_id("x-auto-144")
        elif(jour.lower()[:2] == 'me'):
            linkjour = driver.find_element_by_id("x-auto-145")
        elif(jour.lower()[:1] == 'j'):
            linkjour = driver.find_element_by_id("x-auto-146")
        elif(jour.lower()[:1] == 'v'):
            linkjour = driver.find_element_by_id("x-auto-147")
        else:
            print("Erreur jour")
            await ctx.send("Erreur jour")
            driver.quit()
            return

        linkjour.click()
        time.sleep(1.3)

        planning = driver.find_element_by_id("Planning")
        val = 0
        divinc = "div"
        princ = "\n"
        emploid = discord.Embed(title=f"Emploi du temps {groupe}, Journée : {jour}", color=0x3224ff)
        for val in range(10):
            time.sleep(0.1)
            heurecours = planning.find_elements_by_id(divinc + str(val))
            for content in heurecours: 
                cours = content.find_element_by_class_name("eventText")
                princ = cours.text
                emploid.add_field(name="----------------------", value=f"{princ}", inline="True")

        await ctx.send(embed=emploid)

        driver.quit()

    @edt.error
    async def edt_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Il manque un paramètre, faire .edth pour la syntaxe")

    
def setup(client):
    client.add_cog(EmploiDuTemps(client))
