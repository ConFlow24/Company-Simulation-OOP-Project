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

# the pay ranges for each roles and it generates random pay for each employee based on their role.
# it represents minimum and maximum pay for each role.
role_pay_hash = {
    "Employee": (50000, 70000),
    "Manager": (70000, 90000),
    "CEO": (90000, 150000),
    "Intern": (30000, 40000),
    "Senior": (80000, 120000)
}


class EmpGen:
    """
    This class is one of the most important classes in the simulation as it is
    responsible for generating employees at the start of the simulation.

    It also creates randomized names, roles, pay, speed, and punctuality based on weighted probabilities.
    The first employee is always the CEO.

    Attributes:
        employees (list): A list to store generated employee objects.
        role_pay_hash (dict): A dictionary for min and max pay.
        first_names (list): A list of first names to randomly pick from.
        last_names (list): Same to the first names list.
        roles (list): List for possible roles to assign (except CEO).
        weights (list): A list of weights corresponding to the likelihood of each role being assigned.
    """

    def __init__(self, first_names=first_names, last_names=last_names, role_pay_hash=role_pay_hash):
        self.employees = []
        self.role_pay_hash = role_pay_hash
        self.first_names = first_names
        self.last_names = last_names
        self.roles = ["Employee", "Manager", "Intern", "Senior"]
        # weighted for the employees except the CEO.
        self.weights = [0.71, 0.09, 0.1, 0.1]

    def get_role(self):
        """
        This function determines the role of the generated employee.
        The first employee is always the CEO, and the rest are randomly assigned based on weighted probbabiliyies.

        It returns a string representing the role of the employee to be generated.
        """

        if self.employees == []:
            return "CEO"  # first employee is CEO.
        return random.choices(self.roles, weights=self.weights, k=1)[0]

    def generate_employee(self, amount, company):
        """
        This function generates a specified number of employees and adds them to the company.

        Each employee gets a random name, role, pay, speed (1-5), and punctuality.

        Args:
            amount (int): The number of employees to generate.
            company (Company): The company object to which the generated employees will be added.
        """
        for _ in range(amount):
            role = self.get_role()
            min_pay, max_pay = self.role_pay_hash[role]
            random_name = f"{random.choice(self.first_names)} {random.choice(self.last_names)}"
            pay = random.randint(min_pay, max_pay) // 1000 * \
                1000  # round to nearest 1000
            speed = random.randint(1, 5)

            # 5 means most punctual, 1 means least punctual.
            punctuality_values = [5, 4, 3, 2, 1]
            weights = [0.05, 0.75, 0.10, 0.05, 0.05]
            punctuality = random.choices(
                punctuality_values, weights=weights, k=1)[0]
            emp = Employee(random_name, role, pay, speed, punctuality)
            self.employees.append(emp)
            company.add_employee(emp)

    def print_employees(self):
        """
        This function simply prints the list of employees, their role, and their pay in a beautiful format.
        """

        print(f"{'Name':<20} | {'Role':<10} | {'Pay per Year':<10}")
        print(f"{'-'*19} | {'-'*10} | {'-'*10}")
        for employee in self.employees:
            print(f"{employee.name:<20} | {employee.role:<10} | {employee.pay:<10}")
