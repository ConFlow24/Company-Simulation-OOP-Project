#main simulation engine, responsible for generating days and managing the flow of the simulation
from attendance_salary import *
from company import Company
from CEO_Panel import *
from employee_generator import EmpGen
from task_generator import TaskGen


class mainSimulationEngine:
    def sim_engine(day, employees, control_type):#loop in main.py
        print(f"Day {day}")
        #generate attendance for each employee
        for employee in employees:
            Attendance.clock_in(day, employee.name)
        print("Attendance for the day:")
        Attendance.show_attendance()

        #tasks

        #weighted random for how many tasks to generate for today
        #insert function to generate tasks for the day
        #display all tasks
        if control_type == "Auto":
            pass
            #randomly assign all tasks to all employees
        elif control_type == "Manual":
            pass
            #manually assign tasks



        #finish day

            

        


            
