from datetime import datetime
from dotenv import load_dotenv
import os
import discord
from discord.ext import tasks, commands

#Creates an instance of a discord client
client = discord.Client()
bot = commands.Bot(command_prefix='-')

#starts the update task when the client is ready
@client.event
async def on_ready():
    bot.add_command(christmas_date)
    update_name.start()
    send_message.start()
    print('We have logged in as {0.user}'.format(client))

#For simplicity sends message to the first text channel in every guild/server
#and uses the username to send the date
@tasks.loop(hours=24)
async def send_message():
    print(client.user.display_name)
    for guild in client.guilds:
        print(guild.text_channels)
        channel = client.get_channel(guild.text_channels[0].id)
        await channel.send(client.user.display_name)

#Checks the difference in time till christmas from the current day and hour
@tasks.loop(hours=1)
async def update_name():
    print(client.user.display_name)
    date = datetime.now()
    christmas_day = datetime(date.year,12,25)
    delta = christmas_day - date
    print(str(delta.days)  + " " + str(delta.seconds//3600))
    if (delta.days != 0):
        if delta.seconds//3600 >= 12:
            await client.user.edit(username = "IT'S CHRISTMAS IN {} DAYS".format(delta.days+1))
        else:
            await client.user.edit(username = "IT'S CHRISTMAS IN {} DAYS".format(delta.days))
    else:
        await client.user.edit(username = "ITS CHRISTMAS TODAY LETS GOOO")

#Command to check the days till Christmas
@bot.command()
async def christmas_date():
    for guild in client.guilds:
        channel = client.get_channel(guild.text_channels[0].id)
        await channel.send(client.user.display_name)

load_dotenv()
access_token= os.environ["ACCESS_TOKEN"]
client.run(access_token)
