#main simulation engine, responsible for generating days and managing the flow of the simulation
from Classes.attendance_salary import Attendance
from Classes.task_generator import TaskSystems as TaskGen

class main_simulation_engine:
    def sim_engine(self, day, employees, control_type, company):#loop in main.py
        print(f"Day {day}")
        #generate attendance for each employee
        for employee in employees:
            Attendance.clock_in(day, employee.name)
        print("Attendance for the day:")
        Attendance.show_attendance()

        #tasks
        TaskGen.generate_buy_task(employees)
        TaskGen.generate_store_task(employees)
        TaskGen.generate_sell_task(employees)
        print("Tasks for the day:")
        TaskGen.show_tasks()
        match control_type:
            case "Auto":
                #work for 8 hours
                TaskGen.assign_task(employees, Attendance, day)
                for i in range(8):
                    for employee in employees:
                        TaskGen.do_task(employee)
                TaskGen.overtime_check(employees, Attendance, day)
                TaskGen.complete_task()
            case "Manual":
                TaskGen.assign_task_manual(employees, Attendance, day, company)
                for employee in employees:
                    if employee.working == False:
                        TaskGen.assign_task_manual(employees, Attendance, day, company)
                    else:
                        TaskGen.do_task(employee)
                TaskGen.overtime_check(employees, Attendance, day)
                TaskGen.complete_task()
                
        #show End of day menu
        

        #finish day
