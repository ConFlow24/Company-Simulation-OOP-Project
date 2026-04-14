from People.employee import Employee
from faker import Faker
import random

fake = Faker()
role_pay_hash = {
    "Employee": (50000, 70000),
    "Manager": (70000, 90000),
    "CEO": (90000, 150000),
    "Intern": (30000, 40000),
    "Senior": (80000, 120000)
}
class EmpGen:
    employees = []
    @staticmethod
    def get_role():
        if EmpGen.employees == []:
            return "CEO"#ensures that the first employee generated is a CEO
        roles = ["Employee", "Manager", "Intern", "Senior"]
        weights = [0.71, 0.09, 0.1, 0.1]
        return random.choices(roles, weights=weights, k=1)[0]
    @classmethod
    def generate_employee(cls, amount):
        for _ in range(amount):
            role = cls.get_role()
            min_pay, max_pay = role_pay_hash[role]
            cls.employees.append(Employee(fake.name(), role, random.randint(min_pay, max_pay)//1000*1000))
        
    @classmethod
    def print_employees(cls):
        print(f"{'Name':<20} | {'Role':<10} | {'Pay per Year':<10}\n {'-'*19} | {'-'*10} | {'-'*10} ")
        for employee in cls.employees:
            print(f"{employee.name:<20} | {employee.role:<10} | {employee.pay:<10}")
