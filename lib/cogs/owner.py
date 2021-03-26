import discord
import os
import asyncio
from datetime import *
from discord.ext.commands import *
from discord.ext.commands.cooldowns import *
from discord.ext import *


class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # SHUTDOWN COMMAND -------------------------------------------------------------------------
    @command(name="shutdown")
    @is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Alright, shutting down.")
        print(f"{bcolors.print_info}{bcolors.print_success}Stopping bot.{bcolors.ENDC}")
        exit(0)  # Not a very clean way to stop, but there is a Windows bug with the module where the bot.stop and logout don't work.

    # RESTART COMMAND ---------------------------------------------------------------------------
    @command(name="restart")
    @is_owner()
    async def restart(self, ctx):
        await ctx.reply("Alright, I'm restarting.")
        try:
            await bot.close()
        finally:
            os.system("python3 launcher.py")

    # End of Cog -------------------------------------------------------------------------------------------------------------------------------
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("owner")
            # print(bcolors.print_cog + bcolors.print_spec + "Utility " + bcolors.ENDC + "cog started!")


def setup(bot):
    bot.add_cog(OwnerCog(bot))
