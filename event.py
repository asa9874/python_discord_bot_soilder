from head import *



#이벤트목록
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title = "잘못들었습니다?",
        description = "", color = 0x62c1cc)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/e/eb/Military_Manpower_Administration_Gutgeoni1.png")
        embed.add_field(name = " ", value = " ")
        await ctx.send(embed = embed)

#@bot.event
#async def on_message_delete(message):

#    embed = discord.Embed(title = "굳건이가 삭제된 메세지를 찾았습니다.",
#    description = "", color = 15844367)
#    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/e/eb/Military_Manpower_Administration_Gutgeoni1.png")
#    embed.add_field(name =  "삭제한메세지주인:"+ str(message.author), value ="메세지:"+message.content)
#    await message.channel.send(embed=embed)
#    return
