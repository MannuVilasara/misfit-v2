import requests
from discord.ext import commands
import discord


class Static(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="fox")
    async def fox(self, ctx):
        image = requests.get("https://randomfox.ca/floof/").json()["image"]
        embed = discord.Embed()
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name="waifu")
    async def waifu(self, ctx):
        resp = requests.get("https://nekos.best/api/v2/waifu")
        data = resp.json()
        embed = discord.Embed()
        embed.set_image(url=data["results"][0]["url"])
        await ctx.send(embed=embed)

    @commands.hybrid_command(name="kitsune")
    async def kitsune(self, ctx):
        resp = requests.get("https://nekos.best/api/v2/kitsune")
        data = resp.json()
        embed = discord.Embed()
        embed.set_image(url=data["results"][0]["url"])
        await ctx.send(embed=embed)

    @commands.hybrid_command(name="neko")
    async def neko(self, ctx):
        resp = requests.get("https://nekos.best/api/v2/neko")
        data = resp.json()
        embed = discord.Embed()
        embed.set_image(url=data["results"][0]["url"])
        await ctx.send(embed=embed)

    @commands.hybrid_command(name="stuff")
    async def stuff(self, ctx):
        await ctx.send("Working yay\n Now Create stuff u human", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Static(bot))
    print("Static is loaded")
