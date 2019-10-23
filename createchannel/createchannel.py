from redbot.core import commands
from redbot.core import checks
from redbot.core import Config
import os
import time

BaseCog = getattr(commands, "Cog", object)

class CreateChannel(BaseCog):
    def __init__(self, bot):
        self.bot = bot
    @commands.group(pass_context=True)
    @checks.is_owner()
    async def create(self, ctx):
        pass

    @create.command(name="channel", pass_context=True, no_pm=True)
    async def _channel(self, ctx, name : str):
        guild = ctx.message.guild
        await guild.create_text_channel(name)
        await ctx.send("done")
