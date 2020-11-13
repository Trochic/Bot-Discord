import discord
from discord.ext import commands
import random
from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

client = commands.Bot(command_prefix = '.')
translt = Translator()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def Ping(ctx):
    await ctx.send(f'Pong {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
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
    await ctx.send(f'Question: {question} \n Answer: {random.choice(responses)}')

@client.command()
async def trad(ctx, *, message):
    traduct = translt.translate(f'{message}', dest='fr')
    await ctx.send({traduct.text})

@client.command()
async def edth(ctx):
    boite=discord.Embed(title=".edt GROUPE JOURNEE", color=0x3224ff)
    boite.add_field(name="GROUPE : ", value="F1 - F2 / G1 - G2 / H1 - H2 / I1 - I2 / J1 - J2", inline=False)
    boite.add_field(name="JOURNEE", value="lundi - mardi - mercredi - jeudi - vendredi", inline=False)
    await ctx.send(embed=boite)

@client.command()
async def edt(ctx, groupe, jour):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1400,1500")

    driver = webdriver.Chrome(options=options)
    driver.get("https://planning.univ-rennes1.fr/direct/myplanning.jsp")

    searchUser = driver.find_element_by_id("username")
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
    try:
        linktest = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.ID, "Direct Planning Tree_2117"))
        )
    except:
        driver.quit()

    time.sleep(1)

    if(groupe == 'F1' or groupe == 'f1'):
        link = driver.find_element_by_id("Direct Planning Tree_3475")
    elif(groupe == 'F2' or groupe == 'f2'):
        link = driver.find_element_by_id("Direct Planning Tree_3476")
    elif(groupe == 'G1' or groupe == 'g1'):
        link = driver.find_element_by_id("Direct Planning Tree_3471")
    elif(groupe == 'G2' or groupe == 'g2'):
        link = driver.find_element_by_id("Direct Planning Tree_3473")
    elif(groupe == 'H1' or groupe == 'h1'):
        link = driver.find_element_by_id("Direct Planning Tree_3465")
    elif(groupe == 'H2' or groupe == 'h2'):
        link = driver.find_element_by_id("Direct Planning Tree_3466")
    elif(groupe == 'I1' or groupe == 'i1'):
        link = driver.find_element_by_id("Direct Planning Tree_3462")
    elif(groupe == 'I2' or groupe == 'i2'):
        link = driver.find_element_by_id("Direct Planning Tree_3463")
    elif(groupe == 'J1' or groupe == 'j1'):
        link = driver.find_element_by_id("Direct Planning Tree_3459")
    elif(groupe == 'J2' or groupe == 'j2'):
        link = driver.find_element_by_id("Direct Planning Tree_2117")
    else:
        print("Erreur groupe")
        await ctx.send("Erreur groupe")
        driver.quit()
        return

    link.click()

    time.sleep(1)
    if(jour == 'lundi' or jour == 'Lundi'):
        linkjour = driver.find_element_by_id("x-auto-143")
    elif(jour == 'mardi' or jour == 'Mardi'):
        linkjour = driver.find_element_by_id("x-auto-144")
    elif(jour == 'mercredi' or jour == 'Mercredi'):
        linkjour = driver.find_element_by_id("x-auto-145")
    elif(jour == 'jeudi' or jour == 'Jeudi'):
        linkjour = driver.find_element_by_id("x-auto-146")
    elif(jour == 'vendredi' or jour == 'Vendredi'):
        linkjour = driver.find_element_by_id("x-auto-147")
    else:
        print("Erreur jour")
        await ctx.send("Erreur jour")
        driver.quit()
        return

    linkjour.click()
    time.sleep(1)

    planning = driver.find_element_by_id("Planning")

    val = 0
    divinc = "div"
    princ = "\n"
    for val in range(10):
        time.sleep(0.25)
        heurecours = planning.find_elements_by_id(divinc + str(val))
        for content in heurecours:
            cours = content.find_element_by_class_name("eventText")
            princ += "\n----------------------\n"
            princ += cours.text
    
    emploid = discord.Embed(title=f"Emploi du temps {groupe}, Journée : {jour}", color=0x3224ff)
    emploid.add_field(name="--------------------------------------------", value=f"{princ}", inline="False")
    await ctx.send(embed=emploid)

    driver.quit()


client.run('Nzc2MDg0MjMzNTEyNjgxNTAy.X6vuxA.GTqXPHrSLltlZO5JArwoJh_lkrs')
