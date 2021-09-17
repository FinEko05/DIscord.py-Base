from config import *

#example cog

class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test!")

def setup(bot):
    bot.add_cog(Cog(bot))
