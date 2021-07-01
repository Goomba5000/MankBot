# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import tasks
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

picIndex = 1

@tasks.loop(seconds=2)
async def send():
    # Iterates index.
    global picIndex
    
    # Forms filename.
    prefix = "scene"
    filename = "Mank\\"
    numStr = str(picIndex)
    for i in range(5-len(numStr)):
        prefix += "0"
    filename += prefix + numStr + ".png"
    print(filename);

    # Sends appropriate image in channel.
    for guild in client.guilds:
        if guild.name == GUILD:
            for channel in guild.channels:
                if channel.name == "test":
                    await channel.send(file=discord.File(filename))
    picIndex += 24

@client.event
async def on_ready():
    picIndex = -1
    for guild in client.guilds:
        if guild.name == GUILD:
            break;
    print(
        f'{client.user} has connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    send.start()

#picIndex = -1
client.run(TOKEN)
