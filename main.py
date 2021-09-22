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



#executable_path= r"/app/.chromedriver/bin/chromedriver"     크롬웹드라이버 클라우드할때 넣기



game= discord.Game("버전 2.0.4v 페코라봇")
bot= commands.Bot(command_prefix='!',status=discord.Status.online,activity=game)







#잡다한 말들

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

@bot.command(aliases=['닥쳐','시발',])
async def 아가리(ctx):
    await ctx.send(f'말이 너무심해')

@bot.command(aliases=['야한거',])
async def 섹스(ctx):
    await ctx.send(f'야한건 안되')
   
@bot.command(aliases=['디버그'])
async def debug(ctx):
    await ctx.send(f'페코라는 프로그램이 아니야')
    
@bot.command(aliases=['멈춰'])
async def stop(ctx):
    await ctx.send(f'24시간 영원히 살아가')

@bot.command(aliases=['슈퍼 네네치'])
async def 슈퍼네네치(ctx):
    await ctx.send(f'슈퍼 네네치~')
    await ctx.send(f'https://tenor.com/view/kon-nene-matanene-nene-nenechi-nene-seal-gif-21412185')

@bot.command(aliases=['하이퍼 네네치'])
async def 하이퍼네네치(ctx):
    await ctx.send(f'하이퍼 네네치~')
    await ctx.send(f'https://tenor.com/view/kon-nene-matanene-nene-nenechi-nene-seal-gif-21412185')





#hololive 구독자
@bot.command(aliases=['hololive','홀로라이브구독자','hololive구독자'])
async def 홀로라이브(ctx):
    url=(f'https://trackholo.live/en/')
    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver")
    driver.implicitly_wait(10)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')


    name=soup.findAll("span", attrs={"style":"padding-left: 25px"})
    number=soup.findAll("a", attrs={"class":"py-3 px-2"})

    for i in name:
        print(i.getText())
        
    for j in number:
        print(j.getText())

    embed = discord.Embed(title = "홀로라이브구독자",
    description = "", color = 3066993)
    for i in range(len(name)):
        embed.add_field(name =  "유튜버:"+name[i].getText(), value = str(i+1)+"등 구독자:"+number[1+4*i].getText(),inline=False)
    await ctx.send(embed = embed)
    
    embed = discord.Embed(title = "홀로라이브구독자",
    description = "", color = 3066993)
    for i in range(len(name)-25):
        embed.add_field(name =  "유튜버:"+name[i+25].getText(), value = str(i+26)+"등 구독자:"+number[1+4*(i+25)].getText(),inline=False)
    await ctx.send(embed = embed)



#페코라 수익
@bot.command(aliases=['페코라 수익','페코라 정보','페코라 채널','페코라정보','페코라채널'])
async def 페코라수익(ctx):
    url=(f'https://playboard.co/channel/UC1DCedRgGHBdm81E1llLhOQ')
    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver")
    driver.implicitly_wait(10)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    box=soup.find_all("div", attrs={"class":"item__count"})
    pekora=soup.select_one('#app > div.__window > div > div > main > article > header > div > div > div.logo > a > div > picture > img').get('src')
    #try:
    #    for i in [6,7,8,9]:
    #        box[i]=box[i].getText().replace("$","")
    #        box[i]=box[i].replace(",","")
    #        box[i]=int(box[i])
    #        box[i]=format(int(box[i]*1183),",")
    #except:
    #    await ctx.send(f'원변환 실패')
    
    embed = discord.Embed(title = "페코라 채널정보",
    description = "", color = 3066993)
    embed.set_thumbnail(url=pekora)

    embed.add_field(name =  "좋아요 비율", value = box[0].getText())
    embed.add_field(name =  "싫어요 비율", value = box[1].getText())
    embed.add_field(name =  "댓글 비율", value = box[2].getText(),inline=False)
    embed.add_field(name =  "최고 동시 시청자", value = box[3].getText())
    embed.add_field(name =  "평균 동시 시청자", value = box[4].getText())
    embed.add_field(name =  "누적 방송 횟수", value = box[5].getText(),inline=False)
    embed.add_field(name =  "오늘 수입", value = box[6].getText())
    embed.add_field(name =  "어제 수입", value = box[7].getText())
    embed.add_field(name =  "최근 7일 수입", value = box[8].getText())
    embed.add_field(name =  "전체 수입", value = box[9].getText())
    await ctx.send(embed = embed) 






#나무위키
@bot.command()
async def 나무위키(ctx,*,text):
    text=text.replace(" ","%20")
    url=(f'https://namu.wiki/w/'+text)


    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver")
    driver.implicitly_wait(10)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        nopage=soup.select_one('#app > div > div:nth-child(2) > article > div:nth-child(3) > p:nth-child(1)').text
    except:
        nopage="1"

    if "찾을수" and "문서를" in nopage:
        embed = discord.Embed(title = text+"의 나무위키",
        description = "", color = 3066993)
        embed.set_thumbnail(url="https://w.namu.la/s/76f3cd317712c830ca32c3574db36c64e1e5ecaa7cc034113f98bec89e4a25149a8528b25fd556354c6e594c750889b3971e729596247278234391b5a6c69f4820659c9490c4d6d2e9ca9ab2815bf3ffd8c403de79405d5be2fcd9d849d9e77e")

        embed.add_field(name =  nopage, value = '띄어쓰기를 적절하게 사용해보세요')
        await ctx.send(embed = embed)

    else:
        embed = discord.Embed(title = text+"의 나무위키",
        description = "", color = 3066993)
        embed.set_thumbnail(url="https://w.namu.la/s/76f3cd317712c830ca32c3574db36c64e1e5ecaa7cc034113f98bec89e4a25149a8528b25fd556354c6e594c750889b3971e729596247278234391b5a6c69f4820659c9490c4d6d2e9ca9ab2815bf3ffd8c403de79405d5be2fcd9d849d9e77e")

        embed.add_field(name = 'https://namu.wiki/w/'+text, value = '나무위키'+nopage)
        await ctx.send(embed = embed)



#롤 검색

@bot.command(aliases=['랭크','랭킹','롤 랭크','티어','롤티어'])
async def search(ctx,*,text):
    print(text)
    url=(f'https://www.op.gg/summoner/userName='+text)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    Rank_img=soup.find("div", attrs={"class":"SummonerRatingMedium"}).find("img").get('src')
    Rank_text=soup.find("div", attrs={"class":"TierRank"}).get_text()
    if "Un" in Rank_text:
        Rank_point="x"
        Rank_win="x"
        Rank_lose="x"
        Rank_winrate="x"
    else:
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
    embed.add_field(name = "티어:"+Rank_text, value = "포인트:"+Rank_point)
    embed.add_field(name = "승/패:"+Rank_win+"/"+Rank_lose, value = "승률:"+Rank_winrate,inline=False)
    embed.add_field(name ="최근 전적"+Recent_game+"시간:"+Recent_time, value = "챔프:"+Recent_champ+"___킬뎃:"+Recent_kill+"킬/"+Recent_death+"데스/"+Recent_assist+"어시")
    await ctx.send(embed = embed)




#코로나
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


#날씨
@bot.command()
async def 날씨(ctx,*,text):


    url=(f'https://www.google.com/search?q='+text+'날씨')
    driver=webdriver.Chrome(r"/app/.chromedriver/bin/chromedriver")
    driver.implicitly_wait(10)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    Weather_img=soup.select_one('#wob_tci')['src']
    Weather_rain=soup.select_one('#wob_pp').text
    Weather_water=soup.select_one('#wob_hm').text



    embed = discord.Embed(title = text+"의 날씨",
    description = "", color = 0x62c1cc)
    embed.set_thumbnail(url="http:" + Weather_img)
    embed.add_field(name =  "비올확률:"+Weather_rain, value ="습도:"+Weather_water)
    await ctx.send(embed = embed)















#명령어 목록 알려주기
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
    embed.add_field(name = "!날씨", value = "날씨 정보 보기",inline=False)
    embed.add_field(name = "!나무위키 (검색할것)", value = "나무위키 사이트에 연결",inline=False)
    embed.add_field(name = "!페코라수익", value = "페코라의수익",inline=False)
    await ctx.send(embed = embed)






#이벤트목록
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title = "무슨소리인지 모르겠는페코",
        description = "", color = 0x62c1cc)
        embed.add_field(name = "명령어 목록", value = "!명령어로 확인")
        await ctx.send(embed = embed)

@bot.event
async def on_message_delete(message):

    embed = discord.Embed(title = "탐정왓슨이 삭제된 메세지를 찾았습니다.",
    description = "", color = 15844367)
    embed.set_thumbnail(url="https://w.namu.la/s/2a901aac58e0a8898cfb238dd859af4dc55f9b24e79f0006f7aa7523222b8426433aa57f0a3ce14cc6f6d3f47796299075d2700271096ebb9599b32ca895666cc3cc58dd40d33297a0f34e91f2164e833ae044ca40f5985c5ce1cbacf903eb32")
    embed.add_field(name =  "삭제한사람:"+ str(message.author), value ="메세지:"+message.content)
    await message.channel.send(embed=embed)
    return

#@bot.event
#async def on_message_edit(before, after):
#    embed = discord.Embed(title = "탐정왓슨이 수정된 메세지를 찾았습니다.",
#    description = "", color = 15844367)
#    embed.set_thumbnail(url="https://w.namu.la/s/2a901aac58e0a8898cfb238dd859af4dc55f9b24e79f0006f7aa7523222b8426433aa57f0a3ce14cc6f6d3f47796299075d2700271096ebb9599b32ca895666cc3cc58dd40d33297a0f34e91f2164e833ae044ca40f5985c5ce1cbacf903eb32")
#    embed.add_field(name =  "원본 메세지:"+before.content, value ="바뀐 메세지:"+after.content)
#    await before.channel.send(embed=embed)
#    return






bot.run('ODg2MDU5NDc4MzU1Njg5NjAz.YTwFMQ.BJKKpCldBbCz-S4aR5x7wjveYt8')


