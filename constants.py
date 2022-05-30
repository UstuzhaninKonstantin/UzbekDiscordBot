import discord
import json
from discord.ext import commands


def get_constants():
    with open('constants.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def change_constants(key, value):
    const = get_constants()
    for k in const:
        if k == key:
            const[k] = value
    with open('constants.json', 'w', encoding='utf-8') as f:
        return json.dump(const, f, ensure_ascii=False)


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=get_constants()['PREFIX'], intents=intents)
