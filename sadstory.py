from head import *
from datetime import datetime


@bot.command(aliases=['군대'])
async def goon(ctx):
    now  = datetime.now().date()
    
    deadtime = datetime.strptime("20220920", "%Y%m%d").date()
    lasttime= deadtime-now
    
    embed = discord.Embed(title = "군대",
    description = "", color = 3066993)
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Military_Manpower_Administration_Gutgeoni1.png/200px-Military_Manpower_Administration_Gutgeoni1.png')
    embed.add_field(name ='현재',value =str(now.year)+"년"+str(now.month)+"월"+str(now.day)+"일",inline=False)
    embed.add_field(name ='입대일',value =str(deadtime.year)+"년"+str(deadtime.month)+"월"+str(deadtime.day)+"일",inline=False)
    embed.add_field(name ='남은날',value =str(lasttime))
    await ctx.send(embed = embed) 
