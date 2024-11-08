# bot/route.py
from .common import bot
from web.search import search_with_location_and_budget
from .gemini import get_gemini_response
from web.main_scrap import Main
from web.db import Select


# Dictionary to keep track of user state
user_data = {}

# Step 1: Handle '/start' command
@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    welcome_message = (
        "Welcome to the Bot! 🤖\n"
        "I can help you search for information based on your location and budget.\n"
        "Use the /search command to get started. or you ask any question to me"
    )
    bot.send_message(chat_id, welcome_message)

# Step 1: Handle '/search' command
@bot.message_handler(commands=['search'])
def handle_search(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Enter your desired Province:")
    
    # Initialize user state to capture location first
    user_data[chat_id] = {'step': 'location'}

# Step 2: Handle user responses
@bot.message_handler(func=lambda message: message.chat.id in user_data)
def handle_user_input(message):
    chat_id = message.chat.id
    user_info = user_data.get(chat_id)

    if user_info['step'] == 'location':
        # Save location and ask for the budget
        user_info['location'] = message.text
        bot.send_message(chat_id, "Enter your budget:")
        user_info['step'] = 'budget'

    elif user_info['step'] == 'budget':
        # Save the budget and perform the search
        user_info['budget'] = message.text

        bot.send_message(chat_id, "Enter your desired city:")
        user_info['step'] = 'city'

    
    elif user_info['step'] == 'city':
        # Save the budget and perform the search
        user_info['city'] = message.text

        print(user_data)

        main = Main(user_data[chat_id]['location'],user_data[chat_id]['budget'],user_data[chat_id]['city'])
        main.findList()

        # Reset the user state
        user_data.pop(chat_id)
        select = Select
        for item in select.select():
            bot.send_message(chat_id, item)
