import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODUxNDg2OTUzOTQxMjM3ODEw.YL4_BQ.P967E_TERQtmBh4icz3N4iF_BoU')
