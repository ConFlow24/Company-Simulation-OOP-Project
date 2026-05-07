"""Company Simulation Game - Main Module"""

from Classes.employee import EmpGen
from Classes.main_simulation_engine import main_simulation_engine
from Classes.attendance_salary import Attendance, Salary
from Classes.company import Company
from Classes.CEO_Panel import CEOPanel
from Classes.task_generator import TaskSystems as TaskGen
from Classes.inventory import Inventory

main_simulation_engine = main_simulation_engine()
EmpGen = EmpGen()
CEOPanel = CEOPanel()
inventory = Inventory()
Attendance = Attendance()
TaskGen = TaskGen()
salary = Salary()


print("""
==========================================================
        WELCOME TO THE COMPANY SIMULATOR!
==========================================================
  You are the CEO of a newly founded company.
  Your goal is to manage employees, handle inventory,
  and make strategic decisions to grow your business.

  - Assign tasks to employees
  - Hire and fire staff
  - Buy and sell inventory
  - Grow your company day by day
  - Check your budget! You lose if you hit 0
  - Try to reach 1,000,000!

  Good luck, CEO!
==========================================================\n
""")
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
        day, EmpGen.employees, control_type, company, Attendance, TaskGen, inventory, salary, EmpGen)

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
                amount = int(
                    input("\nEnter number of days to automatically assign tasks: "))
                print(f"\nAuto Simulation set to {amount} day(s).")
                print(
                    "Select Option 1 (Start Next Day) to begin automatic simulation.")
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
