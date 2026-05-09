import discord
from discord.ext import commands

TOKEN = input("Please enter your Discord bot token: ")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command(name='level')
async def level(ctx):
    await ctx.send(f'Type this command every day for you to get the badge')

bot.run(TOKEN)
