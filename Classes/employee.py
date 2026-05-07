from abc import ABC, abstractmethod

import random
from Classes.items import first_names, last_names, role_pay_hash


class Employee(ABC):
    """
    Base class representing a general employee in the company simulation.

    Serves as the parent class for all specific roles (Manager, CEO, Intern, Senior).
    Stores core employee attributes and handles stat upgrades and promotion checks.

    Attributes:
        name (str): Full name of the employee.
        role (str): Current job role (ex. Employee, Manager, Intern, Senior).
        pay (int): Monthly salary of the employee.
        speed (int): Work speed stat that affects task completion rate.
        punctuality (int): Punctuality rating from 1-5; affects attendance probability.
        total_hours (int): Accumulated total hours worked.
        tasks_completed (int): Total number of tasks the employee has finished.
        working (bool): Whether the employee is currently assigned to a task.
        last_levelup (int): Task count at which the employee last leveled up; prevents double leveling.
    """

    def __init__(self, name="John Doe", role="Employee", pay=50000, speed=1, punctuality=1, total_hours=0, tasks_completed=0, working=False):
        self.name = name
        self.role = role
        self.pay = pay
        self.speed = speed
        self.punctuality = punctuality
        self.total_hours = total_hours
        self.tasks_completed = tasks_completed
        self.working = working
        self.last_levelup = 0

    def upgrade_stats(self):
        """
        Increases the employee's speed stat when a level-up threshold is reached.

        Level-up occurs every 8 completed tasks. Uses last_levelup to ensure
        the employee only levels up once per threshold, even if called multiple times.
        """

        if self.tasks_completed % 8 == 0 and self.tasks_completed != self.last_levelup and self.tasks_completed != 0:
            self.speed += random.randint(1, 3)
            self.last_levelup = self.tasks_completed
            print(f"{self.name} leveled up!")

    def check_promotion(self):
        """
        This function checks if the employee is elogible for promotion 
        based on their current role and tasks completed.

        Promotion thresholds:
            - Intern → Employee: 10 tasks
            - Employee → Senior: 20 tasks
            - Senior → Manager: 35 tasks

        Prompts the CEO (user) to confirm or decline each promotion interactively.
        """

        promotion_threshold = {"Intern": 10,
                               "Employee": 20, "Senior": 35, "Manager": 999}
        if self.role == "Intern" and self.tasks_completed >= promotion_threshold["Intern"]:
            while True:
                choice = input(
                    f"{self.name} is ready for promotion! Promote to Employee? (y/n): ").lower()
                match choice:
                    case "y":
                        self.role = "Employee"
                        print(f"{self.name} is now an Employee.")
                        break
                    case "n":
                        print(f"You have not promoted {self.name}.")
                        break
                    case _:
                        print("Invalid input. Enter y or n.")
        elif self.role == "Employee" and self.tasks_completed >= promotion_threshold["Employee"]:
            while True:
                choice = input(
                    f"{self.name} is ready for promotion! Promote to Senior? (y/n): ").lower()
                match choice:
                    case "y":
                        self.role = "Senior"
                        print(f"{self.name} is now a Senior.")
                        break
                    case "n":
                        print(f"You have not promoted {self.name}.")
                        break
                    case _:
                        print("Invalid input. Enter y or n.")
        elif self.role == "Senior" and self.tasks_completed >= promotion_threshold["Senior"]:
            while True:
                choice = input(
                    f"{self.name} is ready for promotion! Promote to Manager? (y/n): ").lower()
                match choice:
                    case "y":
                        self.role = "Manager"
                        print(f"{self.name} is now a Manager.")
                        break
                    case "n":
                        print(f"You have not promoted {self.name}.")
                        break
                    case _:
                        print("Invalid input. Enter y or n.")
    @abstractmethod
    def progress_task(self, task):
        task.progress += self.speed * 1

class RegularEmployee(Employee):
    def __init__(self, name, pay, role="Employee", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0, working=False):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed, working)
    def progress_task(self, task):
        task.progress += self.speed * 1

class Manager(Employee):
    """
    This class represents a Manager role in the company simulation.
    It also inherits from the Employee class and uses the same attributes and methods,
    but has a specific method for managing tasks and teams.
    """

    def __init__(self, name, pay, role="Manager", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0, working=False):
        """
        Initializes a Manager with Manager-specific defaults.

        Args:
            name (str): Manager's full name.
            pay (int): Monthly salary.
            role (str): Defaults to 'Manager'.
            speed (int): Work speed stat. Defaults to 1.
            punctuality (int): Punctuality rating (1-5). Defaults to 1.
            total_hours (int): Total hours worked. Defaults to 0.
            tasks_completed (int): Tasks completed so far. Defaults to 0.
            working (bool): Whether currently on a task. Defaults to False.
        """

        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed, working)

    def progress_task(self, task):
        task.progress += self.speed * 1.5

    def manage(self, employees):
        #temporarily increase a specific group of employees' speed
        employee = random.choice(employees)
        employee.speed += 2
        print(f"{self.name} is managing {employee.name}. {employee.name} is temporarily working faster.")
    def stop_manage(self, employee):
        employee.speed -= 2


class Intern(Employee):
    """
    This class represents an Intern role in the company simulation.
    It also inherits from the Employee class and uses the same attributes and methods,
    but has a specific method for learning and gaining experience.
    """

    def __init__(self, name, pay, role="Intern", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0, working=False):
        #  Same attributes as Employee, but with Intern-specific defaults.
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed, working)
        
    def progress_task(self, task):
        task.progress += self.speed * 0.75

    def learn(self):
        #increase punctuality        
        if random.random() > 0.3:
            stat = random.choices(
            [self.punctuality, self.speed], [0.3, 0.7])[0]
            print(f"{self.name} is learning.", end = "")
            if stat == self.punctuality and self.punctuality < 5:
                self.punctuality += 1
                print(f"{self.name}'s puncuality increased.")
            else:
                self.speed += 1
                print(f"{self.name}'s speed increased.")
        else:
            print(f"{self.name} failed to learn anything.")

    def random_errand(self):
        #intern is sent on a random errand. useless task
        print(f"{self.name} was sent on a useless errand. Nothing of value was gained.")
        pass


class Senior(Employee):
    def __init__(self, name, pay, role="Senior", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0, working=False):
        # Same attributes as Employee, but with Senior-specific defaults.
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed, working)

    def progress_task(self, task):
        task.progress += self.speed * 1.25

    def mentor(self, employees):
        #choose an employee or intern and increase their speed
        temp_employee_list = list(employees)
        for employee in temp_employee_list[:]:
            if employee.role != "Employee" and employee.role != "Intern":
                temp_employee_list.remove(employee)
        employee = random.choice(temp_employee_list)
        employee.speed += 2
        print(f"{self.name} is mentoring {employee.name}.")
    
    def stop_mentor(self, employee):
        employee.speed -= 2
        

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
    def __init__(self):
        self.employees = []
        self.role_pay_hash = role_pay_hash
        self.first_names = first_names
        self.last_names = last_names
        self.roles = ["Employee", "Manager", "Intern", "Senior"]
        self.weights = [0.71, 0.09, 0.1, 0.1]

    def get_role(self):
        """
        This function determines the role of the generated employee.
        The first employee is always the CEO, and the rest are randomly assigned based on weighted probbabiliyies.

        It returns a string representing the role of the employee to be generated.
        """
        if self.employees == []:
            return "CEO"  # first employee is CEO
        return random.choices(self.roles, weights=self.weights)[0]

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
            pay = random.randint(min_pay, max_pay) // 1000 * 1000
            speed = random.randint(1, 5)
            punctuality_values = [5, 4, 3, 2, 1]
            weights = [0.05, 0.75, 0.10, 0.05, 0.05]
            punctuality = random.choices(
                punctuality_values, weights=weights)[0]
            match role:
                case "CEO": emp = CEO(random_name, pay, role, speed, punctuality)
                case "Employee": emp = RegularEmployee(random_name, pay, role, speed, punctuality)
                case "Intern": emp = Intern(random_name, pay, role, speed, punctuality)
                case "Senior": emp = Senior(random_name, pay, role, speed, punctuality)
                case "Manager": emp = Manager(random_name, pay, role, speed, punctuality)
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

class CEO(Employee):
    """
    This class represents a CEO role in the company simulation.
    It also inherits from the Employee class and uses the same attributes and methods,
    but has a specific method for making strategic decisions.
    """
    def __init__(self, name, pay, role="CEO", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0, working = False):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed, working)
        """
        Initializes the CEO with CEO-specific defaults.

        Args:
            name (str): CEO's full name.
            pay (int): Monthly salary.
            role (str): Defaults to 'CEO'.
            speed (int): Work speed stat. Defaults to 1.
            punctuality (int): Punctuality rating (1-5). Defaults to 1.
            total_hours (int): Total hours worked. Defaults to 0.
            tasks_completed (int): Tasks completed so far. Defaults to 0.
        """
    def progress_task(self, task):
        task.progress += self.speed * 1.5
    
    def can_hire(self, taskgen, employees):
        return taskgen.task_to_employee_ratio_check(employees)

    def hire(self, empgen, company):
        #do employee to task ratio check(from taskgen) and add an employee if triggers
        empgen.roles = ["Employee", "Intern"]
        empgen.weights = [0.8, 0.2]
        empgen.generate_employee(1, company)
        employee = empgen.employees[-1]
        print(f"{self.name} has hired {employee.name}.")
        #return original
        empgen.roles = ["Employee", "Manager", "Intern", "Senior"]
        empgen.weights = [0.71, 0.09, 0.1, 0.1]

    def can_fire(self, salary, employees):
        for employee in employees:
            if salary.salary_record[employee.name].get("Deductions", 0) > 7:
                return True
        return False

    def fire(self, salary, employees, company, empgen):
        #check total deductions from attedance.py if greater than 7 fire.
        for employee in employees:
            if salary.salary_record[employee.name].get("Deductions", 0) > 7:
                company.remove_employee(employee, empgen)
                print(f"{self.name} has fired {employee.name}.")
                return

    def give_bonus(self, employees, salary):
        #low chance to give a bonus, something like "Ceo felt happy today gave {employee} bonus!"
        employees_list = employees
        for employee in employees_list[:]:
                if employee.role == "CEO":
                    employees_list.remove(employee)
        employee = random.choice(employees_list)
        employee.pay += 1000
        salary.salary_record[employee.name]["Bonuses"] += 1000
        print(f"{self.name} felt happy today, gave {employee.name} a bonus!")