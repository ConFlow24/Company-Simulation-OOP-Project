#main simulation engine, responsible for generating days and managing the flow of the simulation


class main_simulation_engine:
    def sim_engine(self, day, employees, control_type, company, Attendance, TaskGen, inventory, salary):#loop in main.py
        print(f"\nDay {day}\n")
        #generate attendance for each employee
        for employee in employees:
            Attendance.clock_in(day, employee.name, employee.punctuality)
        print("Attendance for", end=" ")
        Attendance.show_attendance(day)

        #tasks
        TaskGen.generate_buy_task(employees)
        TaskGen.generate_store_task()
        TaskGen.generate_sell_task(inventory)
        print("Tasks for the day:")
        TaskGen.show_tasks()
        match control_type:
            case "Auto":
                #work for 8 hours
                TaskGen.task_to_employee_ratio_check(employees)
                TaskGen.assign_task(employees, Attendance, day)
                for _ in range(8):
                    for employee in employees:
                        TaskGen.do_task(employee)
                TaskGen.overtime_check(employees, Attendance, day)
                TaskGen.complete_task(inventory)
                company.upgrade_employee()
            case "Manual":
                TaskGen.task_to_employee_ratio_check(employees)
                TaskGen.assign_task_manual(employees, Attendance, day, company)
                for i in range(8):
                    for employee in employees:
                        TaskGen.do_task(employee)
                        if not employee.working:
                            if TaskGen.task_list:
                                TaskGen.assign_task_manual_individual(employee)
                TaskGen.overtime_check(employees, Attendance, day)
                TaskGen.complete_task(inventory)
                company.upgrade_employee()
                TaskGen.task_to_employee_ratio_check(employees)
                
        #show End of day menu
        

        #finish day
