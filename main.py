import discord
import logging
import random
import json
from discord.ext import commands
from constants import TOKEN

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True

prefix = 'u!'

bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command(name='length')
async def number_of_words(ctx):
    with open("words.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    await ctx.send(len(data["words"]))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    msg = ''
    for _ in range(3):
        with open("words.json", "r", encoding='utf-8') as f:
            data = json.load(f)
            words = data["words"]
            msg += random.choice(words) + ' '

    with open("words.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        words = data["words"]

    for word in message.content.split():
        if word != '"' and word[0:len(prefix)] != prefix and (word not in words):
            words.append(word)

    with open("words.json", "w", encoding='utf-8') as f:
        json.dump({"words": words}, f, ensure_ascii=False)

    await message.channel.send(msg[0:-1])
    await bot.process_commands(message)


intents = discord.Intents.default()
intents.members = True
bot.run(TOKEN)