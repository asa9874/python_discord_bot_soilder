from head import *

@bot.command(aliases=['안녕','반가워','하이','안뇽','오하요','야하롱'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention} 충성!')

@bot.command(aliases=['병신','병신년','ㅄ','ㅂㅅ'])
async def beongsin(ctx):
    await ctx.send(f'병신')

@bot.command("날군인으로해줘")
async def rename(ctx):
    try:
        await ctx.author.edit(nick="군인")
    except:
        await ctx.send(f'관리자는 못바꿔')


@bot.command('들어와')
async def join(ctx):
    try:
        if ctx.author.voice and ctx.author.voice.channel:
    	    channel = ctx.author.voice.channel
    	    await channel.connect()
    except:
    	await ctx.send("음성채널 감지 실패")



@bot.command('월급')
async def money(ctx):
    embed = discord.Embed(title = "<2022년도 군인 월급>",
    description = "", color = 0x62c1cc)
    embed.set_thumbnail(url="https://pbs.twimg.com/media/EM7weQeU0AA3Qkk.png")
    embed.add_field(name =  "◆이병◆", value ="510,089원",inline=False)
    embed.add_field(name =  "◆일병◆", value ="552,023원",inline=False)
    embed.add_field(name =  "◆상병◆", value ="610,183원",inline=False)
    embed.add_field(name =  "◆병장◆", value ="676,115원",inline=False)
    await ctx.send(embed = embed)



#날씨
@bot.command()
async def 날씨(ctx,*,text):


    url=(f'https://www.google.com/search?q='+text+'날씨')
    driver=webdriver.Chrome(executable_path= r"chromedriver", options=options)
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
    embed.add_field(name = "없어", value = "없어",inline=False)
    await ctx.send(embed = embed)

