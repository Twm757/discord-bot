# bot.py
import os
import discord
from dotenv import load_dotenv, find_dotenv

#finds the env file and sets the login token
load_dotenv(find_dotenv())
TOKEN = os.getenv('discord-token')

#defines the client and the intent
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)