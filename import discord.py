from distutils.cmd import Command
from imaplib import Commands
import discord
from discord import SlashCommand

bot= Commands.Bot (Command_prefix="G", description="Bot InfomaGreen")
slash= SlashCommand(bot, sync_command = True)
@bot.event
async def on_ready():
    print("Bot prêt")

token=("OTA5MDYyNTA1ODc4Mzg4Nzg2.Gl3gBi.P3Ic8neFNaGeCSmfIXeg_LtKsYflUyIemtucxg")

bot.run(token)