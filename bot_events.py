import random

from constants import *


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if random.randint(1, get_constants()['CHANCE']) == 1:
        if get_constants()["MESSAGE_ANSWER"] and \
                (message.content[0:len(get_constants()["PREFIX"])] != get_constants()["PREFIX"]):
            if (not get_constants()["AVAILABLE_CHANNELS"]) or ('<#' + str(message.channel.id) + '>') \
                    in get_constants()["AVAILABLE_CHANNELS"]:
                msg = ''
                for _ in range(3):
                    with open("words.json", "r", encoding='utf-8') as f:
                        data = json.load(f)
                        words = data["words"]
                        msg += random.choice(words) + ' '
                for word in message.content.split():
                    if word != '"' and word[0:2] != '<@' and (word not in words):
                        words.append(word)

                with open("words.json", "w", encoding='utf-8') as f:
                    json.dump({"words": words}, f, ensure_ascii=False)

                await message.channel.send(msg[0:-1])
    await bot.process_commands(message)
