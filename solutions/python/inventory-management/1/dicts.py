# from collections import Counter # Cheat
"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    
    # return Counter(items) # Cheat
    counts = {}
    for word in items:
        counts[word] = counts.get(word, 0) + 1
    return counts

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    # return Counter(inventory)+Counter(items) # Cheat
    for item, count in create_inventory(items).items():
        inventory[item] = inventory.get(item, 0) + count
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """
    for item in items:
        if item in inventory.keys():
            if inventory.get(item) - 1 >= 0:
                inventory[item] = inventory.get(item) - 1
            else:
                inventory[item] = 0
    return inventory
        

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    try:
        del inventory[item]
        return inventory
    except:
        return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """

    return [(k, v) for k, v in inventory.items() if v != 0]
