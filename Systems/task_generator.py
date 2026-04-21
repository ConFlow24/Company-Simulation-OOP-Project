#ian

#mga function:

#ang tasks lang naman ay pagbuy, sell, store ng inventory
#kada task may "time to complete" na naapekto nung speed stat nung employee
#posible rin madagdagan ang mga task bukod dun base sa gagawin ni jeff sa employee.py

#task generator function
#random.choices, alam mo naman siguro kung pano yun
#make sure na may at least 1 of each action everyday, bukod sa mga imposible mangyari like kung walang laman inventory
#skip mo yung may role na CEO

#task assigner function
#possible na dictionary ang gamitin mo. Similar system sa attendance.py
#kung matuloy yung mga mentor() at iba pang unique actions na nakalagay sa employee.py make sure na maassign lang yung task na yun sa specific na role na yun.

#task completed recorder
#per employee merong 

#view all tasks. obvious naman. parang tasks completed and tasks remaining

#delete comments when done

import random
from collections import defaultdict

items = [
    "keyboard", "mouse", "monitor", "laptop", "desktop computer", "printer", "scanner",
    "tablet", "smartphone", "phone case", "charger", "power bank", "usb cable",
    "headphones", "earbuds", "speaker", "webcam", "microphone", "router", "modem",

    "table", "chair", "sofa", "couch", "bed frame", "mattress", "cabinet", "drawer",
    "bookshelf", "desk", "office chair", "stool", "bench", "wardrobe",

    "lightbulb", "lamp", "desk lamp", "floor lamp", "extension cord", "power strip",
    "fan", "air conditioner", "heater",

    "shoes", "sneakers", "sandals", "slippers", "boots", "heels",
    "t-shirt", "shirt", "polo", "hoodie", "jacket", "coat", "jeans",
    "shorts", "skirt", "dress", "socks", "underwear", "belt", "hat", "cap",

    "watch", "sunglasses", "bag", "backpack", "wallet", "purse", "jewelry",
    "necklace", "bracelet", "ring", "earrings",

    "books", "notebooks", "magazines", "textbooks", "comics",
    "pens", "pencils", "markers", "highlighters", "art supplies",

    "kitchen utensils", "plates", "bowls", "cups", "mugs", "glasses",
    "spoons", "forks", "knives", "cutting board", "cookware",
    "pots", "pans", "kettle", "rice cooker", "microwave", "oven", "toaster", "blender",

    "refrigerator", "freezer", "washing machine", "dryer", "dishwasher",

    "toys", "board games", "puzzles", "action figures", "dolls",
    "video games", "game console", "controllers",

    "bicycle", "helmet", "skateboard", "roller skates",
    "dumbbells", "barbell", "yoga mat", "exercise bands",

    "car accessories", "motorcycle helmet", "car cover", "seat cover",
    "toolbox", "hammer", "screwdriver", "wrench", "drill", "saw",

    "gardening tools", "plant pots", "seeds", "fertilizer", "watering can",

    "cosmetics", "makeup", "skincare products", "perfume", "hair dryer", "straightener",

    "curtains", "carpet", "rug", "bedsheets", "blankets", "pillows",

    "collectibles", "antiques", "coins", "stamps", "trading cards",

    "pet supplies", "pet food", "leash", "collar", "pet toys", "aquarium",

    "camera", "lens", "tripod", "lighting equipment", "drone",

    "musical instruments", "guitar", "piano keyboard", "drum set", "violin",

    "cleaning supplies", "vacuum cleaner", "mop", "broom", "detergent"
]

class task:
    task_choices = ["buy"]
    queue = defaultdict(dict)
    to_store = []
    tasks_generated = ["buy{productname}, {size:7}"]

    def generate_task(self):
        # task = {}
        # if inventory has item
            #task[type_of_task] = type of task
            # task_choices.append(task)

        # if queue has items
            # task_choices.append("store")
        return random.choice(self.task_choices)
    
    def buy(self):
        self.queue[random.choice(items)]["size"] = random.randint(1,3)

    def sell(self):
        pass

    def store(self, inventory):
        if self.queue:
             self.generate_task()


task1 = task()

for i in range(5):
    task1.buy()

print(task1.queue)
