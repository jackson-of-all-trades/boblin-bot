import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello {message.author}!')
    
    if message.content.startswith('$echo'):
        await message.channel.send(message.content.replace("$echo", ""))

client.run('MTM0MDc2OTIwNzQ5ODgzMzk4MA.G9p4u1.frfywH05jWa63mdERWOJV4ZPkUlfLs2oBEbPxo')
