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
    def __init__(self, name, pay, role="Manager", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0, working=False):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed)

    def manage(self):
        print(f"{self.name} is managing.")


class CEO(Employee):
    def __init__(self, name, pay, role="CEO", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed)


class Intern(Employee):
    def __init__(self, name, pay, role="Intern", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0, working=False):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed, working)

    def learn(self):
        print(f"{self.name} is learning.")


class Senior(Employee):
    def __init__(self, name, pay, role="Senior", speed=1, punctuality=1,
                 total_hours=0, tasks_completed=0, working=False):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, tasks_completed)

    def mentor(self):
        print(f"{self.name} is mentoring.")
