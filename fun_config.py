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
        data[str(user.id)]["Inventory"] = []

    with open(inventory_json_file, "w") as json_file:
        json.dump(data, json_file, indent=1)
    return True

async def make_bar(subset: int, superset: int, set1_color: str, set2_color: str):
    dash_convert = int(superset/10)
    current_dashes = int(subset/dash_convert)
    remaining_max_value = 10 - current_dashes

    current_value_display = set1_color * current_dashes
    remaining_max_value_display = set2_color * remaining_max_value

    return ("|" + current_value_display + remaining_max_value_display + "|" + " " + f"{subset}/{superset}")