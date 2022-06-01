import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='FT')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == '早':
        await message.channel.send('不早了')
        

bot.run('OTY2OTQ5NDQxODM3ODc1MjEz.GQoprp.BZRYNs4mIYOu8xrr3tnNOyeZKJtR7S7O1fW-Vk')