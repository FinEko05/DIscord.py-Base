from config import *

#example cog

class example_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Hello World!")

def setup(bot):
    bot.add_cog(example_cog(bot))
