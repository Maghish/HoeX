import json
import sys
from fun_config import *

# the templates
items_data_template = {
    "item_name": "",
    "description": "",
    "type": "",
    "extra_data": [],
}

shop_data_template = {
    "shop_name": "",
    "owner_name": "",
    "description": "",
    "items": []
}


# the arguments checking
if len(sys.argv) > 1:
     # Check if the 2nd argument is --edittemp and also has one more argument
    if sys.argv[1] == "--edittemp" and len(sys.argv) > 2:
        # Check the 3rd argument 
        if sys.argv[2] == "shop_data":
            ...
        elif sys.argv[2] == "items_data":
            ...
        else:
            print("Something went wrong")
    # Check if the 2nd argument is --additem and also has one more argument
    elif sys.argv[1] == "--additem" and len(sys.argv) > 2:
        # Check the 3rd argument
        if sys.argv[2] == "shop_data":
            # Create a item dict to append to the json data
            item = {}
            # Get key and value of the items in that template
            for key, value in shop_data_template.items():
                # Check the type of the value
                if isinstance(value, str):
                    # Turn the input to the respective type
                    the_input = str(input(f"(str) {key}: "))
                # Check the type of the value     
                elif isinstance(value, list):
                    # Turn the input to the respective type
                    the_input_list = []
                    while True:
                        the_input = input(f"(list (any)) {key}: ")
                        if str(the_input) == "exit":
                            break
                        else:
                            the_input_list.append(the_input)
                            continue

                    the_input = the_input_list
                # Check the type of the value
                elif isinstance(value, int):
                    # Turn the input to the respective type
                    the_input = int(input(f"(int) {key}: "))
                # Check the type of the value
                elif isinstance(value, float): 
                    # Turn the input to the respective type
                    the_input = float(input(f"(float) {key}: "))
                # Check the type of the value
                elif isinstance(value, bool):
                    # Turn the input to the respective type
                    the_input = bool(input(f"(bool) {key}: "))
                # Check the type of the value
                elif isinstance(value, dict):
                    # Turn the input to the respective type
                    the_input_dict = {}
                    while True:
                        the_input = input(f"(key, value (any) ) {key}: ")
                        if str(the_input) == "exit":
                            break
                        else:
                            the_input_key, the_input_value = the_input.split(":")
                            the_input_dict[the_input_key] = the_input_value
                            continue
                    
                    the_input = the_input_dict
                
                # Finally add the element to the item dict
                item[key] = the_input
                continue

            # Get data from the respected json file
            with open(shop_data_json_file, "r") as data_file:
                data = json.load(data_file)
                
            # Append the new item dict to the json data
            data.append(item)

            # Save it
            with open(shop_data_json_file, "w") as json_file:
                json.dump(data, json_file, indent=1)

            print("Successfully added the item")

        elif sys.argv[2] == "items_data":
            ...
        else:
            print("Something went wrong")

