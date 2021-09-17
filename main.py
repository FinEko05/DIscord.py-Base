from config import *
bot = commands.Bot(command_prefix='.', help_command=None)

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    try:
      bot.load_extension(f'cogs.{filename[:-3]}')
      print(f"{filename} succesfully loaded")
    except:
      print(f"Exception in {filename} unable to load_extension()")
  else:
    if filename != "__pycache__":
      print(f'{filename[:-3]} Not an .py file')

@bot.event
async def on_ready():
    print(f"\nBot {bot.user} Online!")
  
bot.run(bot_token)
