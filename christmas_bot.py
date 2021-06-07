import datetime
import discord

client = discord.Client()

@client.event
async def on_ready():
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
    date = date.today()
    christmas_day = datetime.datetime(date.year,12,25)
    delta = christmas_day - date
    time_change = datetime.timedelta(delta)
    client.user.edit(username = "IT'S CHRISTMAS IN {} DAYS".format(time_change.days))

file = open("token.txt")
token = file.read()
client.run(token)
