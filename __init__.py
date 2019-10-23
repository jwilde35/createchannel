from .createchannel import createchannel

def setup(bot):
    bot.add_cog(createchannel(bot))
