import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    test = "200"
    client.user.edit(username = "IT'S CHRISTMAS IN {} DAYS".format(test))
    if message.author == client.user:
        return
    else:
        await message.channel.send('STFU!')
file = open("token.txt")
token = file.read()
client.run(token)
