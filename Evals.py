import discord
from discord.ext import commands
import sys, traceback

TOKEN = 'NDQ3ODM2NzA4Nzc2NzA2MDQ4.Dj6FYA.FtaZNqK4m_PaqyN5mH4xu-sgbTw'

def get_prefix(bot, message):
    prefixes = ['$']
    if not message.guild:
        return '$'
    return commands.when_mentioned_or(*prefixes)(bot, message)

initial_extensions = ['cogs.owner','cogs.members']

bot = commands.Bot(command_prefix=get_prefix, description='Evals 2.0 by Edilab')

activity = discord.Game(name="$info")

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(status=discord.Status.online, activity=activity)
print('------')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('Prefix : $')
    await bot.process_commands(message)
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        return await ctx.send(':warning: You do not own this bot !')

bot.run(TOKEN, bot=True, reconnect=True)
