# bot/route.py
from .common import bot
from web.search import search_with_location_and_budget
from .gemini import get_gemini_response
from web.main_scrap import Main


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
    bot.send_message(chat_id, "Enter your desired location:")
    
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
        main = Main(user_data[6461380860]['location'],user_data[6461380860]['step'])
        main.findList()

    elif user_info['step'] == 'budget':
        # Save the budget and perform the search
        user_info['budget'] = message.text
        location = user_info['location']
        budget = user_info['budget']
        loader_message = bot.send_message(chat_id, "Processing your request, please wait...")
        # Perform the search using the provided location and budget
        data = 'find listing of houses in'+ location+ 'under' +budget+'cad'
        search_results = get_gemini_response(data)
        # use below function for web scrap
        # search_results = search_with_location_and_budget(location=location, budget=budget)
        bot.delete_message(chat_id,loader_message.id)

        if search_results:
            bot.send_message(chat_id, search_results)
        else:
            bot.send_message(chat_id, "No data found.")

        # Reset the user state
        user_data.pop(chat_id)

# # handle other messages
# @bot.message_handler(func=lambda message: message.chat.id not in user_data)
# def handle_other_messages(message):
#     chat_id = message.chat.id
#     user_message = message.text
#     loader_message = bot.send_message(chat_id, "Processing your request, please wait...")
#     # Get a response from Gemini AI
#     gemini_response = get_gemini_response(user_message)
#     # Send the Gemini AI response back to the user
#     bot.send_message(chat_id, gemini_response)
#     bot.delete_message(chat_id,loader_message.id)