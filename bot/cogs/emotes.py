import discord
from discord.ext import commands
import requests

url = "https://nekos.best/api/v2/"


class Emotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dance(self, ctx: commands.Context):
        image = requests.get(url=url + "dance").json()["results"][0]["url"]
        embed = discord.Embed(title=f"{ctx.author} is Dancing Yay")
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx: commands.Context, member: discord.Member = None):
        if member == None:
            member: str = "Nearby User"
        image = requests.get(url=url + "pat").json()["results"][0]["url"]
        embed = discord.Embed(title=f"{ctx.author} Pat to {member}")
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def bored(self, ctx: commands.Context):
        image = requests.get(url=url + "bored").json()["results"][0]["url"]
        embed = discord.Embed(title=f"{ctx.author} is Bored")
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def blush(self, ctx: commands.Context):
        image = requests.get(url=url + "blush").json()["results"][0]["url"]
        embed = discord.Embed(title=f"{ctx.author} is blushy")
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx: commands.Context):
        image = requests.get(url=url + "cry").json()["results"][0]["url"]
        embed = discord.Embed(title=f"{ctx.author} is crying :(")
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def happy(self, ctx: commands.Context):
        image = requests.get(url=url + "happy").json()["results"][0]["url"]
        embed = discord.Embed(title=f"{ctx.author} is happy :)")
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def wave(self, ctx: commands.Context):
        image = requests.get(url=url + "wave").json()["results"][0]["url"]
        embed = discord.Embed(title=f"{ctx.author} is saying hii 👋")
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def think(self, ctx: commands.Context):
        image = requests.get(url=url + "think").json()["results"][0]["url"]
        embed = discord.Embed(title=f"{ctx.author} is thinking")
        embed.set_image(url=image)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def smile(self, ctx: commands.Context):
        image = requests.get(url=url + "smile").json()["results"][0]["url"]
        embed = discord.Embed(title=f"{ctx.author} Smiles")
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def sleep(self, ctx: commands.Context):
        image = requests.get(url=url + "sleep").json()["results"][0]["url"]
        embed = discord.Embed(title=f"{ctx.author} is Sleeping.")
        embed.set_image(url=image)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def baka(self, ctx: commands.Context):
        image = requests.get(url=url + "baka").json()["results"][0]["url"]
        embed = discord.Embed(title=f"{ctx.author} is baka.")
        embed.set_image(url=image)
        await ctx.send(embed=embed)
async def setup(bot):
    await bot.add_cog(Emotes(bot))
    print("Emotes is loaded")
