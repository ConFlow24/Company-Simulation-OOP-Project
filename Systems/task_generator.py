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





class Task:
    def __init__(self, type, name, size, duration = 1):
        self.name = name
        self.type = type
        self.duration = duration
        self.size = size
        self.progress = 0
        self.assigned_to = None

class TaskSystems:
    def __init__(self):
        self.task_list = []
        self.doing_tasks = []
        self.store_list = [] #for storing items that are bought and waiting to be added to inventory, each item is a dictionary with name, size, and quantity

    size_lookup = { #for length of task duration
        "Small": (1, 3),
        "Medium": (4, 6),
        "Large": (7, 10)
    }

    def assign_task(self, employees, attendance, day):
        available_employees = []
        for emp in employees:
            if emp.role == "CEO" or emp.working:
                continue
            emp_record = attendance.records[day].get(emp.name, {})
            if emp_record.get("status") == "Absent":
                continue

            available_employees.append(emp)
        for task in self.task_list[:]:
            if not available_employees:
                break

            emp = random.choice(available_employees)
            task.assigned_to = emp
            task.duration = random.randint(*self.size_lookup[task.size])

            emp.working = True
            self.doing_tasks.append(task)
            available_employees.remove(emp)
            self.task_list.remove(task)

    def generate_buy_task(self, employees):
        for _ in range(int(len(employees) // 1.5)): #generate buy tasks based on the number of employees, but not more than half of the total employees
            type = "Buy"
            name = random.choice(items)
            size = random.choice(["Small", "Medium", "Large"])
            duration = random.randint(*self.size_lookup[size])
            self.task_list.append(Task(type, name, size, duration))

    def generate_store_task(self, employees):
        for task in self.store_list:
            type = "Store"
            name = task.get("name")
            size = task.get("size")
            duration = random.randint(*self.size_lookup[size])
            self.task_list.append(Task(type, name, size, duration))

    def generate_sell_task(self, employees, inventory):
        for _ in range(len(inventory.items) // 3): #generate sell tasks based on the number of items in inventory, but not more than half of the total items
            type = "Sell"
            name = random.choice(items)
            size = random.choice(["Small", "Medium", "Large"])
            duration = random.randint(*self.size_lookup[size])
            self.task_list.append(Task(type, name, size, duration))

    def complete_task(self, employee):
        for task in self.doing_tasks[:]:
            if task.assigned_to == employee:
                task.progress += employee.speed
                if task.progress >= task.duration:
                    self.doing_tasks.remove(task)
                    employee.tasks_completed += 1
                    employee.working = False
                    break
    
    def overtime_check(self, employee, attendance, day):
        if self.doing_tasks:
            for task in self.doing_tasks:
                #add remaining hours to overtime if task not complete in 8 hours(loops)
                remaining = task.duration - task.progress
                attendance.records[day][employee.name]["overtime_hours"] = remaining
                attendance.records[day][employee.name]["hours_worked"] += remaining