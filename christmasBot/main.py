import discord
from discord.ext import commands

intents = discord.Intents.default()

intents = discord.Intents.default()
intents.messages = True  # Um auf Nachrichten in Channels reagieren zu können
intents.message_content = True  # Um den Inhalt von Nachrichten lesen zu können (wichtig für Befehle)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ist bereit! Eingeloggt als {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')
    
@bot.command()
async def christmas(ctx):
    treeline = ""
    treesize = 11
    spacing = treesize
    for i in range(0, treesize, 2):
        # print("i ist nun: " + str(i))
        treeline = ""
        for x in range(int((treesize - 1 - i) / 2)):
            treeline += "❤️"
        
        for x in range(int(i + 1)):
            treeline += "💚"
        
        for x in range(int((treesize - 1 - i) / 2)):
            treeline += "❤️"
        print(treeline)
        await ctx.send(treeline)
        # treesize = treesize - 2
            
    

# Token hier einfügen
bot.run('TOKEN')
