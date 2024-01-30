import discord
import random, os 
from discord.ext import commands
from project import gen_pass,sampah_organik,sampah_anorganik
from project import flip_coin
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass())

@bot.command()
async def fc(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def roll(ctx, dice="1d9"):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def meme(ctx):
    gambar = random.choice(os.listdir('images'))
    with open(f'images/{gambar}','rb')as f:
        pic = discord.File(f)

    await ctx.send(file=pic)

@bot.command()
async def anime(ctx):
    gambar = random.choice(os.listdir('images1'))
    with open(f'images1/{gambar}','rb')as f:
        pic = discord.File(f)

    await ctx.send(file=pic)

@bot.command()
async def organik(ctx):
    sampah = ''
    for i in sampah_organik:
        i = i+'\n'
        sampah += i
    await ctx.send('berikut sampah organik')
    await ctx.send(sampah)

@bot.command()
async def anorganik(ctx):
    sampah = ''
    for i in sampah_anorganik:
        i = i+'\n'
        sampah1 += i
    await ctx.send('berikut sampah organik')
    await ctx.send(sampah)
