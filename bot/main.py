import discord
from discord.ext import commands, tasks
from utils.constants import token
import os
import asyncio
import aiohttp


class Misfit(commands.Bot):
    def __init__(self, command_prefix):
        self.command_prefix = command_prefix
        super().__init__(command_prefix=command_prefix, intents=discord.Intents.all())

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        guild = self.get_guild(997483421255340092)
        channel = guild.get_channel(1126822610903244891)
        await load()

        await channel.send(
            f"Misfit is online | Guilds: {len(self.guilds)} | Users: {len(self.users)}"
        )


bot = Misfit(command_prefix="m!")


async def load():
    for fn in os.listdir("bot/cogs"):
        if fn.endswith(".py"):
            await bot.load_extension(f"cogs.{fn[:-3]}")
    # return len(os.listdir('bot/cogs'))

@bot.event
async def on_message(message: discord.Message):
    if str(message.author.id) == '821312314246561813':
        if message.content[0] == '!':
            await message.reply('No commands for u')
            return
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if message.content.lower() == 'misfit marry keio':
        await message.channel.send('No Never')
    if message.content.lower() == 'meow':
        await message.reply("Meow")
@bot.command()
async def sync(ctx):
    await ctx.send("Syncing Slash Commands")
    synced = await bot.tree.sync()
    if len(synced) > 0:
        for cmd in synced:
            await ctx.send(f"Synced {cmd}")
        await ctx.send(f"Synced {len(synced)} Commands Globally!")
    else:
        await ctx.send("No Slash Commands to Register.")


@bot.hybrid_command(name="shutdown")
async def shutdown(ctx):
    if str(ctx.author.id) != "1035439449070383106":
        await ctx.send("Owner only Command")
        return
    await ctx.send("Going to sleep")
    await bot.close()


def main():
    bot.run(token)


if __name__ == "__main__":
    main()
