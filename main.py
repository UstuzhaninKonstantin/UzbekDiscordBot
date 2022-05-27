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

bot = commands.Bot(command_prefix='u!', intents=intents)



@bot.command(name='length')
async def len_of_words(ctx):
    with open("words.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    await ctx.send(len(data["words"]))


class BotClient(discord.Client):
    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'u!length':
            with open("words.json", "r", encoding='utf-8') as f:
                data = json.load(f)
            await message.channel.send(len(data["words"]))
        else:
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
                if word != '"' and word[0:2] != 'u!' and (word not in words):
                    words.append(word)

            with open("words.json", "w", encoding='utf-8') as f:
                json.dump({"words": words}, f, ensure_ascii=False)

            await message.channel.send(msg[0:-1])


intents = discord.Intents.default()
intents.members = True
client = BotClient(intents=intents)
client.run(TOKEN)
