import discord
from discord.ext import commands
import random
import requests
from bs4 import BeautifulSoup
import os


import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait











game= discord.Game("!명령어")
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







@bot.command(aliases=['랭크','랭킹','롤 랭크','티어','롤티어'])
async def search(ctx,text):
    print(text)
    url=(f'https://www.op.gg/summoner/userName='+text)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    Rank_img=soup.find("div", attrs={"class":"SummonerRatingMedium"}).find("img").get('src')
    Rank_text=soup.find("div", attrs={"class":"TierRank"}).get_text()
    Rank_point=soup.find("span", attrs={"class":"LeaguePoints"}).get_text()
    Rank_win=soup.find("span", attrs={"class":"wins"}).get_text()
    Rank_lose=soup.find("span", attrs={"class":"losses"}).get_text()
    Rank_winrate=soup.find("span", attrs={"class":"winratio"}).get_text()
    
    Recent_game=soup.find("div", attrs={"class":"GameResult"}).get_text()
    Recent_time=soup.find("div", attrs={"class":"GameLength"}).get_text()
    Recent_kill=soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.KDA > div.KDA > span.Kill").text
    Recent_death=soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.KDA > div.KDA > span.Death").text
    Recent_assist=soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.KDA > div.KDA > span.Assist").text
    Recent_champ=soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.GameSettingInfo > div.ChampionName > a").text

    embed = discord.Embed(title = text+"의 랭크",
    description = "", color = 0x62c1cc)
    embed.set_thumbnail(url="http:" + Rank_img)
    embed.add_field(name = Rank_text, value = Rank_point)
    embed.add_field(name = Rank_win+"/"+Rank_lose, value = Rank_winrate,inline=False)
    embed.add_field(name ="최근 전적"+Recent_game+"시간:"+Recent_time, value = "챔프:"+Recent_champ+"___킬뎃:"+Recent_kill+"킬/"+Recent_death+"데스/"+Recent_assist+"어시")
    await ctx.send(embed = embed)



@bot.command(aliases=['코로나','코로나확진자','확진자수','코로나 확진자','코로나수'])
async def covid(ctx):
    url='http://ncov.mohw.go.kr/bdBoardList_Real.do'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")


    num =soup.find("p", attrs={"class":"inner_value"}).get_text()
    total=soup.find("dd", attrs={"class":"ca_value"}).get_text()
    time=soup.find("span", attrs={"class":"t_date"}).get_text()

    embed = discord.Embed(title = "코로나 확진자"+time,
    description = "", color = 0x62c1cc)
    embed.add_field(name = "총 확진자:"+total, value ="오늘:"+num)
    await ctx.send(embed = embed)


@bot.command('온도')
async def 날씨(ctx,text):


    url=(f'https://rp5.ru/'+text+'의_날씨')
    driver=webdriver.Chrome()
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    Weather_tem=soup.select_one('#ArchTemp > span.t_0').text



    embed = discord.Embed(title = text+"의 날씨",
    description = "", color = 0x62c1cc)
    embed.add_field(name =  "온도:"+Weather_tem, value =츄츄)
    await ctx.send(embed = embed)






    embed = discord.Embed(title = text+"의 날씨",
    description = "", color = 0x62c1cc)
    embed.set_thumbnail(url="http:" +Weather_img)
    embed.add_field(name =  "온도:"+Weather_tem, value = "비올확률:"+Weather_rain+"습도:"+Weather_water)
    await ctx.send(embed = embed)









@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title = "현재있는 명령어 목록",
    description = "", color = 0x62c1cc)
    embed.add_field(name = "!콘페코", value = "인사",inline=False)
    embed.add_field(name = "!병신", value = "병신페코",inline=False)
    embed.add_field(name = "!페코미코", value = "페코미코!",inline=False)
    embed.add_field(name = "!자기소개", value = "페코라의 자기소개",inline=False)
    embed.add_field(name = "!티어 (이름)", value = "랭크 검색",inline=False)
    embed.add_field(name = "!코로나", value = "코로나 정보 보기.",inline=False)
    await ctx.send(embed = embed)







@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title = "무슨소리인지 모르겠는페코",
        description = "", color = 0x62c1cc)
        embed.add_field(name = "명령어 목록", value = "!명령어로 확인")
        await ctx.send(embed = embed)







bot.run('ODg2MDU5NDc4MzU1Njg5NjAz.YTwFMQ.BJKKpCldBbCz-S4aR5x7wjveYt8')


