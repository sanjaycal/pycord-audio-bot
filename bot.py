import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">")

@bot.event
async def on_ready():
    print("yes")

@bot.slash_command(guild_ids=[833780895093227540])
async def play(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    await ctx.send('Started playing: something')
    vc.play(discord.FFmpegPCMAudio('file.mp3'), after=lambda e: print('done', e))

@bot.slash_command(guild_ids=[833780895093227540])
async def ping(ctx):
    await ctx.send("pong")

bot.run(open("token.txt","r").read())


