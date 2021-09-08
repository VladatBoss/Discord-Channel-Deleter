import discord
from discord.ext import commands, tasks
from itertools import cycle
from colorama import Fore, Style
from discord import Permissions

# uptimerobot.com
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Channel deleter is ready!!"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

token = '' # put your token here
client = commands.Bot(command_prefix = '!')
status = cycle(['Made By 𝔖𝔬𝔠𝔦𝔞𝔩 ≯͒̅ ErenYeager#6969','!delete to delete channels'])

@client.event
async def on_ready():
  change_status.start()
  print("Channel deleter is ready!!")

@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def ping(ctx):
    await ctx.send('Pong! My latency is {0}ms'.format(round(client.latency, 1)))

@client.command()
async def delete(ctx):
  await ctx.channel.send("channels are getting deleted.")
  guild = ctx.guild
  for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)

keep_alive()

client.run(token)
