import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import random
import json
import sys
import subprocess
import platform
import datetime
import sys
import logging
import traceback

# I keep anything like game status, dnd , def etc


def process_message(message):
    args = message.content.split(" ")
 
    return args
Client = discord.Client()
bot = commands.Bot(command_prefix = "*")



def process_message(message):
    args = message.content.split(" ")
 
    return args

@client.event

async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('--------')
    print('You are running Yui Funami v1.1')
    print("Created by Yuriii6969 and Tiln#0416")
    return await client.change_presence(game=discord.Game(name='with my smart developer ;p;',status=discord.Status("dnd"))) 
#Here i have put commands that don't require the commad prefix (*)... Editable i guess  

@bot.event
async def on_message(message):
    if message.content == "gay":
        await bot.send_message(message.channel,"gay to you too")
    if message.content == "pansexual":
        await bot.send_message(message.channel,"i'm a pan. They cook eggs on me. Sexually, of course")
    if message.content == "lesbian":
        await bot.send_message(message.channel,"lesbian...lesbeannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn. No?? okay then :<")
    if message.content == "asexual":
        await client.send_message(message.channel,"asexual uh...assexual")
    if message.content == "qwertyuiopsexual":
        await client.send_message(message.channel,"Stop, just stop.")
    if message.content == "demisexual":
        await client.send_message(message.channel,";-;")
    if message.content == "ayy":
        await client.send_message(message.channel,"lmao")


# Some compusary commands that will not help in ANY way or form...

    if message.content.upper().startswith('*GAY'):
        await client.send_message(message.channel, 'Who is gay?? Type *name _namehere_')

        def check(message):
            return message.content.upper().startswith('*NAME')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('*name'):].strip()
        await client.send_message(message.channel, '{} is gay indeed'.format(name))

    if message.content.upper().startswith('*PING'):
        await client.send_message(message.channel,'{:.2f}ms'.format(client.latency * 1000))


    if message.content.upper().startswith('*PONG'):
        userID = message.author.id
        await client.send_message(message.channel, '<@%s> ping :)'%(userID))
        
    if message.content.upper().startswith("*HELLO"):
        await client.send_message(message.channel, "henlo")
        
    if message.content.upper().startswith("*ROAST"):
        userID = message.author.id
        await client.send_message(message.channel,"roasting ur children for you <@%s>"%(userID))
    
    if message.content.startswith("*echo".casefold()):
        client.send_message(message.channel, "You said: {}".format(message.content.lstrip("*echo ")))

    if message.content.upper().startswith("*DING"):
        userID = message.author.id
        await client.send_message(message.channel,"dong <@%s>"%(userID))

    if message.content.upper().startswith("*DONG"):
        userID = message.author.id
        await client.send_message(message.channel,"There is no door that goes dong, <@%s>"%(userID))

    if message.content.upper().startswith("*INVITE"):
        userID = message.author
        await client.send_message(message.channel,"``` To invite Yui to your server, use https://discordapp.com/api/oauth2/authorize?client_id=456910763504697363&permissions=8&scope=bot (Hey, we're still learning embeds,k)```")

    else: pass

@client.remove_command('help')

@client.command(pass_context=True)
async def help(ctx):
    com = ctx.message.content.lower().split("")
    base = False
    if len(com)>1:
        c=com[1]
        if c=="commandname":
            await client.say("```/commandname```")

        elif c== "othercommand":
            await client.say("```/othercommand```")

        else: base= True
        s = ""
        if base:
            s = "/help [command] for help on that command```"
            await client.say(s)



    
            
#I might put really unnessasary things here like the bee movie script, so don't freak lmao



        
client.run("token")
