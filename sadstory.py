from head import *
from datetime import datetime, timedelta


human={'곽호준':datetime.strptime("2022.01.24", "%Y.%m.%d").date(),
       '지인혁':datetime.strptime("2022.01.24", "%Y.%m.%d").date(),
       '윤지환':datetime.strptime("2022.01.24", "%Y.%m.%d").date(),
       '정동호':datetime.strptime("2022.02.08", "%Y.%m.%d").date(),
       '김영권':datetime.strptime("2022.03.15", "%Y.%m.%d").date(),
       '김우현':datetime.strptime("2022.02.21", "%Y.%m.%d").date(),
       '김윤석':datetime.strptime("2022.05.16", "%Y.%m.%d").date(),
       '한동희':datetime.strptime("2022.05.23", "%Y.%m.%d").date(),
       '임승현':datetime.strptime("2022.05.09", "%Y.%m.%d").date(),
       '신승호':datetime.strptime("2022.06.14", "%Y.%m.%d").date(),
       '박종범':datetime.strptime("2022.09.20", "%Y.%m.%d").date(),
       '이병웅':datetime.strptime("2022.09.20", "%Y.%m.%d").date(),
       '조재민':datetime.strptime("2022.09.20", "%Y.%m.%d").date(),
       '천우혁':datetime.strptime("2022.07.25", "%Y.%m.%d").date(),
       }



@bot.command(aliases=['goon'])
async def 군대(ctx,*,text):
    if(text in human):
        now  = datetime.now().date() #오늘 
        endtime=human[text]+timedelta(days=546)
        lasttime= endtime-now
        happytime=endtime-now
        embed = discord.Embed(title = text+"의 군대",
        description = "", color = 3066993)
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Military_Manpower_Administration_Gutgeoni1.png/200px-Military_Manpower_Administration_Gutgeoni1.png')
       
        
        if(lasttime>= timedelta(days=546)):
            deadtime=lasttime-timedelta(days=546)
            embed.add_field(name ='남은입대일',value =str(deadtime))
        else:
            embed.add_field(name ='고통받은 날',value ="+"+str(timedelta(days=546)-lasttime))
        embed.add_field(name ='전역일',value =str(endtime.year)+"년"+str(endtime.month)+"월"+str(endtime.day)+"일",inline=False)
        embed.add_field(name ='남은전역일',value =str(happytime))
        await ctx.send(embed = embed) 
    else:
        await ctx.send("몰루")
