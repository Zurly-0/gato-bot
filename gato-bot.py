import discord
from discord.ext.commands import Bot
from discord import Webhook
from discord.ext import commands
import time
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")

client = discord.Client()
b = Bot = commands.Bot(
command_prefix = '!',
activity = discord.Activity(type=discord.ActivityType.watching, name="github.com/64x2/gato-bot-public")
)


@b.event
async def on_ready():
    print("  ________        __        __________        __    ")
    print(" /  _____/_____ _/  |_  ____\______   \ _____/  |_  ")
    print("/   \  ___\__  \\   __\/  _ \|    |  _//  _ \   __\ ")
    print("\    \_\  \/ __ \|  | (  <_> )    |   (  <_> )  |   ")
    print(" \______  (____  /__|  \____/|______  /\____/|__|   ")
    print("        \/     \/                   \/              ")
    print("")
    print("GatoBot Public by Xofo. Avaliable at github.com/64x2/gato-bot-public")

@b.command()
async def debug(ctx, arg):
    await ctx.send(arg)
    print("The command 'Debug' was just used (This command will be removed in stable releases)")

@b.command(pass_context=True)
async def ping(ctx):
    time_1 = time.perf_counter()
    await ctx.trigger_typing()
    time_2 = time.perf_counter()
    ping = round((time_2-time_1)*1000)
    await ctx.send(f"Pong! Gato-bot currently has a ping of {ping}ms")

@b.command()
async def version(ctx):
    embed=discord.Embed(title="Gato-bot.py Beta 5", url="https://github.com/64x2/gato-bot-public", description="Gato-bot.py is property of Xofo LLC. Unauthorized use and/or abuse of Xofo LLC property isn't nice :(", color=800080)
    await ctx.send(embed=embed)
    print("Command Version was used")

b.run(TOKEN, bot = True)
