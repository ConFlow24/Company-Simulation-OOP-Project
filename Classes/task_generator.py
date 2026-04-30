import random
from collections import defaultdict
from Classes.items import items


class Task:
    def __init__(self, type, name, size, duration=1):
        self.name = name
        self.type = type
        self.duration = duration
        self.size = size
        self.progress = 0
        self.assigned_to = None


class TaskSystems:
    def __init__(self):
        self.task_list = []  # iniial task list
        self.doing_tasks = []  # task list when assigned to employees and in progress
        self.store_list = []  # for storing items that are bought and waiting to be added to inventory, each item is a dictionary with name, size, and quantity
        self.completed_tasks = []
        # task duration based on size of item
        self.size_lookup = {"Small": (1, 2), "Medium": (3, 5), "Large": (6, 8)}
        self.stop_manual_assign = False

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
        while self.task_list and available_employees:
        # pick task
            print("\n--- Unassigned Tasks ---")
            for i, task in enumerate(self.task_list):
                print(f"{i+1}. {task.type} - {task.name.title()} ({task.size})")
            print(f"{len(self.task_list)+1}. Stop assigning")

            while True:
                try:
                    task_choice = int(input("Pick a task: "))
                    if task_choice == len(self.task_list)+1:
                        self.stop_manual_assign = True
                        return  # Stop assigning option
                    if 1 <= task_choice <= len(self.task_list):
                        task = self.task_list[task_choice - 1]
                        break
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input.")

        # pick employee
            company.list_available_employees(available_employees)
            while True:
                try:
                    emp_choice = int(input(f"Enter the number of an employee to work on \"{task.type} - {task.name.title()}\": "))
                    if 1 <= emp_choice <= len(available_employees):
                        employee = available_employees[emp_choice - 1]
                        break
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input.")
                    

            task.assigned_to = employee
            print(f"{task.type} - {task.name} has been assigned to {employee.name}")
            employee.working = True
            self.doing_tasks.append(task)
            available_employees.remove(employee)
            self.task_list.remove(task)

    def assign_task_manual_individual(self, emp):
        if emp.role == "CEO" or self.stop_manual_assign == False:
            return
        print("\n--- Unassigned Tasks ---")
        for i, task in enumerate(self.task_list):
            print(f"{i+1}. {task.type} - {task.name.title()} ({task.size})")
        
        while True:
            try:
                choice = int(input(f"\n{emp.name} is free. Pick a task (1-{len(self.task_list)}): "))
                if 1 <= choice <= len(self.task_list):
                    task = self.task_list[choice - 1]
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")

        task.assigned_to = emp
        emp.working = True
        self.doing_tasks.append(task)
        self.task_list.remove(task)
        
        print(f"{task.type} - {task.name.title()} has been assigned to {emp.name}")
        print("\n--- Continuing Day Events ---")

    def generate_buy_task(self, employees):
        # generate buy tasks based on the number of employees, but not more than half of the total employees
        for _ in range(int(len(employees) // 1.5)):
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
        # generate sell tasks based on the number of items in inventory, but not more than half of the total items
        for _ in range(task_amount):
            type = "Sell"
            item_to_sell = random.choice(list(actual_items.keys()))
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
                print(f"{employee.name} is progressing in \"{task.type} - {task.name.title()}\". Progress left {max(0, task.duration - task.progress)}")

                if task.progress >= task.duration:
                    self.completed_tasks.append(task)
                    self.doing_tasks.remove(task)
                    employee.tasks_completed += 1
                    employee.working = False
                    print(
                        f"{employee.name} has completed \"{task.type} - {task.name.title()}\"")
                    break

    def overtime_check(self, attendance, day):
        for task in self.doing_tasks[:]:
            employee = task.assigned_to
            if employee is None:
                continue
            remaining = task.duration - task.progress
            attendance.records[day][employee.name]["overtime_hours"] = remaining
            attendance.records[day][employee.name]["hours_worked"] += remaining
            self.completed_tasks.append(task)
            self.doing_tasks.remove(task)

    def complete_task(self, inventory):
        for task in self.completed_tasks[:]:
            match task.type:
                case "Buy":
                    self.store_list.append(
                        {"name": task.name, "size": task.size, "quantity": 1})
                    inventory.cash -= inventory.get_price(task.name, task.size)
                    self.completed_tasks.remove(task)
                case "Sell":
                    inventory.remove_item(task.name, task.size, 1)
                    # sell for 20% profit
                    inventory.cash += inventory.get_price(
                        task.name, task.size) * 1.2
                    self.completed_tasks.remove(task)
                case "Store":
                    for item in self.store_list:
                        if item["name"] == task.name and item["size"] == task.size:
                            inventory.add_item(
                                task.name, task.size, item["quantity"])
                            self.store_list.remove(item)
                            break
                    self.completed_tasks.remove(task)
    
    def task_to_employee_ratio_check(self, employees_list):
        if len(self.task_list) / len(employees_list) > 3:
            print("\nYou have too many tasks per employee. Consider hiring more employees, through the CEO Panel.\n")

    def show_tasks(self):
        print("\n" + "=" * 70)
        print(f"{'TASKS FOR THE DAY':^70}")
        print("=" * 70)
        print(
            f"{'Type':<10} {'Name':<15} {'Size':<10} {'Duration':>10} {'Assigned To':<20}")
        print("=" * 70)
        for task in self.task_list:
            assigned = task.assigned_to.name if task.assigned_to else "Unassigned"
            print(
                f"{task.type:<10} {task.name.title():<15} {task.size:<10} {task.duration:>10} {assigned:<20}")
        print("=" * 70 + "\n")
