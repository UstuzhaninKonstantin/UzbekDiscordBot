import discord
import logging
import random
import json
from discord.ext import commands
from constants import TOKEN, PREFIX, MESSAGE_ANSWER, AVAIABLE_CHANNELS

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.command(name='channel_id')
async def get_channel_id(ctx, channel):
    await ctx.send(channel[2:-1])


@bot.command(name='answer')
@commands.is_owner()
async def answers_on(ctx, status):
    if status == 'on':
        MESSAGE_ANSWER = True
        await ctx.send('Ответы на сообщения включены.')
    elif status == 'off':
        MESSAGE_ANSWER = False
        await ctx.send('Ответы на сообщения выключены.')


@bot.command(name='length')
async def number_of_words(ctx):
    with open("words.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    await ctx.send(len(data["words"]))


@bot.command(name='channel')
async def channels_action(ctx, action, id=123):
    if action == 'add':
        AVAIABLE_CHANNELS.append(id)
        await ctx.send(f'Теперь бот будет говорить в канале {"<#" + str(id) + ">"}')
    elif action == 'remove':
        try:
            AVAIABLE_CHANNELS.remove(id)
            await ctx.send(f'Бот не будет говорить в канале {"<#" + str(id) + ">"}')
        except Exception:
            pass
    elif action == 'show':
        if not AVAIABLE_CHANNELS:
            await ctx.send('Все каналы доступны')
        else:
            await ctx.send(', '. join(list(map(lambda x: '<#' + x + '>' + AVAIABLE_CHANNELS))))
    elif action == 'clear':
        AVAIABLE_CHANNELS.clear()
        await ctx.send('Бот будет говорить во всех каналах')



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if MESSAGE_ANSWER and (message.content[0:len(PREFIX)] != PREFIX):
        if message.channel.id in AVAIABLE_CHANNELS or not AVAIABLE_CHANNELS:
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
                if word != '"' and word[0:2] != '<@' and (word not in words):
                    words.append(word)

            with open("words.json", "w", encoding='utf-8') as f:
                json.dump({"words": words}, f, ensure_ascii=False)

            await message.channel.send(msg[0:-1])
    await bot.process_commands(message)


intents = discord.Intents.default()
intents.members = True
bot.run(TOKEN)