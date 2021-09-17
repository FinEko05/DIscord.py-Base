

#it's better to write import in one file then import that file to every file rather than importing everything to every file.

from os import system
import discord, os, youtube_dl
from currency_converter import CurrencyConverter
from discord.ext import commands

prefix = "." # prefix before commands

embed_color = discord.Color.red() # Embed color for messages and such
game_playing = "Wee woo Wee Woo" # Bot's game activity





#
# Bot_token = "" <- your token this is only for repl it
#
bot_token = os.environ['Bot_token_key_thingy'] 
#
#
