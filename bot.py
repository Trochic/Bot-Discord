import discord
from discord.ext import commands
import random
from googletrans import Translator
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

intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = commands.Bot(command_prefix = '.', intents=intents)
translt = Translator()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}.py')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}.py')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

"""@tasks.loop(seconds=310)
async def prixcrypto():
        channel = client.get_channel(776053500059975690)
        databtc = requests.get('https://api.binance.com/api/v1/ticker/24hr?symbol=BTCUSDT')
        jdata = databtc.json()
        datavet = requests.get('https://api.binance.com/api/v1/ticker/24hr?symbol=ETHUSDT').json()
        dataxrp = requests.get('https://api.binance.com/api/v1/ticker/24hr?symbol=DOTUSDT').json()
        phrase = (f'{jdata["symbol"]} : {format(float(jdata["bidPrice"]),".2f")}$ / 24H : {jdata["priceChangePercent"]}% / 24H : {format(float(jdata["priceChange"]), ".2f")}$ ｜｜ {datavet["symbol"]} : {format(float(datavet["bidPrice"]),".2f")}$ / 24H : {datavet["priceChangePercent"]}% / 24H : {format(float(datavet["priceChange"]), ".2f")} ｜｜ {dataxrp["symbol"]} : {format(float(dataxrp["bidPrice"]),".4f")}$ / 24H : {dataxrp["priceChangePercent"]}% / 24H : {format(float(dataxrp["priceChange"]), ".4f")}$ \\\\\\ 5 Min //')
        await channel.edit(topic=phrase)
"""
@client.command()
async def Ping(ctx):
    await ctx.send(f'Pong {round(client.latency * 1000)}ms')

client.run('Nzc2MDg0MjMzNTEyNjgxNTAy.X6vuxA.55spiLYwB6MWSKIIjtTc03Ek_A8')

