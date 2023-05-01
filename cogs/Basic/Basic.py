from core import CogBase
from core.check import is_owner
from lib import find_cogs

import discord
from discord.ext import commands

class BasicCog(CogBase):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong. (bot latency: {round(self.bot.latency * 1000)}ms)')
        return
    
    @commands.command()
    @commands.check(is_owner)
    async def reload(self, ctx: commands.Context):
        errorCount = 0
        errorMsg = []
        for cog in self.bot.cogs_list:
            try:
                self.bot.reload_extension(cog)
            except Exception as e:
                print(f"Error: {e}")
                errorCount += 1
                errorMsg.append(f"{e}")
        await ctx.reply(f"{len(self.bot.cogs_list)-errorCount} cogs reload complete, {errorCount} error happened.",)
        if errorCount > 0:
            await ctx.reply(f"Error: {errorMsg}")
        return

    @commands.command()
    @commands.check(is_owner)
    async def load(self, ctx: commands.Context, cog:str):
        errorCount = 0
        errorMsg = []
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            print(f"Error: {e}")
            errorCount += 1
            errorMsg.append(f"{e}")
        await ctx.reply('Load completed.')
        if errorCount > 0:
            await ctx.reply(f"Error: {errorMsg}")
        return
    
    @commands.command()
    @commands.check(is_owner)
    async def unload(self, ctx: commands.Context, cog:str):
        errorCount = 0
        errorMsg = []
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            print(f"Error: {e}")
            errorCount += 1
            errorMsg.append(f"{e}")
        await ctx.reply('Unload completed.', ephemeral=True)
        if errorCount > 0:
            await ctx.reply(f"Error: {errorMsg}")
        return
    
    @commands.command()
    @commands.check(is_owner)
    async def show_cogs(self, ctx: commands.Context):
        await ctx.send([cog for cog in find_cogs("./cogs")])
        return
    
    @commands.command()
    @commands.check(is_owner)
    async def show_using_cogs(self, ctx: commands.Context):
        await ctx.send([cog for cog in self.bot.cogs])
        return

    @discord.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user.name}")
        await self.bot.get_channel(self.bot.config["bot_info_channel"]).send(f"{self.bot.user.name} is online.")
        return
    
    @commands.command()
    async def info(self, ctx: commands.Context):
        embed = discord.Embed(title="Bot info", color=0xcadc35)
        embed.add_field(name="已執行時間", value=f"<t:{int(self.bot.run_time.timestamp())}:R>", inline=False)
        embed.add_field(name="Loaded Cogs", value=[cog for cog in self.bot.cogs], inline=False)
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(BasicCog(bot))
