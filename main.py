"""Company Simulation Game - Main Module"""

from Classes.employee import EmpGen
from Classes.main_simulation_engine import main_simulation_engine
from Classes.attendance_salary import Attendance, Salary
from Classes.company import Company
from Classes.CEO_Panel import CEOPanel
from Classes.task_generator import TaskSystems as TaskGen
from Classes.inventory import Inventory

def main():
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


  #constructors
  attendance = Attendance()
  salary = Salary(attendance)
  empgen = EmpGen()
  inventory = Inventory()
  company = Company(name, attendance, salary, inventory)
  CEOpanel = CEOPanel(company, empgen, inventory)
  taskgen = TaskGen(attendance, company, inventory, salary, empgen)
  main_sim = main_simulation_engine(company.employees, company, attendance, taskgen, inventory, salary, empgen, CEOpanel)


  main_simulation_engine.run()

if __name__ == "__main__":
    main()
