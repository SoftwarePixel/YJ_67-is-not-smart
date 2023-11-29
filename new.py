# CHANGE THE STUFF BELOW
server_id = 00000000
bot_token = "PUT TOKEN HERE"


import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=None, intents=intents)
@bot.event
async def on_ready():
    guild = bot.get_guild(server_id)
    print("Sending Messages")
    while True:
        for channel in guild.text_channels:
            shit_to_spam = "@everyone \n"
            for x in range(10):
                shit_to_spam = shit_to_spam + "@everyone \n"
            await channel.send(shit_to_spam)
bot.run(bot_token)