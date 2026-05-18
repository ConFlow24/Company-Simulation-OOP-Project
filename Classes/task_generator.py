import random
from Classes.items import items
from Classes import formatting


class Task:
    """
    This class represents a task in the company simulation.

    Tasks are generated daily and categorized as Buy, Sell, or Store.
    Each task has a duration that must be fully worked through before completion.

    Attributes:
        type (str): Task category — 'Buy', 'Sell', or 'Store'.
        name (str): The name of the item involved in the task.
        size (str): Item size — 'Small', 'Medium', or 'Large'.
        duration (int): Total work units needed to complete the task.
        progress (int): Current accumulated work units toward completion.
        assigned_to (Employee or None): The employee currently working on this task.
    """

    def __init__(self, type, name, size, duration=1):
        """
        Initializes a Task with its category, item details, and duration.

        Args:
            type (str): The task type ('Buy', 'Sell', or 'Store').
            name (str): The name of the item this task involves.
            size (str): The size of the item ('Small', 'Medium', 'Large').
            duration (int): Number of work units required to finish. Defaults to 1.
        """

        self.name = name
        self.type = type
        self.duration = duration
        self.size = size
        self.progress = 0  # progress is how much work has been done on the task, once it reaches duration, the task is completed
        self.assigned_to = None    # set when an employee is assigned


class TaskSystems:
    """
    Manages the full task lifecycle: generation, assignment, execution, and completion.

    Handles three types of tasks (Buy, Store, Sell) and supports both manual
    (player-controlled) and automatic (simulation-driven) task assignment modes.

    Attributes:
        task_list (list): Unassigned tasks waiting to be given to an employee.
        doing_tasks (list): Tasks currently in progress by assigned employees.
        store_list (list): Buffer of bought items waiting to be stored into inventory.
        completed_tasks (list): Tasks that have been fully completed this day.
        size_lookup (dict): Maps size strings to (min, max) duration ranges.
        stop_manual_assign (bool): Flag to stop further manual assignment mid-session.
    """

    def __init__(self, attendance, company, inventory, salary, empgen):
        self.task_list = []  # iniial task list
        self.doing_tasks = []  # task list when assigned to employees and in progress
        self.store_list = []  # for storing items that are bought and waiting to be added to inventory, each item is a dictionary with name, size, and quantity
        self.completed_tasks = []
        # task duration based on size of item
        self.size_lookup = {"Small": (1, 2), "Medium": (3, 5), "Large": (6, 8)}
        self.stop_manual_assign = False  # used to let player stop assigning mid-loop
        # other params
        self.employees = company.employees
        self.attendance = attendance
        self.company = company
        self.inventory = inventory
        self.salary = salary
        self.empgen = empgen

    def _pick_employee_for_task(self, task, available_employees):
        # Pick a capable employee for a task, falling back to any available employee.
        if task.type == "Unique":
            role = task.name.split(" - ")[0]
            capable = []
            for employee in available_employees:
                if employee.role == role:
                    capable.append(employee)
            if capable:
                return random.choice(capable)
        else:
            for employee in available_employees[:]:
                if employee.role == "CEO":
                    available_employees.remove(employee)

            return random.choice(available_employees)
        
    def _get_available_employees(self, day):
        # Helper function that returns all employees who are not working and not absent
        return [
            emp for emp in self.employees
            if not emp.working
            and self.attendance.records[day].get(emp.name, {}).get("status") != "Absent"
        ]

    def _assign_task_to_employee(self, task, employee):
        # Helper function that assigns a task to an employee and updates all tracking lists
        task.assigned_to = employee
        employee.working = True
        self.doing_tasks.append(task)
        self.task_list.remove(task)


    def _format_task_display(self, i, task):
        # Helper function that formats a task for display in the task selection menu

        match task.type:

            case "Buy" | "Sell":
                buy_price = self.inventory.get_price(task.name, task.size)
                sell_price = self.inventory.get_sell_price(task.name, task.size)
                profit = round(sell_price - buy_price, 2)

                return (
                    f"{i+1}. {task.type} - {task.name.title()} "
                    f"({task.size}) | Buy: ${buy_price} | "
                    f"Sell: ${sell_price} | Profit: ${profit}"
                )

            case "Unique":
                return f"{i+1}. {task.type} - {task.name.title()}"

            case _:
                return f"{i+1}. {task.type} - {task.name.title()} ({task.size})"

    def assign_task(self, day):
        """
        Automatically assigns tasks to all available employees for the day.

        Skips employees who are already working, absent, or are the CEO.
        Randomly picks a task from the task list for each available employee.
        """

        # Get all available employees for the day
        available_employees = self._get_available_employees(day)

        for task in self.task_list[:]:
            if not available_employees:
                break

            emp = self._pick_employee_for_task(task, available_employees)

            self._assign_task_to_employee(task, emp)

            available_employees.remove(emp)

    def assign_task_single(self, employee, day):
        """
        Automatically assigns a random task to a single free employee mid-day if tasks remain.
        """

        if employee.role == "CEO":
            return

        emp_record = self.attendance.records[day].get(employee.name, {})
        if emp_record.get("status") == "Absent":
            return

        if not self.task_list:
            return

        # Prefer unique tasks that match this employee's role
        matching = [
            task for task in self.task_list
            if task.type == "Unique"
            and task.name.split(" - ")[0] == employee.role
        ]

        task_pool = matching if matching else [
            t for t in self.task_list if t.type != "Unique"
        ]

        task = random.choice(task_pool)

        self._assign_task_to_employee(task, employee)

    def assign_task_manual(self, day):
        """
        Allows the user to manually assign tasks to available employees.

        Loops through available employees and unassigned tasks, prompting the user
        to pick which task goes to which employee. User can stop assigning at any time.
        """

        self.stop_manual_assign = False

        # Get available employees for the day
        available_employees = self._get_available_employees(day)

        while self.task_list and available_employees:

            # Display unassigned tasks
            print(f"""\n{'=' * 70}
{'UNASSIGNED TASKS':^70}
{'=' * 70}""")

            for i, task in enumerate(self.task_list):
                print(self._format_task_display(i, task))

            print(f"{len(self.task_list)+1}. Stop assigning")

            # pick task
            while True:
                try:
                    task_choice = int(input("Pick a task: "))

                    if task_choice == len(self.task_list) + 1:
                        self.stop_manual_assign = True
                        return

                    if 1 <= task_choice <= len(self.task_list):
                        task = self.task_list[task_choice - 1]
                        break

                    print("Invalid choice.")

                except ValueError:
                    print("Invalid input.")

            # pick employee — filter candidates based on the chosen task
            if task.type == "Unique":
                role = task.name.split(" - ")[0]

                capable = [e for e in available_employees if e.role == role]

                if capable:
                    candidates = capable
                else:
                    candidates = available_employees
            else:
                candidates = [e for e in available_employees if e.role != "CEO"]

            if not candidates:
                break

            self.company.list_available_employees(candidates)

            while True:
                try:
                    emp_choice = int(input(
                        f"Enter employee for {task.type} - {task.name.title()}: "
                    ))

                    if 1 <= emp_choice <= len(candidates):
                        employee = candidates[emp_choice - 1]
                        break

                    print("Invalid choice.")

                except ValueError:
                    print("Invalid input.")

            # Assign task
            print(f"{task.type} - {task.name.title()} assigned to {employee.name}")

            self._assign_task_to_employee(task, employee)

            available_employees.remove(employee)

            if not available_employees:
                self.stop_manual_assign = True

    def assign_task_manual_individual(self, emp):
        """
        Prompts the player to assign a specific task to a single free employee mid-day.

        Only activates if the player previously stopped manual assignment early.
        """

        if emp.role == "CEO" or self.stop_manual_assign:
            return

        # Filter out unique tasks that don't match this employee's role
        eligible_tasks = [
            task for task in self.task_list
            if not (task.type == "Unique" and task.name.split(" - ")[0] != emp.role)
        ]

        if not eligible_tasks:
            return

        # Display unassigned tasks
        print(f"""\n{'=' * 70}
    {'UNASSIGNED TASKS':^70}
    {'=' * 70}""")

        for i, task in enumerate(eligible_tasks):
            print(self._format_task_display(i, task))

        print(f"{len(eligible_tasks)+1}. Stop assigning")

        # Pick task
        while True:
            try:
                choice = int(input("Pick a task: "))

                if choice == len(eligible_tasks) + 1:
                    self.stop_manual_assign = True
                    return

                if 1 <= choice <= len(eligible_tasks):
                    task = eligible_tasks[choice - 1]
                    break

                print("Invalid choice.")

            except ValueError:
                print("Invalid input.")

        # Assign task
        self._assign_task_to_employee(task, emp)

        print(f"{task.type} - {task.name.title()} assigned to {emp.name}")
        print("\n--- Continuing Day Events ---")

    def generate_buy_task(self, buy_spike=False):
        """
        Generates a set of Buy tasks for the day based on the number of employees.

        Task count scales with company size (roughly 2/3 of employee count).
        Each task targets a random item and size from the master item list.

        Args:
            employees (list): Full list of company employees (used to scale task count).
        """
        amount = 0
        for task in self.task_list:
            if task.type == "Buy":
                amount += 1
        if amount <= len(self.employees) * 3:
            # limit amount of buy tasks to twice the amount of employees
            buy_task_amount = int(len(
                self.employees) // 1.5) if buy_spike == False else int(len(self.employees) // 1.5) * 3
            for _ in range(buy_task_amount):
                type = "Buy"
                name = random.choice(list(items))
                size = random.choice(["Small", "Medium", "Large"])
                duration = random.randint(*self.size_lookup[size])
                self.task_list.append(Task(type, name, size, duration))

    def generate_store_task(self):
        """
        Generates Store tasks for all items currently in the store_list buffer.

        Store tasks move recently bought items from the buffer into actual inventory.
        Called each day to ensure bought items are eventually stocked.
        """

        for task in self.store_list:
            type = "Store"
            name = task.get("name")
            size = task.get("size")
            duration = random.randint(*self.size_lookup[size])
            self.task_list.insert(0, Task(type, name, size, duration))

    def generate_sell_task(self, order_spike=False):
        """
        Generates Sell tasks based on items currently available in inventory.

        Only generates tasks for items that actually have stock. Task count scales
        with inventory size. If an order spike event is active, task count is multiplied by 4.

        Args:
            inventory (Inventory): The inventory system to check stock levels.
            order_spike (bool): If True, quadruples the number of sell tasks generated.
        """

        actual_items = {}
        for name, stock in self.inventory.items.items():
            has_stock = False
            for size in ["Small", "Medium", "Large"]:
                if stock[size] > 0:
                    has_stock = True
                    break
            if has_stock:
                actual_items[name] = stock

        if not actual_items:
            return

        task_amount = self.inventory.total_stock_and_price()[0] // 3
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
                if self.inventory.items[item_to_sell][size] == 0:
                    size_choices.remove(size)
                else:
                    break
            else:
                continue

            duration = random.randint(*self.size_lookup[size])
            self.task_list.insert(0, Task(type, name, size, duration))

    def generate_unique_task(self, day):
        available_employees = []
        for emp in self.employees:
            if emp.working:
                continue
            emp_record = self.attendance.records[day].get(emp.name, {})
            if emp_record.get("status") == "Absent":
                continue
            available_employees.append(emp)

        for employee in available_employees:
            name = None
            match employee.role:
                case "CEO":
                    if employee.can_hire(self):
                        name = "CEO - Hire"
                    elif employee.can_fire(self.salary, self.employees):
                        name = "CEO - Fire"
                    elif random.random() > 0.8:
                        name = "CEO - Give Bonus"
                case "Intern":
                    if random.random() > 0.4:
                        name = "Intern - Learn"
                    elif random.random() > 0.6:
                        name = "Intern - Errand"
                case "Senior":
                    if random.random() > 0.4:
                        name = "Senior - Mentor"
                case "Manager":
                    if random.random() > 0.55:
                        name = "Manager - Manage"
            if name is not None:
                self.task_list.insert(0, Task("Unique", name, "", 1))
    
    def prioritize_tasks(self):
        priorities = {"Buy": 1, "Sell": 2, "Store": 3, "Unique": 4}
        choice = input("Set priorities for the day? (y/n): ").lower()

        if choice == "y":
            print("\nSet priorities:")
            print("Buy: 0 = delete all Buy tasks")
            print("Sell: 5 = boost Sell task frequency")
            print("Others: 1-4 (unique)\n")

            for task in priorities:
                while True:
                    try:
                        prio = int(input(f"{task} priority: "))
                        # BUY RULE
                        if task == "Buy":
                            if prio == 0:
                                priorities[task] = 0
                                print("⚠ Buy tasks will be removed today.")
                                break
                            elif 1 <= prio <= 4:
                                priorities[task] = prio
                                break
                            else:
                                print("Buy must be 0 or 1-4.")
                        # SELL RULE
                        elif task == "Sell":
                            if prio == 5:
                                priorities[task] = 5
                                print("⬆ Sell tasks boosted.")
                                break
                            elif 1 <= prio <= 4:
                                priorities[task] = prio
                                break
                            else:
                                print("Sell must be 1-5 (5 = boost).")
                        # NORMAL RULES
                        else:
                            if 1 <= prio <= 4:
                                if prio not in priorities.values():
                                    priorities[task] = prio
                                    break
                                else:
                                    print("Priority already used.")
                            else:
                                print("Must be 1-4.")

                    except ValueError:
                        print("Enter a number.")
        else:
            print("Default task priorities set.")
        if priorities.get("Sell") == 5:
            self.generate_sell_task(order_spike=True)
        self.task_list = sorted(self.task_list, key=lambda x: priorities.get(x.type, 99))

    def do_task(self, employee):
        """
        Advances progress on the task assigned to a specific employee by their speed stat.

        If the task is completed (progress >= duration), it is moved to completed_tasks,
        the employee's task count is incremented, and they are marked as free.

        Args:
            employee (Employee): The employee whose task progress should be updated.
        """

        for task in self.doing_tasks[:]:
            if task.assigned_to == employee:
                employee.progress_task(task)
                remaining_ratio = min(task.progress, task.duration) / task.duration
                print(f"{employee.name} is progressing in \"{task.type} - {task.name.title()}\". Progress: {formatting.progress_bar(remaining_ratio)}")
                if task.progress >= task.duration:
                    self.completed_tasks.append(task)
                    self.doing_tasks.remove(task)
                    employee.tasks_completed += 1
                    employee.working = False
                    print(
                        f"{employee.name} has completed \"{task.type} - {task.name.title()}\"")
                    if task.type == "Unique":
                        match task.name:
                            case "Intern - Learn":
                                employee.learn()
                            case "Intern - Errand":
                                employee.random_errand()
                            case "Senior - Mentor":
                                employee.mentor(self.employees)
                            case "Manager - Manage":
                                employee.manage(self.employees)
                            case "CEO - Hire":
                                employee.hire(self.empgen, self.company)
                            case "CEO - Fire":
                                employee.fire(
                                    self.salary, self.employees, self.company, self.empgen)
                            case "CEO - Give Bonus":
                                employee.give_bonus(
                                    self.employees, self.salary)
                    break

    def overtime_check(self, day):
        """
        Processes unfinished tasks at the end of the workday as overtime.

        Any task still in progress when the day ends is automatically completed.
        Overtime hours are recorded in the attendance system for potential salary bonuses.

        Args:
            attendance (Attendance): The attendance system to log overtime hours.
            day (int): The current simulation day.
        """

        for task in self.doing_tasks[:]:
            employee = task.assigned_to
            if employee is None:
                continue
            remaining = (task.duration - task.progress) // employee.speed
            self.attendance.records[day][employee.name]["overtime_hours"] = remaining
            hours_worked = self.attendance.records[day][employee.name].get("hours_worked", 0)
            hours_worked += remaining
            self.attendance.records[day][employee.name]["hours_worked"] = hours_worked
            print(f"{employee.name} worked overtime  for {remaining} hours to complete \"{task.type} - {task.name.title()}\".")
            self.completed_tasks.append(task)
            self.doing_tasks.remove(task)

    def complete_task(self):
        """
        Applies the real-world effects of all completed tasks to the inventory and cash.

        - Buy tasks: deduct item cost from cash and add item to the store buffer.
        - Sell tasks: remove item from inventory and add 20% profit to cash.
        - Store tasks: move items from the store buffer into actual inventory.

        Args:
            inventory (Inventory): The inventory system to update.
        """
        self.task_comp_today = 0
        for task in self.completed_tasks[:]:
            match task.type:
                case "Buy":
                    self.store_list.append(
                        {"name": task.name, "size": task.size, "quantity": 1})
                    self.inventory.cash -= self.inventory.get_price(
                        task.name, task.size)
                    self.completed_tasks.remove(task)
                case "Sell":
                    self.inventory.remove_item(task.name, task.size, 1)
                    # sell for 20% profit
                    self.inventory.cash += self.inventory.get_sell_price(
                        task.name, task.size)
                    self.completed_tasks.remove(task)
                case "Store":
                    for item in self.store_list:
                        if item["name"] == task.name and item["size"] == task.size:
                            self.inventory.add_item(
                                task.name, task.size, item["quantity"])
                            self.store_list.remove(item)
                            break
                    self.completed_tasks.remove(task)
            self.task_comp_today += 1

    def task_to_employee_ratio_check(self):
        """
        Warns the player if there are too many tasks per employee.

        Triggers a warning if the ratio of unassigned tasks to employees exceeds 3,
        suggesting the player should hire more staff via the CEO Panel.

        Args:
            employees_list (list): Full list of company employees.
        """

        if len(self.task_list) / len(self.employees) > 3:
            print(f"\n{'-' * 70}\nYou have too many tasks per employee. Consider hiring more employees, through the CEO Panel.\n{'-' * 70}\n")
            return True  # True if ratio is bad
        else:
            return False

    def __str__(self):
        output = f"""
{'=' * 70}
{'TASKS FOR THE DAY':^70}
{'=' * 70}
{'Type':<10} {'Name':<15} {'Size':<10} {'Duration':>10} {'Assigned To':<20}
{'=' * 70}
"""

        for task in self.task_list:
            assigned = task.assigned_to.name if task.assigned_to else "Unassigned"

            output += f"{task.type:<10} {task.name.title():<15} {task.size:<10} {task.duration:>10} {assigned:<20}\n"

        output += '=' * 70 + "\n"

        return output