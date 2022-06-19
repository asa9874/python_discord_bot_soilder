from head import *


@bot.command('들어와')
async def join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
    	channel = ctx.author.voice.channel
    	await channel.connect()
    else:
    	await ctx.send("음성채널 감지 실패")