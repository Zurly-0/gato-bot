import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

# Put your discord bot's token here (You can get it from discord.com/developers/applications/)
TOKEN = "TOKEN HERE"

client = discord.Client()
b = Bot(command_prefix = "!", self_bot=False)
b.remove_command("help")

@b.command()
async def message(ctx, user:discord.Member, *, message=None):
    await user.send("This is a test command, if you recieved this message, then hi :cat2:")
    print("Message command was used on "+user.name+"#"+user.discriminator)

@b.command()
async def version(ctx):
    embed=discord.Embed(title="Gato-bot.py Alpha 2", url="https://cdn.discordapp.com/avatars/471386638984151042/fca27b6741fb03c80a0a34034a9ba44f.png", description="Gato-bot.py is property of Xofo LLC. Unauthorized use and/or abuse of Xofo LLC property isn't nice :(", color=800080)
    await ctx.send(embed=embed)
    print("Command Version was used")

b.run(TOKEN, bot = True)
