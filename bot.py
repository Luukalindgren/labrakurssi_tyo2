# Must install discord.py, python-dotenv and openai (pip install discord.py python-dotenv openai)
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import createPicture
import random

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

    # Print server name and id
    print(
        f'{bot.user.name} is connected to:\n' 
        f'{guild.name} (id: {guild.id})'
    )
    
    # Print all members of server
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

# Bot test command
@bot.command(name='sup', help='Responds with a message')
async def sup(ctx):
    await ctx.send('Biip boop')

# Bot coinflip command
@bot.command(name='coinflip', help='Flips a coin')
async def coinflip(ctx):
    flip = random.randint(0, 100)
    if (flip < 50):
        await ctx.send('Heads')
    elif (flip == 50):
        await ctx.send('OMG it landed on the side (1 in 101 chance)')
    else: await ctx.send('Tails')

# Bot image generator command
@bot.command(name='image', help='Generates an image with text input "!image <input>"')

# Input takes multiple words
async def image(ctx, *words):
    await ctx.send('Generating image with input: '+ ' '.join(words))
    await ctx.send(createPicture.create(' '.join(words)))


# Run bot
bot.run(TOKEN)