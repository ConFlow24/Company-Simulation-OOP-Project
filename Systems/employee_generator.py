from People.employee import Employee
import random

first_names = [
    "Liam", "Noah", "Ethan", "Mason", "Lucas", "Aiden", "Elijah", "James", "Benjamin", "Logan",
    "Olivia", "Emma", "Ava", "Sophia", "Isabella", "Alice", "Charlotte", "Amelia", "Harper", "Evelyn",
    "Henry", "Alexander", "Daniel", "Matthew", "Samuel", "Joseph", "David", "Carter", "Owen", "Wyatt",
    "John", "Jack", "Luke", "Jayden", "Dylan", "Levi", "Isaac", "Gabriel", "Julian", "Anthony"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores"
]

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
        return random.choices(roles, weights=weights, k=1)[0] #weighted randomness
    @classmethod
    def generate_employee(cls, amount):
        for _ in range(amount):
            role = cls.get_role()
            min_pay, max_pay = role_pay_hash[role]
            random_name = f"{random.choice(first_names)} {random.choice(last_names)}"
            cls.employees.append(Employee(random_name, role, random.randint(min_pay, max_pay)//1000*1000))
            #generates employee with random name, role based on weighted randomness, and pay based on role with some variability. Pay is rounded to the nearest 1000 for simplicity.
    @classmethod
    def print_employees(cls):
        print(f"{'Name':<20} | {'Role':<10} | {'Pay per Year':<10}\n {'-'*19} | {'-'*10} | {'-'*10} ")
        for employee in cls.employees:
            print(f"{employee.name:<20} | {employee.role:<10} | {employee.pay:<10}")
