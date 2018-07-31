import discord
from discord.ext import commands

class Members:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='add')
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a + b)
    
    @commands.command(name='ping')
    async def ping(self, ctx):
        latency = int(ctx.bot.latency * 1000)
        em = discord.Embed(color=discord.Color.green())
        em.description = f'Pong :ping_pong: ({latency} ms)'
        await ctx.send(embed=em)
    
    @commands.command(name='profile')
    async def profile(self, ctx, user : discord.Member):
        embed = discord.Embed(title="{}'s profile".format(user.name), description="Here's what I know :")
        embed.colour = user.colour
        embed.add_field(name = "Name", value = user.name, inline = True)
        embed.add_field(name = "ID", value = user.id, inline = True)
        embed.add_field(name = "Status", value = user.status, inline = True)
        embed.add_field(name = "Highest role", value = user.top_role)
        embed.add_field(name = "Joined", value = user.joined_at)
        embed.set_thumbnail(url = user.avatar_url)
        await ctx.send(embed = embed)

    @commands.command(name='info')
    async def info(self, ctx):
        embed = discord.Embed(title=self.bot.user.name, description="Here we go !")
        embed.colour = discord.Colour(0x7289da)
        embed.add_field(name = "Status", value = ctx.me.status, inline = True)
        embed.add_field(name = "ID", value = self.bot.user.id, inline = True)
        embed.add_field(name = "Commands", value = "Type $help for a list of all commands")
        embed.set_thumbnail(url = self.bot.user.avatar_url)
        embed.set_footer(text="v2.0 by Edilab", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        await ctx.send(embed = embed)
                 
def setup(bot):
    bot.add_cog(Members(bot))
