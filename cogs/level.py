"""
General commands — available to everyone.
"""

from datetime import datetime_CAPI

import discord
import platform
import time
from discord import app_commands, Interaction
from discord.ext import commands
import json
import utils.embeds as em
import utils.level as ul


class Level(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def calculatexp(self, level: int) -> float:
        return (level / 10) ** 1.4

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Level(bot))
