#runs the program
# Dito papasok kung paano gumagalaw ung attendance sa totoong buhay. 

from Classes.employee_generator import EmpGen
from Classes.main_simulation_engine import mainSimulationEngine



while True:
    try:
        weeks_to_simulate = int(input("Welcome to the company simulator! Input how many days you want to simulate(1-50): "))
        if 1 <= weeks_to_simulate <= 50:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 50.")
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    try:
        initial_comp_size = int(input("Welcome to the company simulator! Input how many employees to start with(5-10): "))
        if 5 <= initial_comp_size <= 10:
            EmpGen.generate_employee(initial_comp_size)
            EmpGen.print_employees()

            break
        else:
            print("Invalid input. Please enter a number between 5 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number.")

#insert main simulation engine here