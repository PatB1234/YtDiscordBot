import discord 
import asyncio
import random

with open('token.txt') as f:
    contents = f.read()

images = ["Images/ArduinoJPG.jpg", "Images/ClickerImage.jpg", "Images/LoginImage.jpg", "Images/DiscordImage.jpg", "Images/logo.png"]
bot = discord.Client()
@bot.event
async def on_message(message):
    if message.content == "Hello Bot":
        await message.channel.send("Hello YT!")
    if message.content == "Send Me A Image":

        a = len(images)
        b = random.randint(0, a-1)

        await message.channel.send(file = discord.File(images[b]))
    if message.content == "Play Mad Libs" :


        msg1 = "________"
        msg2 = "________"
        await message.channel.send("Your Sentence is:")
        await message.channel.send("I like " + msg1 + " fries but I do not like " + msg2 + " Carrots")
        await message.channel.send("Please say your first word in the sentence")
        msg1 = await bot.wait_for("message")
        msg1 = msg1.content.lower()
        await message.channel.send("Please say your second word in the sentence")
        msg2 = await bot.wait_for("message")
        msg2 = msg2.content.lower()
        await message.channel.send("Your new sentence is:")
        await message.channel.send("I like " + msg1 + " fries but I do not like " + msg2 + " Carrots")

bot.run(contents)
