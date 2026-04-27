import random
from collections import defaultdict
from Classes.items import items


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
                name = input("Enter an employee from the list: ").strip()
                employee = company.get_employee(name)
                if employee is None:
                    print("Employee not found.")
                else:
                    found = False
                    for emp in available_employees:
                        if emp.name == employee.name:
                            found = True
                            break
                    if not found:
                        print("Employee is unavailable (absent, already working, or is CEO).")
                    else:
                        break

            task.assigned_to = employee
            task.duration = random.randint(*self.size_lookup[task.size])

            employee.working = True
            self.doing_tasks.append(task)
            available_employees.remove(employee)
            self.task_list.remove(task)

    def assign_task_manual_individual(self, emp):
        self.task_list[0].assigned_to = emp
        self.task_list[0].duration = random.randint(*self.size_lookup[self.task_list[0].size])

        emp.working = True
        self.doing_tasks.append(self.task_list[0])
        self.task_list.remove(self.task_list[0])

    def generate_buy_task(self, employees):
        for _ in range(int(len(employees) // 1.5)): #generate buy tasks based on the number of employees, but not more than half of the total employees
            type = "Buy"
            name = random.choice(list(items))
            size = random.choice(["Small", "Medium", "Large"])
            duration = random.randint(*self.size_lookup[size])
            self.task_list.append(Task(type, name, size, duration))

    def generate_store_task(self):
        for task in self.store_list:
            type = "Store"
            name = task.get("name")
            size = task.get("size")
            duration = random.randint(*self.size_lookup[size])
            self.task_list.append(Task(type, name, size, duration))

    def generate_sell_task(self, inventory, order_spike=False):
        actual_items = {}
        for name, stock in inventory.items.items():
            has_stock = False
            for size in ["Small", "Medium", "Large"]:
                if stock[size] > 0:
                    has_stock = True
                    break
            if has_stock:
                actual_items[name] = stock

        if not actual_items:
            return

        task_amount = len(inventory.items) // 3
        if order_spike:
            task_amount *= 4
        for _ in range(task_amount): #generate sell tasks based on the number of items in inventory, but not more than half of the total items
            type = "Sell"
            item_to_sell = random.choice(list(inventory.items.keys()))
            name = item_to_sell
            size_choices = ["Small", "Medium", "Large"]
            while size_choices:
                size = random.choice(size_choices)
                if inventory.items[item_to_sell][size] == 0:
                    size_choices.remove(size)
                else:
                    break
            else:
                continue
                
            duration = random.randint(*self.size_lookup[size])
            self.task_list.append(Task(type, name, size, duration))

    def do_task(self, employee):
        for task in self.doing_tasks[:]:
            if task.assigned_to == employee:
                task.progress += employee.speed
                print(f"{employee.name} is progressing in \"{task.type} - {task.name}\". Progress left {task.duration - task.progress}")

                if task.progress >= task.duration:
                    self.completed_tasks.append(task)
                    self.doing_tasks.remove(task)
                    employee.tasks_completed += 1
                    employee.working = False
                    print(f"{employee.name} has completed \"{task.type} - {task.name}\"")
                    break
    
    def overtime_check(self, employees, attendance, day):
        for employee in employees:
            if self.doing_tasks:
                for task in self.doing_tasks[:]:
                    #add remaining hours to overtime if task not complete in 8 hours(loops)
                    remaining = task.duration - task.progress
                    attendance.records[day][employee.name]["overtime_hours"] = remaining
                    attendance.records[day][employee.name]["hours_worked"] += remaining
                    self.completed_tasks.append(task)
                    self.doing_tasks.remove(task)

    def complete_task(self, inventory):
        for task in self.completed_tasks[:]:
            match task.type:
                case "Buy":
                    self.store_list.append({"name": task.name, "size": task.size, "quantity": 1})
                    inventory.cash -= inventory.get_price(task.name, task.size)
                    self.completed_tasks.remove(task)
                case "Sell":
                    inventory.remove_item(task.name, task.size, 1)
                    inventory.cash += inventory.get_price(task.name, task.size) * 1.2 #sell for 20% profit
                    self.completed_tasks.remove(task)
                case "Store":
                    for item in self.store_list:
                        if item["name"] == task.name and item["size"] == task.size:
                            inventory.add_item(task.name, task.size, item["quantity"])
                            self.store_list.remove(item)
                            break
                    self.completed_tasks.remove(task)

    def show_tasks(self):
        print("\n--- Tasks ---")
        for task in self.task_list:
            print(f"{task.type} | {task.name} | {task.size} | Duration: {task.duration} | Assigned to: {task.assigned_to.name if task.assigned_to else 'Unassigned'}")
