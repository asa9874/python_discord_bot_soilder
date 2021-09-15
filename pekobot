import discord
from discord.ext import commands
import random
import requests
from bs4 import BeautifulSoup

game= discord.Game("콘페코")
bot= commands.Bot(command_prefix='!',status=discord.Status.online,activity=game)


@bot.command(aliases=['콘페코','안녕','반가워','하이','konpeko','안뇽','오하요'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention} 콘페코~ \n https://tenor.com/view/pekora-usada-hololive-animation-strut-gif-22386678')

@bot.command(aliases=['병신','병신년','병신페코','ㅄ','ㅂㅅ','병신 페코네'])
async def beongsin(ctx):
    await ctx.send(f'병신 페코네 w')

@bot.command(aliases=['페코미코','페미','페코 미코','페코미코대전쟁','페코미코 대전쟁','페코 미코 대전쟁'])
async def pekomiko(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=m8wUO6XGJH8')

@bot.command(aliases=['자기소개'])
async def introduce(ctx):
    await ctx.send(f'こんぺこ、こんぺこ、こんぺこ！ホロライブ三期生の兎田ぺこらぺこ！どうも、どうも！\n https://tenor.com/view/pekora-kon-peko-ha-ha-ha-gif-18966253')

@bot.command(aliases=['검색','전적','전적검색'])
async def search(ctx,text):
    await ctx.send(f'https://www.op.gg/summoner/userName='+text)

@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title = "현재있는 명령어 목록",
    description = "", color = 0x62c1cc)
    embed.add_field(name = "!콘페코", value = "인사")
    embed.add_field(name = "!병신", value = "병신페코")
    embed.add_field(name = "!페코미코", value = "페코미코!")
    embed.add_field(name = "!자기소개", value = "페코라의 자기소개")
    embed.add_field(name = "!전잭 (이름)", value = "전적검색")
    await ctx.send(embed = embed)


bot.run('ODg2MDU5NDc4MzU1Njg5NjAz.YTwFMQ.BJKKpCldBbCz-S4aR5x7wjveYt8')


