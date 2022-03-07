import discord
from discord.ext import commands

token = "OTE2MDYwNzkyMDQ1MDQzNzEz.YiRT-A.VquBFYKRQ-3DTeHtGPTnqS5tL6c"

bot = commands.Bot(command_prefix = "123456789")

print('What would you like to stream?')
status = input(' > ')

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = status,
        url = 'https://www.twitch.tv/twitch'
    )
    print('Streaming: ' + status)
    await bot.change_presence(activity=stream)

bot.run(token, bot=False)    
