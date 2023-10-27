import json
import firebase_admin
from firebase_admin import db, credentials
from fun_config import *
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
credentials_path = os.path.join(script_dir, 'credentials.json')

cred = credentials.Certificate(credentials_path)
firebase_admin.initialize_app(cred, {"databaseURL": "https://hoex-41b97-default-rtdb.asia-southeast1.firebasedatabase.app/"})



class DB():

    def __init__(self):
        self.db = db

    async def create(self):
        if self.db.reference("/").get() == None:
            self.db.reference("/").update({"inventory": "None"})
            self.db.reference("/").update({"farm": "None"})
            self.db.reference("/").update({"items_data": "None"})
            self.db.reference("/").update({"shop_data": "None"})
            return True
        else:
            return False
        
    async def update(self, mode=("inventory", "farm", "items_data", "shop_data")):
        if mode == "inventory":
            users = await get_inventory_data()
        elif mode == "farm":
            users = await get_farm_data()
        elif mode == "items_data":
            with open(items_data_json_file, "r") as json_file:
                users = json.load(json_file)
                users = (users)
        elif mode == "shop_data":
            with open(shop_data_json_file, "r") as json_file:
                users = json.load(json_file)
                users = (users)
        try:
            self.db.reference(f"/{mode}").update(users)
        except:
            self.db.reference(f"/{mode}").set(users)

    async def retrieve(self, mode=("inventory", "farm", "items_data", "shop_data")):
        return self.db.reference(f"/{mode}").get()
    
    async def update_json(self, mode=("inventory", "farm", "items_data", "shop_data")):
        if mode == "inventory":
            users = self.db.reference("/inventory").get()
            with open(inventory_json_file, "w") as json_file:
                json.dump(users, json_file, indent=1)
        elif mode == "farm":
            users = self.db.reference("/farm").get()
            with open(farm_json_file, "w") as json_file:
                json.dump(users, json_file, indent=1)
        elif mode == "items_data":
            users = self.db.reference("/items_data").get()
            with open(items_data_json_file, "w") as json_file:
                json.dump(users, json_file, indent=1)
        elif mode == "shop_data":
            users = self.db.reference("/shop_data").get()
            with open(shop_data_json_file, "w") as json_file:
                json.dump(users, json_file, indent=1)
        
        return users
    