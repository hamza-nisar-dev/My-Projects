import os
import discord
from discord import channel
client = discord.Client()
guild = discord.Guild
from discord.ext import tasks, commands


@client.event
async def on_message(message):
   print(message.author)
   channel=client.get_channel(901555959283990591)
   print(channel)
   d=message.content
   if message.author.id !=908393191328329748:
    if "@" in d:
        invitelink = await channel.create_invite(max_uses=1,unique=True)
        await message.reply('Hello! here is your channel link: {}'.format(invitelink), mention_author=True)
    else:
        await message.reply('Please send your eamil in order to get into the paid channel')

@tasks.loop(seconds = 10)
async def test():
    print("start")


test.start()
client.run('OTA4MzkzMTkxMzI4MzI5NzQ4.YY1FFQ.Q2ULcd7dU283HVcP6CLKanFLeHA')