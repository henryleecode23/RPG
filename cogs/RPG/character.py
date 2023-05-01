from core import CogBase
from lib import is_player_exist, save_player, kill_player, get_player

from RPG.core import Character
import discord
from discord import SlashCommandGroup
from discord.ext import commands

class CharacterCog(CogBase):
    character = SlashCommandGroup(name="character", description="Character related commands")

    @character.command(name="create", description="Create a character")
    async def character_create(self, ctx: discord.ApplicationContext):
        if (is_player_exist(ctx.author.id, self.bot.database)):
            await ctx.respond("You already have a character", ephemeral=True)
            return
        character = Character.random_create(id=ctx.author.id, name=ctx.author.name)
        embed = discord.Embed(title="Here is your character", color=0x57e389)
        embed.add_field(name="HP", value=f"{character.HP}/{character.MAX_HP}", inline=True)
        embed.add_field(name="MP", value=f"{character.MP}/{character.MAX_MP}", inline=True)
        embed.add_field(name="屬性", value=
                        f"STR: {character.STR}\n \
                        DEX: {character.DEX}\n \
                        CON: {character.CON}\n \
                        INT: {character.INT}\n \
                        WIS: {character.WIS}\n \
                        CHA: {character.CHA}",
                        inline=False)
        embed.set_thumbnail(url=ctx.author.display_avatar.url)
        await ctx.respond(embed=embed, ephemeral=True)
        save_player(character, self.bot.database)

    @character.command(name="status", description="Show your character status")
    async def character_status(self, ctx: discord.ApplicationContext):
        data = get_player(ctx.author.id, self.bot.database)
        if data is None:
            await ctx.respond("You don't have a character. Try to create one!", ephemeral=True)
            return
        character = Character.create_from_dict(data)
        embed=discord.Embed(title=ctx.author.name, description=ctx.author.mention, color=0x57e389)
        embed.add_field(name="HP", value=f"{character.HP}/{character.MAX_HP}", inline=True)
        embed.add_field(name="MP", value=f"{character.MP}/{character.MAX_MP}", inline=True)
        embed.add_field(name="屬性", value=
                        f"STR: {character.STR}\n \
                        DEX: {character.DEX}\n \
                        CON: {character.CON}\n \
                        INT: {character.INT}\n \
                        WIS: {character.WIS}\n \
                        CHA: {character.CHA}",
                        inline=False)
        embed.set_thumbnail(url=ctx.author.display_avatar.url)
        await ctx.respond(embed=embed, ephemeral=True)

    @character.command(name="kill", description="Kill your character")
    async def character_kill(self, ctx: discord.ApplicationContext):
        if (not is_player_exist(ctx.author.id, self.bot.database)):
            await ctx.respond("You don't have a character. Try to create one!", ephemeral=True)
            return
        kill_player(ctx.author.id, self.bot.database)
        await ctx.respond("Your character is killed", ephemeral=True)

    @character.command(name="show", description="Show your character status on public")
    async def character_show(self, ctx: discord.ApplicationContext):
        data = get_player(ctx.author.id, self.bot.database)
        if data is None:
            await ctx.respond("You don't have a character. Try to create one!", ephemeral=True)
            return
        character = Character.create_from_dict(data)
        embed=discord.Embed(title=ctx.author.name, description=ctx.author.mention, color=0x57e389)
        embed.add_field(name="HP", value=f"{character.HP}/{character.MAX_HP}", inline=True)
        embed.add_field(name="MP", value=f"{character.MP}/{character.MAX_MP}", inline=True)
        embed.add_field(name="屬性", value=
                        f"STR: {character.STR}\n \
                        DEX: {character.DEX}\n \
                        CON: {character.CON}\n \
                        INT: {character.INT}\n \
                        WIS: {character.WIS}\n \
                        CHA: {character.CHA}",
                        inline=False)
        embed.set_thumbnail(url=ctx.author.display_avatar.url)
        await ctx.respond(embed=embed)
        

def setup(bot: commands.Bot):
    bot.add_cog(CharacterCog(bot))
