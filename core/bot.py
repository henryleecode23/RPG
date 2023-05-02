from lib import *
from lib.keep_alive import keep_alive

import discord
from discord.ext import commands
from dotenv import load_dotenv
from pymongo import MongoClient
import os
from datetime import datetime


load_dotenv()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(debug_guilds=[967615452341739621], command_prefix=';', intents=discord.Intents.all(), help_command=None)
        self.config = get_config("./config.json")
        self.load_extension("cogs.Basic.Basic")
        self.cogs_list = find_cogs("./cogs")
        self.cogs_list.remove("cogs.Basic.Basic")
        for cog in self.config["disabled_cogs"]:
            try:
                self.cogs_list.remove(cog)
            except:
                pass
        for cog in self.cogs_list:
            self.load_extension(cog)
        self.database = MongoClient(os.getenv("MONGODB_URI")).RPG_database
        self.run_time = datetime.now()
        keep_alive()
