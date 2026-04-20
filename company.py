# not real

from Systems.attendance import Attendance
from Systems.salary import Salary
from Systems.inventory import Inventory


class Company:
    def __init__(self, name, starting_cash=1000000):
        self.name = name
        self.day = 0
        self.employees = []
        self.attendance = Attendance()
        self.salary = Salary()
        self.inventory = Inventory(starting_cash)
        self.daily_log = []

    # Employee managem
    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, name):
        employee = self.get_employee(name)
        if employee:
            self.employees.remove(employee)

    def get_employee(self, employee_name):
        for emp in self.employees:
            if emp.name == employee_name:
                return emp
        return None

    def list_employees(self):
        print("\n--- Employees ---")
        for emp in self.employees:
            print(f"{emp.name} - {emp.role} - ${emp.pay}")
