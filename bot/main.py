# add commands 
# bot/main.py
from .common import bot
from .commands import *
def runBot():
    print("Bot is running...")
    bot.polling()  # Start polling to listen for messages

    
