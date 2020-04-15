from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command(message):
    try:
        if message.author.bot:
            return
    await bot.process_commands(message)
except Exception:
    await message.channel.send(f'```\n｛traceback.format_exc()｝\n```')


@bot.command
async def ping(ctx):
    await ctx.send('pong')


    bot.command
async def neko(ctx):
    await ctx.send('にゃーん')
    

 bot.run(token)
