import discord,os,sys, time
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_CHANNEL = os.getenv('BOT_CHAN')

COMMAND_PREFIX = "!"
prefixLength = len(COMMAND_PREFIX)

queueingPlayersMessage = None
queuedPlayers = []

bot = discord.Client()
  
@bot.event
async def on_message(message):
    global queueingPlayersMessage

    if message.content[:prefixLength] == COMMAND_PREFIX:
        # Send message for everybody to react to
        if message.content[prefixLength:] == 'start catan':
            await message.channel.send('React to this message if you want to queue up!')
        
        # If command = start game and there is a queueingPlayersMessage
        # Start the game and set cure
        elif message.content[prefixLength:] == 'start game' and queueingPlayersMessage != None:
            queueingPlayersMessage = None  
            await message.channel.send('Starting game...')
            
            # Need to start game function from somewhere here

@bot.event
async def on_reaction_add(reaction, user):
    global queueingPlayersMessage 
    global queuedPlayers
    
    # Ignore if it is not a message sent by the bot
    if reaction.message.author.id != bot.user.id: return 
    
    # Ignore if message IS a bot message BUT not to the message players need to react to, to queue up
    if reaction.message.content != 'React to this message if you want to queue up!': return

    # Add players to queue if they aren't already
    if user not in queuedPlayers:
        queuedPlayers.append(user)
        await reaction.message.channel.send(f"{user} is playing! ")
    
    # If this is the first time a player reacted to the queue up message
    # 1. Set currentlyQueuingPlayersMessageID to message ID
    # 2. Set time for when message should expire
    if queueingPlayersMessage == None: 
        queueingPlayersMessage  = reaction.message.id 


print("**BOT_TOKEN is ", BOT_TOKEN)
print("CHANNEL bound to is ", BOT_CHANNEL)
bot.run(BOT_TOKEN)
















