from Classes.employee import Employee
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
    def __init__(self, first_names=first_names, last_names=last_names, role_pay_hash=role_pay_hash):
        self.employees = []
        self.role_pay_hash = role_pay_hash
        self.first_names = first_names
        self.last_names = last_names
        self.roles = ["Employee", "Manager", "Intern", "Senior"]
        self.weights = [0.71, 0.09, 0.1, 0.1]

    def get_role(self):
        if self.employees == []:
            return "CEO"  # first employee is CEO
        return random.choices(self.roles, weights=self.weights, k=1)[0]

    def generate_employee(self, amount, company):
        for _ in range(amount):
            role = self.get_role()
            min_pay, max_pay = self.role_pay_hash[role]
            random_name = f"{random.choice(self.first_names)} {random.choice(self.last_names)}"
            pay = random.randint(min_pay, max_pay) // 1000 * 1000
            speed = random.randint(1, 5)
            punctuality_values = [5, 4, 3, 2, 1]
            weights = [0.05, 0.75, 0.10, 0.05, 0.05]
            puncuality = random.choices(
                punctuality_values, weights=weights, k=1)[0]
            emp = Employee(random_name, role, pay, speed, puncuality)
            self.employees.append(emp)
            company.add_employee(emp)

    def print_employees(self):
        print(f"{'Name':<20} | {'Role':<10} | {'Pay per Year':<10}")
        print(f"{'-'*19} | {'-'*10} | {'-'*10}")
        for employee in self.employees:
            print(f"{employee.name:<20} | {employee.role:<10} | {employee.pay:<10}")
