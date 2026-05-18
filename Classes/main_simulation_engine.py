# main simulation engine, responsible for generating days and managing the flow of the simulation

import os
from Classes.events import Event


class main_simulation_engine:
    """
    Coordinates the full flow of each simulation day — attendance, events,
    task generation, work execution, and end-of-day upgrades.
    """

    def __init__(self, employees, company, Attendance, TaskGen, inventory, salary, empgen, CEOPanel):
        # Initialize the event system to manage random events.
        self.event_system = Event()
        #constructor params
        self.employees = employees
        self.company = company
        self.Attendance = Attendance
        self.TaskGen = TaskGen
        self.inventory = inventory
        self.salary = salary
        self.empgen = empgen
        self.CEOPanel = CEOPanel
        #other params
        self.auto_days = 0
        self.day = 1
        self.week = (self.day - 1) // 7 + 1
        match self.week:
            case 1:
                self.goal = 10_000
            case 2:
                self.goal = 11_000
            case 3:
                self.goal = 20_000
            case _:
                self.goal = 20_000 + (self.week - 3) * 5_000

    def _clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def sim_engine(self, control_type):
        """
        Runs a single simulation day from start to finish.

        Args:
            day (int): Current day number.
            employees (list): All company employees.
            control_type (str): 'Auto' or 'Manual' task assignment mode.
            company (Company): The player's company.
            Attendance (Attendance): Attendance tracking system.
            TaskGen (TaskSystems): Task generation and management system.
            inventory (Inventory): Company inventory.
            salary (Salary): Salary management system.
        """

        print(f"""\n{'=' * 70}
Day {self.day}
Week {self.week}
{'=' * 70}""")
        #failure/success check
        if self.day % 7 == 0:
            for emp in self.employees:
                salary_subtract = emp.pay // 52
                self.inventory.cash -= salary_subtract
            if self.inventory.cash <= self.goal:
                print(f"A week has passed. You have {self.inventory.cash}. You have not met the required cash for this week!\n Thank you for playing!")
                exit()
            elif self.inventory.cash >= self.goal:
                print(f"You have reached the goal for this week! Your new goal is {self.goal + 10000}")
        self.start_day_cash = self.inventory.cash
        # generate attendance for each employee
        for employee in self.employees:
            self.Attendance.clock_in(self.day, employee.name, employee.punctuality)
        self.Attendance.show_attendance(self.day)
        self.event_system.random_productivity(
            self.employees)  # for random speed applier

        # generate tasks for the day
        self.TaskGen.generate_buy_task(buy_spike=self.event_system.check_buy_spike())
        self.TaskGen.generate_store_task()  # stores items waiting from buy tasks
        self.TaskGen.generate_sell_task(order_spike=self.event_system.check_order_spike())
        self.TaskGen.generate_unique_task(self.day)
        self.TaskGen.prioritize_tasks()
        attendance_display = self.Attendance.show_attendance_str(self.day)
        task_display = str(self.TaskGen)

        match control_type:
            case "Auto":
                # auto-assign tasks based on employee stats.
                self.TaskGen.assign_task(self.day)
                print(f"""{'=' * 70}
            {'DAY EVENTS':^70}
            {'=' * 70}""")
                for i in range(1, 9):  # simulate 8 hours of work
                    for employee in self.employees:
                        self.TaskGen.do_task(employee)
                        if not employee.working and self.TaskGen.task_list:
                            self.TaskGen.assign_task_single(employee, self.day)
                            # assign new task if employee finished their task and there are still tasks left
                    print(self.TaskGen.show_work_hour(i))
                # finish leftover tasks as overtime
                self.TaskGen.overtime_check(self.day)
                # apply task results to inventory
                self.TaskGen.complete_task()
                self.company.upgrade_employee(self.day, self.empgen)
            case "Manual":
                # manual task assignment with CEO input
                self.TaskGen.assign_task_manual(self.day, attendance_display, task_display)

                print(f"""{'=' * 70}
{'DAY EVENTS':^70}
{'=' * 70}""")
                for i in range(1, 9):  # simulate 8 hours of work
                    for employee in self.employees:
                        self.TaskGen.do_task(employee)
                        if not employee.working:
                            if self.TaskGen.task_list:
                                # assign new task if employee finished their task and there are still tasks left, with CEO input
                                self.TaskGen.assign_task_manual_individual(employee, attendance_display, task_display)
                    print(self.TaskGen.show_work_hour(i))
                # finish leftover tasks as overtime
                self.TaskGen.overtime_check(self.day)
                # apply task results to inventory
                self.TaskGen.complete_task()
                self.company.upgrade_employee(self.day, self.empgen)

        # reset  speed modifiers after the day ends
        self.event_system.restore_productivity(self.employees)
        self.end_day_cash = self.inventory.cash



    def end_sim(self):
        tips = {
            5:  "TIP: Inventory piling up? Use the CEO Panel to manually sell items directly without needing a task.",
            6:  "TIP: Payday is tomorrow! Prioritize Sell tasks today to make sure you can cover salaries.",
            7:  "TIP: Payday! If you're short on cash, use CEO Panel > Inventory Options to sell items instantly.",
            10: "TIP: Employees level up every 8 tasks. Faster employees = tasks done in fewer hours = less overtime.",
            12: "TIP: Store tasks are easy to forget. If your inventory isn't growing, check if items are stuck in the store buffer.",
            14: "TIP: Payday again! Check cash after payroll in the daily report — if it's red, you need to sell more.",
            15: "TIP: Interns are cheap but slow. Once they hit 10 tasks, promote them to Employee for a big speed boost.",
            18: "TIP: Managers progress tasks 1.5x faster and can manage other employees mid-day. Worth promoting Seniors.",
            20: "TIP: Too many Buy tasks? You're spending cash without earning it. Prioritize Sell and Store tasks instead.",
            21: "TIP: Third payday! Your salary costs grow as you hire. Make sure your sell income is keeping up.",
            25: "TIP: Seniors can mentor Employees and Interns, temporarily boosting their speed. Unique tasks are worth it.",
            28: "TIP: If the same employee keeps getting deductions, the CEO can fire underperformers automatically.",
            30: "TIP: Weekly goals get harder each week. Focus on building inventory early so you have items ready to sell.",
        }

        if self.day in tips:
            print(f"\n  {tips[self.day]}")
        self.TaskGen.task_to_employee_ratio_check()
        self.company.show_daily_report(self.day, self.end_day_cash, self.start_day_cash, self.TaskGen.task_comp_today, self.goal)
        while True:
            End_day_choice = input(f"""
{'=' * 70}
{'END OF DAY MENU':^70}
{'=' * 70}
1. Start next day
2. Open CEO panel (Employee and Inventory Options)
3. View reports
4. View Inventory
5. View Employees
6. Enable Auto Simulation
7. Exit Simulation
{'=' * 70}

Input choice: """)

            match End_day_choice:
                case "1":
                    self._clear()
                    return self.day + 1
                    # start next day
                case "2":
                    self.CEOPanel.show_panel()
                case "3":
                    self.company.show_report(self.day)
                case "4":
                    print(self.inventory)
                case "5":
                    self.company.list_employees()
                case "6":
                    self.auto_days = int(
                        input("\nEnter number of days to automatically assign tasks: "))
                    print(f"\nAuto Simulation set to {self.auto_days} day(s).")
                    print(
                        "Select Option 1 (Start Next Day) to begin automatic simulation.")
                case "7":
                    print(f"""
=====================================
SIMULATION ENDED
=====================================
Company  : {self.company.name}
Days Run : {self.day}
Cash Left: {self.inventory.cash:,.2f}
Employees: {len(self.employees)}
=====================================
Thank you for playing!
=====================================
""")
                    exit()
                case _:
                    print("\nInput not in choices. Please try again.")


    def run(self):
        while True:
            try:
                initial_comp_size = int(input("How many employees to start with (5-10): "))
                if 5 <= initial_comp_size <= 10:
                    self.empgen.generate_employee(initial_comp_size, self.company)
                    self.company.list_employees()
                    break
                else:
                    print("Invalid input. Please enter a number between 5 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            control_type = "Auto" if self.auto_days > 0 else "Manual"
            if self.auto_days > 0:
                self.auto_days -= 1
            self.sim_engine(control_type)
            self.day = self.end_sim()
