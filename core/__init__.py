from discord import Cog
from discord.ext import commands

class CogBase(Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot