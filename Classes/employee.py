import random


class Employee:
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


class Manager(Employee):
    """
    This class represents a Manager role in the company simulation.
    It also inherits from the Employee class and uses the same attributes and methods,
    but has a specific method for managing tasks and teams.
    """

    def __init__(self, name, pay, role="Manager", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0, working=False):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed)

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

    def manage(self):
        print(f"{self.name} is managing.")


class CEO(Employee):
    """
    This class represents a CEO role in the company simulation.
    It also inherits from the Employee class and uses the same attributes and methods,
    but has a specific method for making strategic decisions.
    """

    def __init__(self, name, pay, role="CEO", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed)

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


class Intern(Employee):
    """
    This class represents an Intern role in the company simulation.
    It also inherits from the Employee class and uses the same attributes and methods,
    but has a specific method for learning and gaining experience.
    """

    def __init__(self, name, pay, role="Intern", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0, working=False):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed, working)

        # Same attributes as Employee, but with Intern-specific defaults.

    def learn(self):
        print(f"{self.name} is learning.")


class Senior(Employee):
    def __init__(self, name, pay, role="Senior", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0, working=False):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed)

        # Same attributes as Employee, but with Senior-specific defaults.

    def mentor(self):
        print(f"{self.name} is mentoring.")
