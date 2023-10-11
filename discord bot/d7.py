import discord
import asyncio
from discord.ext import commands
client = discord.Client()

bot = commands.Bot(command_prefix='/')

@bot.command()
async def embed(ctx):
   embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=discord.Color.blue())
   embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)
   embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
   embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False)
   embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
   embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)
   embed.add_field(name="Field 4 Title", value="It is inline with Field 2", inline=True)
   embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
   await ctx.send(embed=embed)

bot.run('ODIwOTc2MDYwMzYyNjUzNzI2.YE8_iQ.hwdTZEZdu_bun6DBYaEYQNiP8Lc')