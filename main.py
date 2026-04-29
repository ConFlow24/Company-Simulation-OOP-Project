# runs the program

from Classes.employee_generator import EmpGen
from Classes.main_simulation_engine import main_simulation_engine
from Classes.attendance_salary import Attendance
from Classes.attendance_salary import Salary
from Classes.company import Company
from Classes.CEO_Panel import CEOPanel
from Classes.employee_generator import EmpGen
from Classes.task_generator import TaskSystems as TaskGen
from Classes.inventory import Inventory


main_simulation_engine = main_simulation_engine()
EmpGen = EmpGen()
CEOPanel = CEOPanel()
inventory = Inventory()
Attendance = Attendance()
TaskGen = TaskGen()
salary = Salary()


print("\n--- Welcome to the Company Simulator! ---\n")
print("In this simulation, you will be managing a company, overseeing employees, and making strategic decisions to grow your business.")
name = input("\nEnter the name of your Company: ")
company = Company(name, Attendance, salary, inventory)


while True:
    try:
        initial_comp_size = int(
            input("How many employees to start with (5-10): "))
        if 5 <= initial_comp_size <= 10:
            EmpGen.generate_employee(initial_comp_size, company)
            company.list_employees()
            break
        else:
            print("Invalid input. Please enter a number between 5 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number.")

day = 1
control_type = "Manual"
auto_days = 0
while True:
    if auto_days == 0:
        control_type = "Manual"
    else:
        control_type = "Auto"
        auto_days -= 1

    main_simulation_engine.sim_engine(
        day, EmpGen.employees, control_type, company, Attendance, TaskGen, inventory, salary)

    while True:
        End_day_choice = input(f"""
{'=' * 70}
{'END OF DAY MENU':^70}
{'=' * 70}
1. Start next day
2. Open CEO panel
3. View reports
4. View Inventory
5. View Employees
6. Enable Auto Simulation
7. Exit Simulation
{'=' * 70}
Input choice: """)

        match End_day_choice:
            case "1":
                day += 1
                break
                # start next day
            case "2":
                CEOPanel.show_panel(company, inventory, EmpGen)
            case "3":
                company.show_full_report(day)
            case "4":
                inventory.show_inventory()
            case "5":
                company.list_employees()
            case "6":
                amount = int(input("\nEnter number of days to automatically assign tasks: "))
                auto_days = amount
            case "7":
                print(f"""
=====================================
   SIMULATION ENDED
=====================================
   Company  : {company.name}
   Days Run : {day}
   Cash Left: {inventory.cash:,.2f}
   Employees: {len(company.employees)}
=====================================
   Thank you for playing!
=====================================
""")
                exit()
            case _:
                print("\nInput not in choices. Please try again.")
