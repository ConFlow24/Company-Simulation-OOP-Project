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
from inventory import Inventory

items = {
    "keyboard": 25, "mouse": 15, "monitor": 180, "laptop": 800, "desktop computer": 900,
    "printer": 120, "scanner": 100, "tablet": 300, "smartphone": 700, "phone case": 15,
    "charger": 20, "power bank": 30, "usb cable": 10, "headphones": 60, "earbuds": 40,
    "speaker": 80, "webcam": 50, "microphone": 70, "router": 100, "modem": 90,

    "table": 150, "chair": 80, "sofa": 500, "couch": 600, "bed frame": 250,
    "mattress": 400, "cabinet": 200, "drawer": 120, "bookshelf": 140, "desk": 180,
    "office chair": 220, "stool": 50, "bench": 130, "wardrobe": 350,

    "lightbulb": 5, "lamp": 40, "desk lamp": 30, "floor lamp": 70,
    "extension cord": 20, "power strip": 25, "fan": 60, "air conditioner": 400, "heater": 90,

    "shoes": 80, "sneakers": 100, "sandals": 40, "slippers": 20, "boots": 120, "heels": 90,
    "t-shirt": 20, "shirt": 35, "polo": 40, "hoodie": 50, "jacket": 80, "coat": 120,
    "jeans": 60, "shorts": 30, "skirt": 35, "dress": 70, "socks": 10, "underwear": 15,
    "belt": 25, "hat": 20, "cap": 18,

    "watch": 120, "sunglasses": 80, "bag": 70, "backpack": 60, "wallet": 40,
    "purse": 90, "jewelry": 150, "necklace": 100, "bracelet": 80, "ring": 120, "earrings": 70,

    "books": 20, "notebooks": 10, "magazines": 8, "textbooks": 100, "comics": 12,
    "pens": 5, "pencils": 3, "markers": 12, "highlighters": 10, "art supplies": 50,

    "kitchen utensils": 40, "plates": 30, "bowls": 25, "cups": 20, "mugs": 15, "glasses": 25,
    "spoons": 15, "forks": 15, "knives": 30, "cutting board": 20, "cookware": 150,
    "pots": 60, "pans": 50, "kettle": 40, "rice cooker": 80, "microwave": 120,
    "oven": 500, "toaster": 30, "blender": 70,

    "refrigerator": 800, "freezer": 500, "washing machine": 600,
    "dryer": 500, "dishwasher": 700,

    "toys": 25, "board games": 40, "puzzles": 20, "action figures": 30, "dolls": 25,
    "video games": 60, "game console": 500, "controllers": 60,

    "bicycle": 300, "helmet": 50, "skateboard": 80, "roller skates": 70,
    "dumbbells": 60, "barbell": 120, "yoga mat": 25, "exercise bands": 20,

    "car accessories": 100, "motorcycle helmet": 150, "car cover": 60, "seat cover": 80,
    "toolbox": 70, "hammer": 15, "screwdriver": 10, "wrench": 20, "drill": 80, "saw": 50,

    "gardening tools": 50, "plant pots": 30, "seeds": 10, "fertilizer": 20, "watering can": 15,

    "cosmetics": 50, "makeup": 60, "skincare products": 70, "perfume": 100,
    "hair dryer": 40, "straightener": 50,

    "curtains": 60, "carpet": 200, "rug": 120, "bedsheets": 50, "blankets": 60, "pillows": 30,

    "collectibles": 200, "antiques": 500, "coins": 50, "stamps": 40, "trading cards": 30,

    "pet supplies": 60, "pet food": 40, "leash": 20, "collar": 15, "pet toys": 25, "aquarium": 150,

    "camera": 700, "lens": 400, "tripod": 80, "lighting equipment": 150, "drone": 900,

    "musical instruments": 300, "guitar": 200, "piano keyboard": 250, "drum set": 500, "violin": 180,

    "cleaning supplies": 40, "vacuum cleaner": 150, "mop": 20, "broom": 15, "detergent": 25
}



inventory = Inventory()

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
        self.task_list = [] #iniial task list
        self.doing_tasks = [] #task list when assigned to employees and in progress
        self.store_list = [] #for storing items that are bought and waiting to be added to inventory, each item is a dictionary with name, size, and quantity
        self.completed_tasks = []
        self.size_lookup = {"Small": (1, 2), "Medium": (3, 5), "Large": (6, 8)} #task duration based on size of item

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

    def assign_task_manual(self, employees, attendance, day, company):
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

            company.list_employees()
            while True:
                emp = input("Enter an employee from the list:  ").strip()

                employee = company.get_employee(emp)
                if employee is None:
                    print("Employee not found.")
                else: break
                
            task.assigned_to = emp
            task.duration = random.randint(*self.size_lookup[task.size])

            emp.working = True
            self.doing_tasks.append(task)
            available_employees.remove(emp)
            self.task_list.remove(task)

    def generate_buy_task(self, employees):
        for _ in range(int(len(employees) // 1.5)): #generate buy tasks based on the number of employees, but not more than half of the total employees
            type = "Buy"
            name = random.choice(list(items))
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

    def generate_sell_task(self, employees):
        if inventory.items():
            for _ in range(len(inventory.items) // 3): #generate sell tasks based on the number of items in inventory, but not more than half of the total items
                type = "Sell"
                item_to_sell = random.choice(list(inventory.items.keys()))
                name = item_to_sell[name]
                size = item_to_sell[name][size]
                duration = random.randint(*self.size_lookup[size])
                self.task_list.append(Task(type, name, size, duration))

    def do_task(self, employee):
        for task in self.doing_tasks[:]:
            if task.assigned_to == employee:
                task.progress += employee.speed
                if task.progress >= task.duration:
                    self.completed_tasks.append(task)
                    self.doing_tasks.remove(task)
                    employee.tasks_completed += 1
                    employee.working = False
                    break
    
    def overtime_check(self, employee, attendance, day):
        if self.doing_tasks:
            for task in self.doing_tasks[:]:
                #add remaining hours to overtime if task not complete in 8 hours(loops)
                remaining = task.duration - task.progress
                attendance.records[day][employee.name]["overtime_hours"] = remaining
                attendance.records[day][employee.name]["hours_worked"] += remaining
                self.completed_tasks.append(task)
                self.doing_tasks.remove(task)

    def complete_task(self):
        for task in self.completed_tasks[:]:
            match task.type:
                case "Buy":
                    self.store_list.append({"name": task.name, "size": task.size, "quantity": 1})
                    inventory.money -= inventory.get_price(task.name, task.size)
                    self.complete_tasks.remove(task)
                case "Sell":
                    inventory.remove_item(task.name, task.size, 1)
                    inventory.money += inventory.get_price(task.name, task.size) * 1.2 #sell for 20% profit
                    self.complete_tasks.remove(task)
                case "Store":
                    for item in self.store_list:
                        if item["name"] == task.name and item["size"] == task.size:
                            inventory.add_item(task.name, task.size, item["quantity"], inventory.get_price(task.name, task.size))
                            self.store_list.remove(item)
                            break
                    self.complete_tasks.remove(task)

    def show_tasks(self):
        print("\n--- Tasks ---")
        for task in self.task_list:
            print(f"{task.type} | {task.name} | {task.size} | Duration: {task.duration} | Assigned to: {task.assigned_to.name if task.assigned_to else 'Unassigned'}")