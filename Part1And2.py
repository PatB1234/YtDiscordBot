

import discord 
import asyncio

bot = discord.Client()
@bot.event
async def on_message(message):
    print(message.content)
    if (message.content == "Hello Bot"):
        await message.channel.send("Hello YT!")
        await message.channel.send(file=discord.File("Your File Directory"))
        
bot.run('Your Token Here')
