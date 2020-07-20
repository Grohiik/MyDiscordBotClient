import discord
from discord.ext import commands
from hidden import my_token as TOKEN
import asyncio

#from window import startwindow


client = commands.Bot(command_prefix = "!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #window.add_to_msgs(f"{message.author}: {message.content}")
    print(f"{message.author} in {message.channel.name}: {message.content}")
    await client.process_commands(message)

@client.event
async def on_ready():
    print("Logged in as")
    print("{0.user}".format(client))
    print(client.user.id)
    print("------")


#loop = asyncio.get_event_loop()
#loop.create_task(client.start(TOKEN))
#loop.create_task(startwindow())
#loop.run_forever()
#client.run()
asyncio.get_event_loop.run_forever(client.start(TOKEN))