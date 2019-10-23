from .createchannel import CreateChannel

def setup(bot):
    bot.add_cog(CreateChannel(bot))
