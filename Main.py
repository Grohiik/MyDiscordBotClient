import discord
from hidden import my_token as TOKEN

client = discord.Client()



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

@client.event
async def on_ready():
    print("Logged in as")
    print("{0.user}".format(client))
    print(client.user.id)
    print("------")

client.run(TOKEN)