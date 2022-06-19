from head import *
from datetime import datetime


@bot.command(aliases=['goon'])
async def 군대(ctx,*,text):
    now  = datetime.now().date()
    if text=="곽호준":
        endtime = datetime.strptime("20230723", "%Y%m%d").date()
        
    if text=="박종범" or text=="이병웅" or text=="조재민":
        deadtime = datetime.strptime("20220920", "%Y%m%d").date()
        endtime = datetime.strptime("20240319", "%Y%m%d").date()
        lasttime= deadtime-now
    
    if(text=="박종범" or text=="이병웅" or text=="조재민" or text=="곽호준"):
        happytime=endtime-now
        embed = discord.Embed(title = text+"의 군대",
        description = "", color = 3066993)
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Military_Manpower_Administration_Gutgeoni1.png/200px-Military_Manpower_Administration_Gutgeoni1.png')
        if text=="박종범" or text=="이병웅" or text=="조재민":
            embed.add_field(name ='입대일',value =str(deadtime.year)+"년"+str(deadtime.month)+"월"+str(deadtime.day)+"일",inline=False)
            embed.add_field(name ='남은입대일',value =str(lasttime))
        embed.add_field(name ='전역일',value =str(endtime.year)+"년"+str(endtime.month)+"월"+str(endtime.day)+"일",inline=False)
        embed.add_field(name ='남은전역일',value =str(happytime))
        await ctx.send(embed = embed) 
    else:
        await ctx.send("몰?루")
