from head import *
from datetime import datetime


@bot.command(aliases=['군대'])
async def goon(ctx):
    now  = datetime.now()
    await ctx.send(f'현재'+str(now))

    deadtime = datetime.strptime("20220920", "%Y%m%d")
    await ctx.send(f'비교할 날짜'+str(deadtime))

    date_diff = now - deadtime
    await ctx.send(f'남은날'+str(deadtime-now))
