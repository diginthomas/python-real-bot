from telebot import TeleBot
from dotenv import load_dotenv
import os
load_dotenv()

bot_token = os.environ['BOT_API']

bot = TeleBot(bot_token)