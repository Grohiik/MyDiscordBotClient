import discord
from discord.ext import commands
from hidden import my_token as TOKEN
import asyncio
import threading


client = commands.Bot(command_prefix="!")


async def start():
    await client.start(TOKEN)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # window.add_to_msgs(f"{message.author}: {message.content}")
    print(f"{message.author} in {message.channel.name}: {message.content}")
    await client.process_commands(message)


@client.event
async def on_ready():
    print("Logged in as")
    print("{0.user}".format(client))
    print(client.user.id)
    print("------")
