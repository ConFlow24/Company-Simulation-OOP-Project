#main simulation engine, responsible for generating days and managing the flow of the simulation
from attendance_salary import *
from company import Company
from CEO_Panel import *
from employee_generator import EmpGen
from task_generator import TaskGen


class mainSimulationEngine:
    def sim_engine(day, employees, control_type):#loop in main.py
        company = Company()
        EmpGen = EmpGen()
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
                TaskGen.assign_task(employees, Attendance, day)
            case "Manual":
                pass
                #manually assign tasks
        #work for 8 hours
        for i in range(8):
            for employee in employees:
                TaskGen.do_task(employee)
        TaskGen.overtime_check(employees, Attendance, day)
        TaskGen.complete_task()

        # if control_type == "Auto":
        #     pass
        #     #randomly assign all tasks to all employees
        # elif control_type == "Manual":
        #     pass
        #     #manually assign tasks

        #show End of day menu
        while True:
            End_day_choice = input(f"""1. Start next day
2. Open CEO panel
3. View reports
4. View Inventory
5. View Employees
6. Enable Auto Simulation
7. Exit Simulation
Input choice: """)
            match End_day_choice:
                case "1":
                    break
                    #start next day
                case "2":
                    pass #CEO panel options
                case "3":
                    company.show_full_report()
                case "4":
                    company.inventory.show_inventory()
                case "5":
                    company.list_employees()
                case "6":
                    amount = int(input("Enter number of days to simulate: "))
                    return amount, "Auto"
                case "7":
                    exit()

        #finish day

            

        


            
