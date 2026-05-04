import random


class Employee:
    """
    Represents a company employee with attributes like role, pay, and performance stats.
    Serves as the base class for Manager, CEO, Intern, and Senior.
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
        # tasks multiple of 5, never level up more than once, not level up when no tasks complete
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
