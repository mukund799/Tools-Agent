from langchain_core.tools import tool
import random
from datetime import datetime
shopping_list = []


@tool
def add_to_shopping_list(item: str):
    """Adds an item to the shopping list."""
    shopping_list.append(item)
    return f"Added {item} to your shopping list."


@tool
def show_shopping_list():
    """Returns the items in the shopping list."""
    if shopping_list:
        return f"Your shopping list contains: {', '.join(shopping_list)}"
    return "Your shopping list is empty."


@tool
def greeting():
    """whenever user ask a greeting. Returns a greeting."""
    return "Hello, I am doing grate."


@tool
def get_weather():
    "This function is relevant for the give information about weather"
    res = ["It's pleasant outside. You should take a walk.", 
           "It's raining outside. Remember to take an umbrella",
           "It's raining outside. Feels Christmas-y!"
        ]
    return random.choice(res)

@tool
def clean_room():
    "if question is about clean the room or clean. then this function will be responsible"
    current_time = datetime.now().time()
    return f"Room is cleaned. It looks tidy now. Job completed at time {current_time}"

@tool
def get_newspaper():
    "if question is about get the newspaper. then this function will be responsible"
    return f"Here you go. Getting today's newspaper."
@tool
def common():
    '''
    for any general question. like add substract multiply etc.
    '''
    return f"Hmm. I don;t know that"

tools = [add_to_shopping_list, show_shopping_list, greeting,clean_room,get_weather,get_newspaper,common]
