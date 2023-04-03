import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

# Load environment variables
load_dotenv()

# Set environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# All commands must start with '!' prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Confirm bot is connected to server
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f'{bot.user.name} is connected to:\n' 
        f'{guild.name} (id: {guild.id})'
    )
    
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

# Bot test command
@bot.command(name='sup')
async def sup(ctx):
    await ctx.send('Biip boop')

# Run bot
bot.run(TOKEN)