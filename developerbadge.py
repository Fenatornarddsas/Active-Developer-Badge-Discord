
import discord
from discord.ext import commands

TOKEN = 'Put_Your_Token_Here'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command(name='level')
async def level(ctx):
    await ctx.send(f'Type this command everyday so you can get the badge')

bot.run(TOKEN)
