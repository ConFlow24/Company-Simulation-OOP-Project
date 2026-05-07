# main simulation engine, responsible for generating days and managing the flow of the simulation

from Classes.events import Event


class main_simulation_engine:
    """
    Coordinates the full flow of each simulation day — attendance, events,
    task generation, work execution, and end-of-day upgrades.
    """

    def __init__(self):
        # Initialize the event system to manage random events.
        self.event_system = Event()

    def sim_engine(self, day, employees, control_type, company, Attendance, TaskGen, inventory, salary, empgen):
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
Day {day}
{'=' * 70}""")

        # generate attendance for each employee
        for employee in employees:
            Attendance.clock_in(day, employee.name, employee.punctuality)
        Attendance.show_attendance(day)

        self.event_system.random_productivity(
            employees)  # for random speed applier

        # generate tasks for the day
        TaskGen.generate_buy_task(employees)
        TaskGen.generate_store_task()  # stores items waiting from buy tasks
        TaskGen.generate_sell_task(
            inventory, order_spike=self.event_system.check_order_spike())
        TaskGen.generate_unique_task(employees, TaskGen, salary)
        TaskGen.show_tasks()

        match control_type:
            case "Auto":
                TaskGen.task_to_employee_ratio_check(employees)
                # auto-asssign tasks based on employee stats.
                TaskGen.assign_task(employees, Attendance, day)
                print(f"""{'=' * 70}
{'DAY EVENTS':^70}
{'=' * 70}""")
                for _ in range(8):  # simulate 8 hours of work
                    for employee in employees:
                        TaskGen.do_task(employee, TaskGen, employees, empgen, company, salary)
                        if not employee.working and TaskGen.task_list:
                            TaskGen.assign_task_single(
                                # assign new task if employee finished their task and there are still tasks left
                                employee, Attendance, day)
                # finish leftover tasks as overtime
                TaskGen.overtime_check(Attendance, day)
                # apply task results to inventory
                TaskGen.complete_task(inventory)

                for employee in employees:
                    employee.working = False  # reset working state for next day
                company.upgrade_employee(day)
                TaskGen.task_to_employee_ratio_check(employees)

            case "Manual":
                TaskGen.task_to_employee_ratio_check(employees)
                # manual task assignment with CEO input
                TaskGen.assign_task_manual(employees, Attendance, day, company)

                print(f"""{'=' * 70}
{'DAY EVENTS':^70}
{'=' * 70}""")
                for _ in range(8):  # simulate 8 hours of work
                    for employee in employees:
                        TaskGen.do_task(employee, TaskGen, employees, empgen, company, salary)
                        if not employee.working:
                            if TaskGen.task_list:
                                # assign new task if employee finished their task and there are still tasks left, with CEO input
                                TaskGen.assign_task_manual_individual(employee)
                # finish leftover tasks as overtime
                TaskGen.overtime_check(Attendance, day)
                # apply task results to inventory
                TaskGen.complete_task(inventory)
                company.upgrade_employee(day)
                TaskGen.task_to_employee_ratio_check(employees)

        # reset  speed modifiers after the day ends
        self.event_system.restore_productivity(employees)
