from config import *

#example cog

class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


   
    @commands.command()
    async def test(self, ctx):
        embed=discord.Embed(title="moi", description="moikka", color=(embed_color))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Cog(bot))
