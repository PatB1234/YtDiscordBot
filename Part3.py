import discord 
import asyncio
import random

with open('token.txt') as f:
    contents = f.read()

images = ["Images/ArduinoJPG.jpg", "Images/CLickerImage.jpg", "Images/Coding.gif", "Images/LoginImage.jpg", "Images/DiscordImage.jpg", "Images/logo.png"]
bot = discord.Client()
@bot.event
async def on_message(message):
    if (message.content == "Hello Bot"):
        await message.channel.send("Hello YT!")
    if (message.content == "Send Me A Image"):

        a = len(images)
        b = random.randint(0, a-1)

        await message.channel.send(file = discord.File(images[b]))

bot.run(contents)
