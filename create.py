import json
import sys
from fun_config import *


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



if len(sys.argv) > 1:
    if sys.argv[1] == "--edititem" and len(sys.argv) > 2:
        if sys.argv[2] == "shop_data":
            shop_name = input("shop_name: ")
            with open(shop_data_json_file, "r") as data_file:
                data = json.load(data_file)

            t = 0

            edited_item = {}
            index = 0
            for shop in data:
                if shop["shop_name"] == shop_name:
                    t = 1
                    for key, value in shop.items():
                        if isinstance(value, str):
                            the_input = input(f"(str) [ {value} ] {key}: ")

                            if the_input == "":
                                the_input = value
                            else:
                                the_input = str(the_input)
 
                        elif isinstance(value, list):
                            the_input_list = []
                            while True:
                                the_input = input(f"(list (any)) [ {value} ] {key}: ")
                                if str(the_input) == "":
                                    break
                                else:
                                    the_input_list.append(the_input)
                                    continue

                            if the_input_list == ["empty"]:
                                the_input_list = []
                            elif the_input_list == []:
                                the_input_list = value

                            the_input = the_input_list

                        elif isinstance(value, int):
                            the_input = input(f"(int) [ {value} ] {key}: ")

                            if the_input == "":
                                the_input = value
                            else:
                                the_input = int(the_input)

                        elif isinstance(value, float): 
                            the_input = input(f"(float) [ {value} ] {key}: ")

                            if the_input == "":
                                the_input = value
                            else:
                                the_input = float(the_input)

                        elif isinstance(value, bool):
                            the_input = input(f"(bool) [ {value} ] {key}: ")

                            if the_input == "":
                                the_input = value
                            else:
                                the_input = bool(the_input)
                        
                        elif isinstance(value, dict):
                            the_input_dict = {}
                            while True:
                                the_input = input(f"(key, value (any) ) [ {value} ] {key}: ")
                                if str(the_input) == "":
                                    break
                                else:
                                    the_input_key, the_input_value = the_input.split(":")
                                    the_input_dict[the_input_key] = the_input_value
                                    continue

                            if the_input_dict == {"empty"}:
                                the_input_dict = {}
                            elif the_input_dict == {}:
                                the_input_dict = value
                            
                            the_input = the_input_dict                            
    
                        edited_item[key] = the_input
                        continue

                    break

                else:
                    index += 1
                    pass


            
            if t == 0:
                print("No results found")
            else:

                data[index] = edited_item

                with open(shop_data_json_file, "w") as json_file:
                    json.dump(data, json_file, indent=1)

                print("Successfully edited the item")



        elif sys.argv[2] == "items_data":
            item_name = input("item_name: ")
            with open(items_data_json_file, "r") as data_file:
                data = json.load(data_file)

            t = 0

            edited_item = {}
            index = 0
            for item in data:
                if item["item_name"] == item_name:
                    t = 1
                    for key, value in item.items():
                        if isinstance(value, str):
                            the_input = input(f"(str) [ {value} ] {key}: ")

                            if the_input == "":
                                the_input = value
                            else:
                                the_input = str(the_input)
 
                        elif isinstance(value, list):
                            the_input_list = []
                            while True:
                                the_input = input(f"(list (any)) [ {value} ] {key}: ")
                                if str(the_input) == "":
                                    break
                                else:
                                    the_input_list.append(the_input)
                                    continue

                            if the_input_list == ["empty"]:
                                the_input_list = []
                            elif the_input_list == []:
                                the_input_list = value

                            the_input = the_input_list

                        elif isinstance(value, int):
                            the_input = input(f"(int) [ {value} ] {key}: ")

                            if the_input == "":
                                the_input = value
                            else:
                                the_input = int(the_input)

                        elif isinstance(value, float): 
                            the_input = input(f"(float) [ {value} ] {key}: ")

                            if the_input == "":
                                the_input = value
                            else:
                                the_input = float(the_input)

                        elif isinstance(value, bool):
                            the_input = input(f"(bool) [ {value} ] {key}: ")

                            if the_input == "":
                                the_input = value
                            else:
                                the_input = bool(the_input)
                        
                        elif isinstance(value, dict):
                            the_input_dict = {}
                            while True:
                                the_input = input(f"(key, value (any) ) [ {value} ] {key}: ")
                                if str(the_input) == "":
                                    break
                                else:
                                    the_input_key, the_input_value = the_input.split(":")
                                    the_input_dict[the_input_key] = the_input_value
                                    continue

                            if the_input_dict == {"empty"}:
                                the_input_dict = {}
                            elif the_input_dict == {}:
                                the_input_dict = value
                            
                            the_input = the_input_dict                            
    
                        edited_item[key] = the_input
                        continue

                    break

                else:
                    index += 1
                    pass


            
            if t == 0:
                print("No results found")
            else:

                data[index] = edited_item

                with open(items_data_json_file, "w") as json_file:
                    json.dump(data, json_file, indent=1)

                print("Successfully edited the item")
        else:
            print("Something went wrong")




    elif sys.argv[1] == "--additem" and len(sys.argv) > 2:
        if sys.argv[2] == "shop_data":
            item = {}
            for key, value in shop_data_template.items():
                if isinstance(value, str):
                    the_input = str(input(f"(str) {key}: "))   
                elif isinstance(value, list):
                    the_input_list = []
                    while True:
                        the_input = input(f"(list (any)) {key}: ")
                        if str(the_input) == "":
                            break
                        else:
                            the_input_list.append(the_input)
                            continue

                    the_input = the_input_list
                elif isinstance(value, int):
                    the_input = int(input(f"(int) {key}: "))
                elif isinstance(value, float): 
                    the_input = float(input(f"(float) {key}: "))
                elif isinstance(value, bool):
                    the_input = bool(input(f"(bool) {key}: "))
                elif isinstance(value, dict):
                    the_input_dict = {}
                    while True:
                        the_input = input(f"(key, value (any) ) {key}: ")
                        if str(the_input) == "":
                            break
                        else:
                            the_input_key, the_input_value = the_input.split(":")
                            the_input_dict[the_input_key] = the_input_value
                            continue
                    
                    the_input = the_input_dict
                
                item[key] = the_input
                continue

            with open(shop_data_json_file, "r") as data_file:
                data = json.load(data_file)
                
            data.append(item)

            with open(shop_data_json_file, "w") as json_file:
                json.dump(data, json_file, indent=1)

            print("Successfully added the item")

        elif sys.argv[2] == "items_data":
            item = {}
            for key, value in items_data_template.items():
                if isinstance(value, str):
                    the_input = str(input(f"(str) {key}: "))   
                elif isinstance(value, list):
                    the_input_list = []
                    while True:
                        the_input = input(f"(list (any)) {key}: ")
                        if str(the_input) == "":
                            break
                        else:
                            the_input_list.append(the_input)
                            continue

                    the_input = the_input_list
                elif isinstance(value, int):
                    the_input = int(input(f"(int) {key}: "))
                elif isinstance(value, float): 
                    the_input = float(input(f"(float) {key}: "))
                elif isinstance(value, bool):
                    the_input = bool(input(f"(bool) {key}: "))
                elif isinstance(value, dict):
                    the_input_dict = {}
                    while True:
                        the_input = input(f"(key, value (any) ) {key}: ")
                        if str(the_input) == "":
                            break
                        else:
                            the_input_key, the_input_value = the_input.split(":")
                            the_input_dict[the_input_key] = the_input_value
                            continue
                    
                    the_input = the_input_dict
                
                item[key] = the_input
                continue

            with open(items_data_json_file, "r") as data_file:
                data = json.load(data_file)
                
            data.append(item)

            with open(items_data_json_file, "w") as json_file:
                json.dump(data, json_file, indent=1)

            print("Successfully added the item")
        else:
            print("Something went wrong")

