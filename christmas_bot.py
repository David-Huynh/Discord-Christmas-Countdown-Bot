from datetime import datetime, timedelta
import discord
from discord.ext import tasks

client = discord.Client()
@client.event
async def on_ready():
    update_name.start()
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        await message.channel.send('STFU!')
        await message.channel.send(client.user.display_name)

@tasks.loop(hours=24)
async def update_name():
    print(client.user.display_name)
    date = datetime.now()
    christmas_day = datetime(date.year,12,25)
    delta = christmas_day - date
    await client.user.edit(username = "IT'S CHRISTMAS IN {} DAYS".format(delta.days))


file = open("token.txt")
token = file.read()
client.run(token)
