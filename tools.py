from langchain_core.tools import tool

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

tools = [add_to_shopping_list, show_shopping_list,greeting]
