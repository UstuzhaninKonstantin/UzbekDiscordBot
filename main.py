import logging
import random
import json

import discord
from discord.ext import commands

from constants import *
from bot_commands import *
from bot_events import *

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
intents = discord.Intents.default()
intents.members = True
bot.run(get_constants()['TOKEN'])
