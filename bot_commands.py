from constants import *


@bot.command(name='channel_channel')
async def get_channel_channel(ctx, channel):
    await ctx.send(channel[2:-1])


@bot.command(name='answer')
@commands.is_owner()
async def answers_action(ctx, status):
    if status == 'on':
        change_constants('MESSAGE_ANSWER', True)
        await ctx.send('Ответы на сообщения включены.')
    elif status == 'off':
        change_constants('MESSAGE_ANSWER', False)
        await ctx.send('Ответы на сообщения выключены.')


@bot.command(name='length')
async def number_of_words(ctx):
    with open("words.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    await ctx.send(len(data["words"]))


@bot.command(name='channel')
async def channels_action(ctx, action, channel="<#123>"):
    if action == 'add':
        channels = get_constants()['AVAILABLE_CHANNELS'].append(channel)
        change_constants('AVAILABLE_CHANNELS', channels)
        await ctx.send(f'Теперь бот будет говорить в канале {channel}')
    elif action == 'remove':
        try:
            channels = get_constants()['AVAILABLE_CHANNELS'].remove(channel)
            change_constants('AVAILABLE_CHANNELS', channels)
            await ctx.send(f'Бот не будет говорить в канале {channel}')
        except Exception:
            pass
    elif action == 'show':
        if not get_constants()['AVAILABLE_CHANNELS']:
            await ctx.send('Все каналы доступны')
        else:
            await ctx.send(', '. join(list(map(lambda x: '<#' + str(x) + '>', get_constants()['AVAILABLE_CHANNELS']))))
    elif action == 'clear':
        change_constants('AVAILABLE_CHANNELS', [])
        await ctx.send('Бот будет говорить во всех каналах')


@bot.command(name='set_chance')
async def chance(ctx, value):
    try:
        if value == 0:
            raise Exception
        int(value)
        change_constants('CHANCE', (1 / value))
        await ctx.send(f'Шанс появления сообщений был изменен на {1 / value} успешно')
    except Exception:
        await ctx.send('Некоректное значение')
