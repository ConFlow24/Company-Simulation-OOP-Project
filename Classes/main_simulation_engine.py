# main simulation engine, responsible for generating days and managing the flow of the simulation

from Classes.events import Event


class main_simulation_engine:
    """
    Coordinates the full flow of each simulation day — attendance, events,
    task generation, work execution, and end-of-day upgrades.
    """

    def __init__(self, employees, company, Attendance, TaskGen, inventory, salary, empgen, CEOPanel):
        # Initialize the event system to manage random events.
        self.event_system = Event()
        self.still_playing = False
        #other params
        self.employees = employees
        self.company = company
        self.Attendance = Attendance
        self.TaskGen = TaskGen
        self.inventory = inventory
        self.salary = salary
        self.empgen = empgen
        self.auto_days = 0
        self.CEOPanel = CEOPanel
        self.day = 1


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
{'=' * 70}""")
        #failure/success check
        if self.day % 7 == 0:
            for emp in self.employees:
                salary_subtract = emp.pay // 52
                self.inventory.cash -= salary_subtract
            if self.inventory.cash <= 0:
                print(f"A week has passed. You have {self.inventory.cash}. You have gone bankrupt!\n Thank you for playing!")
                exit()
            elif self.inventory.cash >= 1000000 and self.still_playing == False:#if true never get asked this again.
                while True:
                    choice = input(f"You've reached a million! Do you still want to play (y/n): ").lower()
                    match choice:
                        case "y":
                            print("You may now continue playing.")
                            self.still_playing = True
                            break
                        case "n":
                            print("Thank you for playing!")
                            exit()
                        case _:
                            print("Invalid choice.")
        start_day_cash = self.inventory.cash
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
        print(self.TaskGen)

        match control_type:
            case "Auto":
                self.TaskGen.task_to_employee_ratio_check()
                # auto-asssign tasks based on employee stats.
                self.TaskGen.assign_task(self.day)
                print(f"""{'=' * 70}
{'DAY EVENTS':^70}
{'=' * 70}""")
                for _ in range(8):  # simulate 8 hours of work
                    for employee in self.employees:
                        self.TaskGen.do_task(employee)
                        if not employee.working and self.TaskGen.task_list:
                            self.TaskGen.assign_task_single(employee, self.day)
                                # assign new task if employee finished their task and there are still tasks left
                                
                # finish leftover tasks as overtime
                self.TaskGen.overtime_check(self.day)
                # apply task results to inventory
                self.TaskGen.complete_task()

                for employee in self.employees:
                    employee.working = False  # reset working state for next day
                self.company.upgrade_employee(self.day, self.empgen)
                self.TaskGen.task_to_employee_ratio_check()

            case "Manual":
                self.TaskGen.task_to_employee_ratio_check()
                # manual task assignment with CEO input
                self.TaskGen.assign_task_manual(self.day)

                print(f"""{'=' * 70}
{'DAY EVENTS':^70}
{'=' * 70}""")
                for _ in range(8):  # simulate 8 hours of work
                    for employee in self.employees:
                        self.TaskGen.do_task(employee)
                        if not employee.working:
                            if self.TaskGen.task_list:
                                # assign new task if employee finished their task and there are still tasks left, with CEO input
                                self.TaskGen.assign_task_manual_individual(employee)
                # finish leftover tasks as overtime
                self.TaskGen.overtime_check(self.day)
                # apply task results to inventory
                self.TaskGen.complete_task()
                self.company.upgrade_employee(self.day, self.empgen)
                self.TaskGen.task_to_employee_ratio_check()

        # reset  speed modifiers after the day ends
        self.event_system.restore_productivity(self.employees)
        end_day_cash = self.inventory.cash
        print(f"Your total profits today: {end_day_cash - start_day_cash}.")



    def end_sim(self):
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
