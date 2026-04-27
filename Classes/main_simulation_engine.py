#main simulation engine, responsible for generating days and managing the flow of the simulation


class main_simulation_engine:
    def sim_engine(self, day, employees, control_type, company, Attendance, TaskGen, inventory, salary):#loop in main.py
        print(f"\nDay {day}\n")
        #generate attendance for each employee
        for employee in employees:
            Attendance.clock_in(day, employee.name)
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
                TaskGen.assign_task(employees, Attendance, day)
                for _ in range(8):
                    for employee in employees:
                        TaskGen.do_task(employee)
                TaskGen.overtime_check(employees, Attendance, day)
                TaskGen.complete_task(inventory)
            case "Manual":
                TaskGen.assign_task_manual(employees, Attendance, day, company)
                for _ in range(8):
                    for employee in employees:
                        TaskGen.do_task(employee)
                        if employee.working == False:
                            if not TaskGen.task_list:
                                break
                            TaskGen.assign_task_manual_individual(employee)
                TaskGen.overtime_check(employees, Attendance, day)
                TaskGen.complete_task(inventory)
                
        #show End of day menu
        

        #finish day
