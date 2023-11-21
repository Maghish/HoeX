import json
import os

# Storing paths in variables
script_dir = os.path.dirname(os.path.abspath(__file__))
inventory_json_file = os.path.abspath(os.path.join(script_dir, '../Storage/inventory.json'))
farm_json_file = os.path.abspath(os.path.join(script_dir, '../Storage/farm.json'))
items_data_json_file = os.path.abspath(os.path.join(script_dir, '../Storage/items.json'))
shop_data_json_file = os.path.abspath(os.path.join(script_dir, '../Storage/shop.json'))


# getting the data of inventory json file
async def get_inventory_data():
    with open(inventory_json_file, "r") as json_file:
        data = json.load(json_file)
    return data

# getting the data of farm json file
async def get_farm_data():
    with open(farm_json_file, "r") as json_file:
        data = json.load(json_file)
    return data

# create a user account like thing in the inventory json file
async def create_inventory(user):

    data = await get_inventory_data()

    if str(user.id) in data:
        return False
    else:
        data[str(user.id)] = {}
        data[str(user.id)]["Stats"] = {
            "Health": 100,
            "MaxHealth": 100,
            "Energy": 200,
            "MaxEnergy": 200,
            "Farming": 0,
            "Fishing": 0, 
            "Mining": 0,
            "Animals": 0,
            "Combat": 0,
        }
        data[str(user.id)]["Inventory"] = [
            {"item_name": "Axe", "item_amount": 1, "item_type": "Tool"},    
            {"item_name": "Pickaxe", "item_amount": 1, "item_type": "Tool"},    
            {"item_name": "Hoe", "item_amount": 1, "item_type": "Tool"},    
            {"item_name": "Sickle", "item_amount": 1, "item_type": "Tool"},    
        ]
        data[str(user.id)]["Money"] = {
            "Bank": 0,
            "Wallet": 100
        }

    with open(inventory_json_file, "w") as json_file:
        json.dump(data, json_file, indent=1)
    return True

async def update_money(user, amount: int = 0, mode=["Wallet", "Bank"]):
    
    # Get the inventory data as users
    users = await get_inventory_data()

    # Add the value in respective mode
    users[str(user.id)]["Money"][mode] += amount

    # Save the changes
    with open(inventory_json_file, "w") as json_file:
        json.dump(users, json_file, indent=1) 

async def make_bar(subset: int, superset: int, set1_color: str, set2_color: str):
    dash_convert = int(superset/10)
    current_dashes = int(subset/dash_convert)
    remaining_max_value = 10 - current_dashes

    current_value_display = set1_color * current_dashes
    remaining_max_value_display = set2_color * remaining_max_value

    return ("|" + current_value_display + remaining_max_value_display + "|" + " " + f"{subset}/{superset}")

async def buy(user, shop_index: int, item_index: int, item_amount: int):

    # Open the shop data json file
    with open(shop_data_json_file, "r") as json_file:
        # Load the data of the json file
        data = json.load(json_file)
        
    t1 = None # Delcare this to track if the shop exists 
    t2 = None # Delcare this to track if the item exists in the shop data
    # Declare a variable to track the current index
    index = 1
    # Iterate over the data
    for shop in data:
        # If the given argument shop_index and the current index are same
        if index == shop_index: # We make this condition to find the shop through it's index
            shop_name = shop["shop_name"] # Declare this variable to store the name of the shop
            # Then declare another variable to track the current index within the loop itself 
            index = 1
            t1 = 1 # Set the t1 to 1 for indicating that the shop exists
            # After that iterate over the shop's item 
            for thing in shop["items"]: 
                # If the given argument item_index and the current index are same 
                if index == item_index: # We again do this condition, this time to find the item thorugh it's index 
                    # Then declare a variable for storing the name of the item and the price of the item 
                    item_name = thing["item_name"]
                    item_price = thing["item_price"]
                    t2 = 1 # Set the t2 to 1 for indicating that the item is found
                    break
                else:
                    # Else increase the index by one
                    index += 1
                    continue
        else:
            # Else decrease the index by one
            index += 1
            continue

    # Check if the t1 is still None
    if t1 is None:
        # If none, then it means that there is no shop in that index
        return [False, 1]
    
    # Check if the t2 is still None
    if t2 is None:
        # if still none, then it means that there is no such item in that shop
        return [False, 2]

    # Get the inventory data as users
    users = await get_inventory_data()
    # Check if the user has enough money to buy this item
    if users[str(user.id)]["Money"]["Wallet"] >= int(item_price*item_amount):
        pass
    else:
        # If not return False and 3 to indicate that the user does not have enough money
        return [False, 3]


    # Open the items data json file        
    with open(items_data_json_file, "r") as json_file:
        # Load the data of the json file
        data = json.load(json_file)
    
    # Iterate over the data
    for item in data:
        # If the item's name and item_name variable's value are same
        if item["item_name"] == item_name:
            item_name = item["item_name"]
            item_type = item["type"]
            break
        
        else: 
            # Else then pass
            pass

    # Declare a variable to track the current index
    index = 0
    # Declare another variable to track if the user already has the item
    t = None
    # Iterate over the user's inventory first
    for thing in users[str(user.id)]["Inventory"]:
        n = thing["item_name"]
        if n == item_name:
            old_amt = thing["item_amount"]
            new_amt = old_amt + item_amount
            # Set the new amount of the item in the user's inventory
            users[str(user.id)]["Inventory"][index]["item_amount"] = new_amt
            # Set t variable to 1 to indicate that the user already has the item in their inventory
            t = 1
            break
        index += 1
    if t == None:
        # If the user doesn't has the item, then add the item to the user's inventory
        obj = {"item_name": item_name, "item_amount": item_amount, "item_type": item_type}

        users[str(user.id)]["Inventory"].append(obj)

    # Save it
    with open(inventory_json_file, "w") as json_file:
        json.dump(users, json_file, indent=1)

    # Update the money
    await update_money(user, int(item_price*item_amount)*-1,"Wallet")

    # Return True
    return [True, item_name, item_amount, shop_name]