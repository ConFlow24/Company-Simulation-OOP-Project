#main simulation engine, responsible for generating days and managing the flow of the simulation

from Classes.events import Event

class main_simulation_engine:
    def __init__(self):
        self.event_system = Event()

    def sim_engine(self, day, employees, control_type, company, Attendance, TaskGen, inventory, salary):#loop in main.py
        print(f"\nDay {day}\n")
        #generate attendance for each employee
        for employee in employees:
            Attendance.clock_in(day, employee.name, employee.punctuality)
        Attendance.show_attendance(day)
        
        self.event_system.random_productivity(employees)

        #tasks
        TaskGen.generate_buy_task(employees)
        TaskGen.generate_store_task()
        TaskGen.generate_sell_task(inventory, order_spike=self.event_system.check_order_spike())
        TaskGen.show_tasks()
        match control_type:
            case "Auto":
                #work for 8 hours
                TaskGen.task_to_employee_ratio_check(employees)
                TaskGen.assign_task(employees, Attendance, day)
                print(f"""{'=' * 70}
{'DAY EVENTS':^70}
{'=' * 70}""")
                for _ in range(8):
                    for employee in employees:
                        TaskGen.do_task(employee)
                TaskGen.overtime_check(Attendance, day)
                TaskGen.complete_task(inventory)
                company.upgrade_employee(day)
                TaskGen.task_to_employee_ratio_check(employees)
            case "Manual":
                TaskGen.task_to_employee_ratio_check(employees)
                TaskGen.assign_task_manual(employees, Attendance, day, company)
                print(f"""{'=' * 70}
{'DAY EVENTS':^70}
{'=' * 70}""")
                for i in range(8):
                    for employee in employees:
                        TaskGen.do_task(employee)
                        if not employee.working:
                            if TaskGen.task_list:
                                TaskGen.assign_task_manual_individual(employee)
                TaskGen.overtime_check(Attendance, day)
                TaskGen.complete_task(inventory)
                company.upgrade_employee(day)
                TaskGen.task_to_employee_ratio_check(employees)
                
        self.event_system.restore_productivity(employees)

        #show End of day menu


        #finish day
