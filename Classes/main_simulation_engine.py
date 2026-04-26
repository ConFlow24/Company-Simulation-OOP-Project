#main simulation engine, responsible for generating days and managing the flow of the simulation
from attendance_salary import *
from company import Company
from CEO_Panel import *
from employee_generator import EmpGen
from task_generator import TaskGen
from inventory import Inventory

class main_Simulation_engine:
    def sim_engine(day, employees, control_type):#loop in main.py
        company = Company()
        EmpGen = EmpGen()
        CEOPanel = CEOPanel()
        inventory = Inventory()
        company.employees = employees
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
