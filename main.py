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

import time




# 옵션 생성
options = webdriver.ChromeOptions()
# 랙제거
prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
options.add_experimental_option('prefs', prefs)
#executable_path= r"/app/.chromedriver/bin/chromedriver", options=options     크롬웹드라이버 클라우드할때 넣기



game= discord.Game("NEW버전 1v 페코라봇")
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

#@bot.command(aliases=['닥쳐','시발',])
#async def 아가리(ctx):
#    await ctx.send(f'말이 너무심해')

#@bot.command(aliases=['야한거',])
#async def 섹스(ctx):
#    await ctx.send(f'야한건 안되')
   
#@bot.command(aliases=['디버그'])
#async def debug(ctx):
#    await ctx.send(f'페코라는 프로그램이 아니야')
    
#@bot.command(aliases=['멈춰'])
#async def stop(ctx):
#    await ctx.send(f'24시간 영원히 살아가')


@bot.command(aliases=['슈퍼 네네치'])
async def 슈퍼네네치(ctx):
    await ctx.send(f'슈퍼 네네치~')
    await ctx.send(f'https://tenor.com/view/kon-nene-matanene-nene-nenechi-nene-seal-gif-21412185')

@bot.command(aliases=['하이퍼 네네치'])
async def 하이퍼네네치(ctx):
    await ctx.send(f'하이퍼 네네치~')
    await ctx.send(f'https://tenor.com/view/kon-nene-matanene-nene-nenechi-nene-seal-gif-21412185')

#롤상점
@bot.command(aliases=['롤 상점'])
async def 롤상점(ctx):

    embed = discord.Embed(title = "롤상점",
    description = "", color = 3066993)
    embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1082741607852519424/U84ElL3m.png')
    embed.add_field(name = "롤상점", value ="https://store.leagueoflegends.co.kr/")
    await ctx.send(embed = embed) 


##우타
#@bot.command()
#async def 우타(ctx):
#    url=('https://www.youtube.com/playlist?list=PLet0wKVboCzEMtX-hZQn1obu40HWVKn7q')

#    try:
#        driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
#        driver.implicitly_wait(10)
#        driver.get(url)

#    except:
#        await ctx.send(f'실패')
#        return

#    soup = BeautifulSoup(driver.page_source, 'html.parser')


#    aaa=soup.findAll("a", attrs={"class":"ytp-next-button ytp-button"})

#    print(aaa)

#    #await ctx.send(aaa)












#steamsale
@bot.command()
async def 스팀세일(ctx):
    url=('https://steamsale.windbell.co.kr/Next')

    try:
        driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
        driver.implicitly_wait(10)
        driver.get(url)

    except:
        await ctx.send(f'실패')
        return
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    whatsale=soup.select_one('#contents > div > div:nth-child(1) > div > h3:nth-child(1)').text
    day=soup.select_one('#contents > div > div:nth-child(1) > div > h4').text

    hour=soup.select_one('#contents > div > div:nth-child(1) > div > h3:nth-child(4) > span:nth-child(1)').text
    min=soup.select_one('#contents > div > div:nth-child(1) > div > h3:nth-child(4) > span:nth-child(2)').text
    second=soup.select_one('#contents > div > div:nth-child(1) > div > h3:nth-child(4) > span:nth-child(3)').text
    
    term=soup.select_one('#contents > div > div:nth-child(1) > div > h6').text

    day=day.replace('\n','')
    day=day.replace(' ','')
    term=term.replace('            ','')
    embed = discord.Embed(title = whatsale,
    description = "", color = 3066993)
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/512px-Steam_icon_logo.svg.png')
    embed.add_field(name = "남은기간:`" + day+ "일 "+ hour+"시간 "+min+"분 "+second+"초`", value ="세일기간:`"+term+"`")

    await ctx.send(embed = embed) 
    driver.quit()





#dc하기
@bot.command(aliases=['디씨인사이드','디씨'])
async def dc(ctx,text):


    if text in '싱글벙글':
        url=('https://gall.dcinside.com/mgallery/board/lists?id=singlebungle1472&exception_mode=recommend')
    elif text in '키즈나':
        url=('https://gall.dcinside.com/mgallery/board/lists?id=kizunaai&exception_mode=recommend')
    elif text in '몸매':
        url=('https://gall.dcinside.com/mgallery/board/lists?id=beautifulbody&exception_mode=recommend')
    else:
        await ctx.send(f'갤러리실패')
        return



    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
    driver.implicitly_wait(10)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')


    name=soup.findAll("td", attrs={"class":"gall_tit ub-word"})
   
    embed = discord.Embed(title = "`개념글`",
    description = "", color = 3066993)
    embed.set_thumbnail(url='https://static-s.aa-cdn.net/img/gp/20600005506263/VP6qsU103YOgbP_xEJhUg77FoWDIhiWOjW6YJ9BxxZpYcCzo_TJnBQhTGs5eoPGsxKI=s300?v=1')
    for i in range(0,10):
        embed.add_field(name =name[i].getText().replace('\n',''), value = f'https://gall.dcinside.com/'+name[i].find('a').get('href'),inline=False)
    await ctx.send(embed = embed)
    driver.quit()




#hololive 구독자
@bot.command(aliases=['hololive','홀로라이브구독자','hololive구독자'])
async def 홀로라이브(ctx):
    url=(f'https://trackholo.live/en/')
    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
    driver.implicitly_wait(10)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')


    name=soup.findAll("span", attrs={"style":"padding-left: 25px"})
    number=soup.findAll("a", attrs={"class":"py-3 px-2"})

    embed = discord.Embed(title = "홀로라이브구독자",
    description = "", color = 3066993)
    for i in range(len(name)):
        embed.add_field(name =  "유튜버:"+name[i].getText(), value = str(i+1)+"등: 구독자:"+"`"+number[1+4*i].getText()+"`",inline=False)
    await ctx.send(embed = embed)
    
    embed = discord.Embed(title = "홀로라이브구독자",
    description = "", color = 3066993)
    for i in range(len(name)-25):
        embed.add_field(name =  "유튜버:"+name[i+25].getText(), value = str(i+26)+"등: 구독자:"+"`"+number[1+4*(i+25)].getText()+"`",inline=False)
    await ctx.send(embed = embed)
    driver.quit()







#페코라 수익
@bot.command(aliases=['페코라 수익','페코라 정보','페코라 채널','페코라정보','페코라채널'])
async def 페코라수익(ctx):
    url=(f'https://playboard.co/channel/UC1DCedRgGHBdm81E1llLhOQ')
    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
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
    #    return
    

    embed = discord.Embed(title = "페코라 채널정보(1달러->1183원기준)",
    description = "", color = 3066993)
    embed.set_thumbnail(url=pekora)
    embed.add_field(name =  "좋아요 비율", value = box[0].getText())
    embed.add_field(name =  "싫어요 비율", value = box[1].getText())
    embed.add_field(name =  "댓글 비율", value = box[2].getText(),inline=False)
    embed.add_field(name =  "최고 동시 시청자", value = box[3].getText())
    embed.add_field(name =  "평균 동시 시청자", value = box[4].getText())
    embed.add_field(name =  "누적 방송 횟수", value = box[5].getText(),inline=False)
    embed.add_field(name =  "오늘 수입", value = "`"+str(box[6])+"₩"+"`")
    embed.add_field(name =  "어제 수입", value = "`"+str(box[7])+"₩"+"`")
    embed.add_field(name =  "최근 7일 수입", value = "`"+str(box[8])+"₩"+"`")
    embed.add_field(name =  "전체 수입", value = "`"+str(box[9])+"₩"+"`")
    await ctx.send(embed = embed) 
    driver.quit()





#나무위키
@bot.command()
async def 나무위키(ctx,*,text):
    text=text.replace(" ","%20")
    url=(f'https://namu.wiki/w/'+text)


    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
    driver.implicitly_wait(10)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        nopage=soup.select_one('#app > div > div:nth-child(2) > article > div:nth-child(3) > p:nth-child(1)').text
        embed = discord.Embed(title = text+"의 나무위키",
        description = "", color = 3066993)
        embed.set_thumbnail(url="https://w.namu.la/s/76f3cd317712c830ca32c3574db36c64e1e5ecaa7cc034113f98bec89e4a25149a8528b25fd556354c6e594c750889b3971e729596247278234391b5a6c69f4820659c9490c4d6d2e9ca9ab2815bf3ffd8c403de79405d5be2fcd9d849d9e77e")

        embed.add_field(name =  nopage, value = '띄어쓰기를 적절하게 사용해보세요')
        await ctx.send(embed = embed)
    except:
        nopage="1"
        embed = discord.Embed(title = text+"의 나무위키",
        description = "", color = 3066993)
        embed.set_thumbnail(url="https://w.namu.la/s/76f3cd317712c830ca32c3574db36c64e1e5ecaa7cc034113f98bec89e4a25149a8528b25fd556354c6e594c750889b3971e729596247278234391b5a6c69f4820659c9490c4d6d2e9ca9ab2815bf3ffd8c403de79405d5be2fcd9d849d9e77e")

        embed.add_field(name = 'https://namu.wiki/w/'+text, value = '나무위키')
        await ctx.send(embed = embed)

    driver.quit()



#롤 검색

@bot.command(aliases=['랭크','랭킹','롤 랭크','티어','롤티어'])
async def search(ctx,*,text):
    url=(f'https://www.op.gg/summoner/userName='+text)

    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
    driver.implicitly_wait(10)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')


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
    embed.add_field(name = "티어:"+"`"+Rank_text+"`", value = "포인트:"+Rank_point)
    embed.add_field(name = "승/패:"+"`"+Rank_win+"/"+Rank_lose+"`", value = "승률:"+"`"+Rank_winrate+"`",inline=False)
    embed.add_field(name ="최근 전적"+Recent_game+"시간:"+Recent_time, value = "챔프:"+Recent_champ+"___킬뎃:"+Recent_kill+"킬/"+Recent_death+"데스/"+Recent_assist+"어시")
    await ctx.send(embed = embed)
    driver.quit()



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
    embed.add_field(name = "총 확진자:"+"`"+total+"`", value ="오늘:"+"`"+num+"`")
    await ctx.send(embed = embed)


#날씨
@bot.command()
async def 날씨(ctx,*,text):


    url=(f'https://www.google.com/search?q='+text+'날씨')
    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
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
    driver.quit()















#명령어 목록 알려주기
@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title = "현재있는 명령어 목록",
    description = "", color = 0x62c1cc)
    embed.add_field(name = "!티어 (이름)", value = "랭크 검색",inline=False)
    embed.add_field(name = "!코로나", value = "코로나 정보 보기.",inline=False)
    embed.add_field(name = "!날씨", value = "날씨 정보 보기",inline=False)
    embed.add_field(name = "!나무위키 (검색할것)", value = "나무위키 사이트에 연결",inline=False)
    embed.add_field(name = "!페코라수익", value = "페코라의수익",inline=False)
    embed.add_field(name = "!디씨 (갤러리)", value = "갤러리 념글 10개 갤목록:키즈나,싱글벙글,몸매",inline=False)
    embed.add_field(name = "!스팀세일", value = "스팀세일",inline=False) 
    embed.add_field(name = "!홀로라이브", value = "홀로라이브 구독자순위",inline=False) 
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









    #안되는것들


#@bot.event
#async def on_message_edit(before, after):
#    embed = discord.Embed(title = "탐정왓슨이 수정된 메세지를 찾았습니다.",
#    description = "", color = 15844367)
#    embed.set_thumbnail(url="https://w.namu.la/s/2a901aac58e0a8898cfb238dd859af4dc55f9b24e79f0006f7aa7523222b8426433aa57f0a3ce14cc6f6d3f47796299075d2700271096ebb9599b32ca895666cc3cc58dd40d33297a0f34e91f2164e833ae044ca40f5985c5ce1cbacf903eb32")
#    embed.add_field(name =  "원본 메세지:"+before.content, value ="바뀐 메세지:"+after.content)
#    await before.channel.send(embed=embed)
#    return

##롤패치
#@bot.command()
#async def 롤패치(ctx):
#    url=('https://www.leagueoflegends.com/ko-kr/news/game-updates/')

#    try:
#        driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
#        driver.implicitly_wait(10)
#        driver.get(url)

#    except:
#        await ctx.send(f'실패')
#        return
#    soup = BeautifulSoup(driver.page_source, 'html.parser')
#    driver.find_element_by_css_selector('#gatsby-focus-wrapper > div > div.style__Wrapper-sc-1ynvx8h-0.style__ResponsiveWrapper-sc-1ynvx8h-6.gLoTys.eELrEI > div > nav > div > ol > li:nth-child(2) > button').click()
#    driver.find_element_by_css_selector('#gatsby-focus-wrapper > div > div.style__Wrapper-sc-1ynvx8h-0.style__ResponsiveWrapper-sc-1ynvx8h-6.gLoTys.eELrEI > div > div.style__Wrapper-sc-106zuld-0.style__ResponsiveWrapper-sc-106zuld-4.dRXdjM.kXYoSI.style__List-sc-1ynvx8h-3.cwQJeW > div > ol > li:nth-child(1) > a > article > div.style__Image-sc-1h41bzo-2.cbzxFR > div > div > img').click()

#    img=soup.find_all("div", attrs={"class":"style__Main-nag7bg-1 bILiti"})
#    print(img)
#    embed = discord.Embed(title = "dd",
#    description = "", color = 3066993)
#    embed.set_thumbnail(url=img)
#    embed.add_field(name ="das", value ="세일기간:")

#    await ctx.send(embed = embed) 
#    driver.quit()



##과제목록
#@bot.command()
#async def 과제목록(ctx):
#    url=('https://el.koreatech.ac.kr/ilos/main/main_form.acl')

#    try:
#        driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
#        driver.implicitly_wait(10)
#        driver.get(url)

#    except:
#        await ctx.send(f'실패')
#        return

#    soup = BeautifulSoup(driver.page_source, 'html.parser')


#    yeah=driver.find_element_by_css_selector('#header > div.utillmenu > ul > a > li').click()
#    driver.find_element_by_css_selector('#usr_id').send_keys('아이디입ㄺ')
#    driver.find_element_by_css_selector('#usr_pwd').send_keys('비밀번호입력')
#    driver.find_element_by_css_selector('#login_btn').click()
#    try:
#        driver.find_element_by_css_selector('#show_schedule_list').click()
#    except:
#        pass

#    name=soup.select_one("#view_0_st_1_2_1475634 > div:nth-child(2) > a > div.schedule_view_title")

#    print(name)



bot.run('ODg2MDU5NDc4MzU1Njg5NjAz.YTwFMQ.BJKKpCldBbCz-S4aR5x7wjveYt8')


