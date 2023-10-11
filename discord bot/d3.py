import typing

import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='/', description="This is a Helper Bot")
@bot.command()
async def ping(ctx):
    await ctx.send("This message has a button!", view=ViewWithButton())

class ViewWithButton(discord.ui.View):
    @discord.ui.button(style=discord.ButtonStyle.blurple, label='Click Me')
    async def click_me_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Your favourite colour is')

bot.run('ODIwOTc2MDYwMzYyNjUzNzI2.YE8_iQ.hwdTZEZdu_bun6DBYaEYQNiP8Lc')