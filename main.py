
###################
####python 3.x#####
#discord.py==1.4.0#
###################

import discord
import asyncio
import datetime

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    else:
        y = datetime.datetime.now().year
        m = datetime.datetime.now().month
        d = datetime.datetime.now().day
        h = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        bot_logs = '1040650046271660112'
        embed = discord.Embed(title='메시지 수정됨', colour=discord.Colour.orange())
        embed.add_field(name='유저', value=f'<@{before.author.id}>({before.author})', inline=False)
        embed.set_footer(text=f"유저 ID:{before.author.id} • 메시지 ID: {before.id}")
        embed.add_field(name='수정 전', value=before.content + "\u200b", inline=True)
        embed.add_field(name='수정 후', value=after.content + "\u200b", inline=True)
        embed.add_field(name='날짜', value=f"{y}-{m}-{d} {h}:{min}", inline=False)
        await client.get_channel(int(bot_logs)).send(embed=embed)
        
@client.event
async def on_message_delete(message):
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    bot_logs = '1040650046271660112'
    embed = discord.Embed(title='메시지 삭제됨', colour=discord.Colour.orange())
    embed.add_field(name='유저', value=f'<@{message.author.id}>({message.author})')
    embed.add_field(name='채널', value=f'<#{message.channel.id}>')
    embed.add_field(name='내용', value=message.content, inline=False)
    embed.add_field(name='날짜', value=f"{y}-{m}-{d} {h}:{min}", inline=False)
    embed.set_footer(text=f"유저 ID:{message.author.id} • 메시지 ID: {message.id}")
    await client.get_channel(int(bot_logs)).send(embed=embed)


client.run('OTQyMjk0MTI4NjE4NzkwOTMy.Ga2XLl.3m9kzY5h1iNYkn5AT2m__P6cIEbS_93vw5WojY')
