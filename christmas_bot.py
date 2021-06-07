from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import discord
from discord.ext import tasks

client = discord.Client()
@client.event
async def on_ready():
    update_name_send_message.start()
    print('We have logged in as {0.user}'.format(client))

@tasks.loop(hours=24)
async def update_name_send_message():
    print(client.user.display_name)
    date = datetime.now()
    christmas_day = datetime(date.year,12,25)
    delta = christmas_day - date
    
    for guild in client.guilds:
        print(guild.text_channels)
        channel = client.get_channel(guild.text_channels[0].id)
        await channel.send("IT'S CHRISTMAS IN {} DAYS".format(delta.days))
    await client.user.edit(username = "IT'S CHRISTMAS IN {} DAYS".format(delta.days))

load_dotenv()
access_token= os.environ["ACCESS_TOKEN"]
client.run(access_token)
