import discord
from discord.ext import commands
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command
# working but incorrectly
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#
#    if message.content.startswith('#add'):
#        fout = message.content
#        fout = fout.split(' ', 1)
#        #fout = 'you added ' , fout  , ' you stupid bitch!'
#        await message.channel.send(fout)
#
#    if message.content.startswith('#show list'):
#        await message.channel.send('you asked for the movie list you stupid bitch!') 
#
#    if message.content.startswith('#penis'):
#        await message.channel.send('oh no! our stupid bitch! its broken!')
#
#    if message.content.startswith('#whatsyourname'):
#        await message.channel.send('Ethan you stupid bitch!')
#

client.run(os.getenv('TOKEN'))