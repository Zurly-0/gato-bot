import discord
from discord.ext.commands import Bot
from discord import Webhook
from discord.ext import commands
import time

# Put your discord bot's token here (You can get it from discord.com/developers/applications/)
TOKEN = "Token Here"

client = discord.Client()
b = Bot = commands.Bot(
command_prefix = '!',
activity = discord.Activity(type=discord.ActivityType.watching, name="github.com/64x2/gato-bot")
)


@b.event
async def on_ready():
    channel = b.get_channel(974317715563089920) # This is for debug purposes, if you are going to use this, change the channel ID to your own :)
    await channel.send("Gato-bot started up! :cat2:")
    time.sleep(0.5)
    await channel.send("Hope you day or night is going well! You can check my commands with `!help` and check the current version with `!verison`")
    time.sleep(0.5)
    await channel.send("Remember to star the repository if you enjoy (https://github.com/64x2/gato-bot)")
    time.sleep(0.5)
    print("Gato-bot.py has started up on the frontend! Enjoy the bot :^)")

@b.command()
async def debug(ctx, arg):
    await ctx.send(arg)
    print("The command 'Debug' was just used for testing purposes!")


@b.command()
async def version(ctx):
    embed=discord.Embed(title="Gato-bot.py Beta 2", url="https://soundcloud.com/aprilboyy", description="Gato-bot.py is property of Xofo LLC. Unauthorized use and/or abuse of Xofo LLC property isn't nice :(", color=800080)
    await ctx.send(embed=embed)
    print("Command Version was used")

b.run(TOKEN, bot = True)
