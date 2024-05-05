





    #안되는것들

##나무위키
#@bot.command()
#async def 나무위키(ctx,*,text):
#    text=text.replace(" ","%20")
#    url=(f'https://namu.wiki/w/'+text)


#    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
#    driver.implicitly_wait(10)
#    driver.get(url)
#    soup = BeautifulSoup(driver.page_source, 'html.parser')
#    try:
#        nopage=soup.select_one('#app > div > div:nth-child(2) > article > div:nth-child(3) > p:nth-child(1)').text
#        embed = discord.Embed(title = text+"의 나무위키",
#        description = "", color = 3066993)
#        embed.set_thumbnail(url="https://w.namu.la/s/76f3cd317712c830ca32c3574db36c64e1e5ecaa7cc034113f98bec89e4a25149a8528b25fd556354c6e594c750889b3971e729596247278234391b5a6c69f4820659c9490c4d6d2e9ca9ab2815bf3ffd8c403de79405d5be2fcd9d849d9e77e")

#        embed.add_field(name =  nopage, value = '띄어쓰기를 적절하게 사용해보세요')
#        await ctx.send(embed = embed)
#    except:
#        nopage="1"
#        embed = discord.Embed(title = text+"의 나무위키",
#        description = "", color = 3066993)
#        embed.set_thumbnail(url="https://w.namu.la/s/76f3cd317712c830ca32c3574db36c64e1e5ecaa7cc034113f98bec89e4a25149a8528b25fd556354c6e594c750889b3971e729596247278234391b5a6c69f4820659c9490c4d6d2e9ca9ab2815bf3ffd8c403de79405d5be2fcd9d849d9e77e")

#        embed.add_field(name = 'https://namu.wiki/w/'+text, value = '나무위키')
#        await ctx.send(embed = embed)

#    driver.quit()



##롤 검색

#@bot.command(aliases=['랭크','랭킹','롤 랭크','티어','롤티어'])
#async def search(ctx,*,text):
#    url=(f'https://www.op.gg/summoner/userName='+text)

#    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
#    driver.implicitly_wait(10)
#    driver.get(url)
#    soup = BeautifulSoup(driver.page_source, 'html.parser')


#    Rank_img=soup.find("div", attrs={"class":"SummonerRatingMedium"}).find("img").get('src')
#    Rank_text=soup.find("div", attrs={"class":"TierRank"}).get_text()
#    if "Un" in Rank_text:
#        Rank_point="x"
#        Rank_win="x"
#        Rank_lose="x"
#        Rank_winrate="x"
#    else:
#        Rank_point=soup.find("span", attrs={"class":"LeaguePoints"}).get_text()
#        Rank_win=soup.find("span", attrs={"class":"wins"}).get_text()
#        Rank_lose=soup.find("span", attrs={"class":"losses"}).get_text()
#        Rank_winrate=soup.find("span", attrs={"class":"winratio"}).get_text()
    
#    Recent_game=soup.find("div", attrs={"class":"GameResult"}).get_text()
#    Recent_time=soup.find("div", attrs={"class":"GameLength"}).get_text()
#    Recent_kill=soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.KDA > div.KDA > span.Kill").text
#    Recent_death=soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.KDA > div.KDA > span.Death").text
#    Recent_assist=soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.KDA > div.KDA > span.Assist").text
#    Recent_champ=soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.GameSettingInfo > div.ChampionName > a").text

#    embed = discord.Embed(title = text+"의 랭크",
#    description = "", color = 0x62c1cc)
#    embed.set_thumbnail(url="http:" + Rank_img)
#    embed.add_field(name = "티어:"+"`"+Rank_text+"`", value = "포인트:"+Rank_point)
#    embed.add_field(name = "승/패:"+"`"+Rank_win+"/"+Rank_lose+"`", value = "승률:"+"`"+Rank_winrate+"`",inline=False)
#    embed.add_field(name ="최근 전적"+Recent_game+"시간:"+Recent_time, value = "챔프:"+Recent_champ+"___킬뎃:"+Recent_kill+"킬/"+Recent_death+"데스/"+Recent_assist+"어시")
#    await ctx.send(embed = embed)
#    driver.quit()



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




##코로나
#@bot.command(aliases=['코로나','코로나확진자','확진자수','코로나 확진자','코로나수'])
#async def covid(ctx):
#    url='http://ncov.mohw.go.kr/bdBoardList_Real.do'
#    page = requests.get(url)
#    soup = BeautifulSoup(page.content, "html.parser")


#    num =soup.find("p", attrs={"class":"inner_value"}).get_text()
#    total=soup.find("dd", attrs={"class":"ca_value"}).get_text()
#    time=soup.find("span", attrs={"class":"t_date"}).get_text()

#    embed = discord.Embed(title = "코로나 확진자"+time,
#    description = "", color = 0x62c1cc)
#    embed.add_field(name = "총 확진자:"+"`"+total+"`", value ="오늘:"+"`"+num+"`")
#    await ctx.send(embed = embed)


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


##steamsale
#@bot.command()
#async def 스팀세일(ctx):
#    url=('https://steamsale.windbell.co.kr/Next')

#    try:
#        driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
#        driver.implicitly_wait(10)
#        driver.get(url)

#    except:
#        await ctx.send(f'실패')
#        return
#    soup = BeautifulSoup(driver.page_source, 'html.parser')

#    whatsale=soup.select_one('#contents > div > div:nth-child(1) > div > h3:nth-child(1)').text
#    day=soup.select_one('#contents > div > div:nth-child(1) > div > h4').text

#    hour=soup.select_one('#contents > div > div:nth-child(1) > div > h3:nth-child(4) > span:nth-child(1)').text
#    min=soup.select_one('#contents > div > div:nth-child(1) > div > h3:nth-child(4) > span:nth-child(2)').text
#    second=soup.select_one('#contents > div > div:nth-child(1) > div > h3:nth-child(4) > span:nth-child(3)').text
    
#    term=soup.select_one('#contents > div > div:nth-child(1) > div > h6').text

#    day=day.replace('\n','')
#    day=day.replace(' ','')
#    term=term.replace('            ','')
#    embed = discord.Embed(title = whatsale,
#    description = "", color = 3066993)
#    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/512px-Steam_icon_logo.svg.png')
#    embed.add_field(name = "남은기간:`" + day+ "일 "+ hour+"시간 "+min+"분 "+second+"초`", value ="세일기간:`"+term+"`")

#    await ctx.send(embed = embed) 
#    driver.quit()






##hololive 구독자
#@bot.command(aliases=['hololive','홀로라이브구독자','hololive구독자'])
#async def 홀로라이브(ctx):
#    url=(f'https://trackholo.live/en/')
#    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
#    driver.implicitly_wait(10)
#    driver.get(url)

#    soup = BeautifulSoup(driver.page_source, 'html.parser')


#    name=soup.findAll("span", attrs={"style":"padding-left: 25px"})
#    number=soup.findAll("a", attrs={"class":"py-3 px-2"})

#    embed = discord.Embed(title = "홀로라이브구독자",
#    description = "", color = 3066993)
#    for i in range(len(name)):
#        embed.add_field(name =  "유튜버:"+name[i].getText(), value = str(i+1)+"등: 구독자:"+"`"+number[1+4*i].getText()+"`",inline=False)
#    await ctx.send(embed = embed)
    
#    embed = discord.Embed(title = "홀로라이브구독자",
#    description = "", color = 3066993)
#    for i in range(len(name)-25):
#        embed.add_field(name =  "유튜버:"+name[i+25].getText(), value = str(i+26)+"등: 구독자:"+"`"+number[1+4*(i+25)].getText()+"`",inline=False)
#    await ctx.send(embed = embed)
#    driver.quit()







##페코라 수익
#@bot.command(aliases=['페코라 수익','페코라 정보','페코라 채널','페코라정보','페코라채널'])
#async def 페코라수익(ctx):
#    url=(f'https://playboard.co/channel/UC1DCedRgGHBdm81E1llLhOQ')
#    driver=webdriver.Chrome(executable_path= r"/app/.chromedriver/bin/chromedriver", options=options)
#    driver.implicitly_wait(10)
#    driver.get(url)

#    soup = BeautifulSoup(driver.page_source, 'html.parser')

#    box=soup.find_all("div", attrs={"class":"item__count"})
#    pekora=soup.select_one('#app > div.__window > div > div > main > article > header > div > div > div.logo > a > div > picture > img').get('src')


#    #try:
#    #    for i in [6,7,8,9]:
#    #        box[i]=box[i].getText().replace("$","")
#    #        box[i]=box[i].replace(",","")
#    #        box[i]=int(box[i])
#    #        box[i]=format(int(box[i]*1183),",")
#    #except:
#    #    await ctx.send(f'원변환 실패')
#    #    return
    

#    embed = discord.Embed(title = "페코라 채널정보(1달러->1183원기준)",
#    description = "", color = 3066993)
#    embed.set_thumbnail(url=pekora)
#    embed.add_field(name =  "좋아요 비율", value = box[0].getText())
#    embed.add_field(name =  "싫어요 비율", value = box[1].getText())
#    embed.add_field(name =  "댓글 비율", value = box[2].getText(),inline=False)
#    embed.add_field(name =  "최고 동시 시청자", value = box[3].getText())
#    embed.add_field(name =  "평균 동시 시청자", value = box[4].getText())
#    embed.add_field(name =  "누적 방송 횟수", value = box[5].getText(),inline=False)
#    embed.add_field(name =  "오늘 수입", value = "`"+str(box[6])+"₩"+"`")
#    embed.add_field(name =  "어제 수입", value = "`"+str(box[7])+"₩"+"`")
#    embed.add_field(name =  "최근 7일 수입", value = "`"+str(box[8])+"₩"+"`")
#    embed.add_field(name =  "전체 수입", value = "`"+str(box[9])+"₩"+"`")
#    await ctx.send(embed = embed) 
#    driver.quit()

