import discord
from discord.ext import commands
from binance.client import Client
from datetime import datetime
import csv
import matplotlib.pyplot as plt 
import mplfinance as mpf
import pandas as pd
import matplotlib.dates as mpl_dates



class Graph(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["g", "gr"])
    async def graph(self, ctx, paire, interv ="1m"):
        apik = "s7O4bcEALbiJJ7AIhjbHDoWOZXEIkXHls5vLuAxD23nShT5LUhEXHWaCMfcgu2Y5"
        apisk = "9V9U1a5UVQRcXspOVOlxh4KgcYaUgVsK7Zq8CPSuKSPcPxDOk1iV5mBtDfeykPWD"
        openacc = Client(apik, apisk)
        stamp = datetime.timestamp(datetime.now())
        try:
            if (interv.lower()[:3] == "1mo"):
                kline = openacc.get_historical_klines(f'{paire.upper()}', interval=Client.KLINE_INTERVAL_1MONTH,start_str="10 year ago UTC")
            elif (interv.lower()[:2] == "1m"):
                kline = openacc.get_historical_klines(f'{paire.upper()}', interval=Client.KLINE_INTERVAL_1MINUTE,start_str="150 minutes ago UTC")
            elif (interv.lower()[:2] == "5m"):
                kline = openacc.get_historical_klines(f'{paire.upper()}', interval=Client.KLINE_INTERVAL_5MINUTE,start_str="10 hours ago UTC")
            elif (interv.lower()[:3] == "15m"):
                kline = openacc.get_historical_klines(f'{paire.upper()}', interval=Client.KLINE_INTERVAL_15MINUTE,start_str="30 hours ago UTC")
            elif (interv.lower()[:3] == "30m"):
                kline = openacc.get_historical_klines(f'{paire.upper()}', interval=Client.KLINE_INTERVAL_30MINUTE,start_str="3 days ago UTC")
            elif (interv.lower()[:2] == "1h"):
                kline = openacc.get_historical_klines(f'{paire.upper()}', interval=Client.KLINE_INTERVAL_1HOUR,start_str="5 days ago UTC")
            elif (interv.lower()[:2] == "4h"):
                kline = openacc.get_historical_klines(f'{paire.upper()}', interval=Client.KLINE_INTERVAL_4HOUR,start_str="2 weeks ago UTC")
            elif (interv.lower()[:3] == "12h"):
                kline = openacc.get_historical_klines(f'{paire.upper()}', interval=Client.KLINE_INTERVAL_12HOUR,start_str="1 month ago UTC")
            elif (interv.lower()[:2] == "1d"):
                kline = openacc.get_historical_klines(f'{paire.upper()}', interval=Client.KLINE_INTERVAL_1DAY,start_str="3 month ago UTC")
            elif (interv.lower()[:2] == "1w"):
                kline = openacc.get_historical_klines(f'{paire.upper()}', interval=Client.KLINE_INTERVAL_1WEEK,start_str="2 year ago UTC")
            else:
                await ctx.send("Ne reconnais pas la durée, durées disponibles : ['1m','5m','15m','30m','1h','4h','12h','1d','1w','1mo']")
        except Exception as e:
            await ctx.send("Erreur : \nPaire non reconnue, (une paire : BTCUSDT) \nLe dollar c'est USDT ")
            await ctx.send(f"Erreur: {e.message}")
            return
        with open("kline.csv", "w") as datakline:
            fields = ["Date", "Open", "High", "Low", "Close", "Volume"]
            writer = csv.DictWriter(datakline, fieldnames=fields)
            writer.writerow({"Date": "Date", "Open": "Open", "High": "High", "Low": "Low", "Close": "Close", "Volume": "Volume"})
            for lines in kline:
                row = {"Date": f'{lines[0]}', "Open": f'{lines[1]}', "High": f'{lines[2]}', "Low": f'{lines[3]}', "Close": f'{lines[4]}', "Volume": f'{lines[5]}'}
                writer.writerow(row)

        mc = mpf.make_marketcolors(
            up='#00ff00', down='red',
            edge={'up':'green', 'down':'red'},
            wick={'up':'green', 'down':'red'},
            volume={'up':'green', 'down':'red'}
        )
        mestyle = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=mc)
        df = pd.read_csv('kline.csv', index_col="Date")
        df.index = pd.to_datetime(df.index, unit='ms')
        mpf.plot(df, type='candle', style=mestyle,
        title=f'{paire.upper()} : {interv}',
        ylabel='Prix $',
        volume=True,
        mav=(25,50,100),
        figratio=(12,6),
        savefig='result.png')
        with open("./result.png","rb") as graphique:
            await ctx.send(file=discord.File(graphique, f'{paire}.png'))
        
def setup(client):
    client.add_cog(Graph(client))