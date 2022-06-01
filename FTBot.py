import discord
import random

client = discord.Client()
@client.event
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '早':
        await message.channel.send('早上好')
    if message.content == 'WAH':
        await message.channel.send('WAH你老師')
    if message.content == '幹':
        await message.channel.send('來打架阿')
    if message.content == '三小':
        await message.channel.send('舒服啦')
    if message.content == '笑死':
        await message.channel.send('欸嘿嘿')
    if message.content == '嗨':
        await message.reply('你好')

client.run('OTY2OTQ5NDQxODM3ODc1MjEz.GQoprp.BZRYNs4mIYOu8xrr3tnNOyeZKJtR7S7O1fW-Vk')
