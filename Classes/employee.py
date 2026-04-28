# Already  done, pa-check if ok, ung check promotion i-call yan sa main.py
import random
promotion_threshold = {"Intern": 10,
                       "Employee": 20, "Senior": 35, "Manager": 999}


class Employee:
    def __init__(self, name="John Doe", role="Employee", pay=50000, speed=1, punctuality=1, total_hours=0, tasks_completed=0, working = False):
        self.name = name
        self.role = role
        self.pay = pay
        self.speed = speed
        self.punctuality = punctuality
        self.total_hours = total_hours
        self.tasks_completed = tasks_completed
        self.working = working

    def upgrade_stats(self):
        if self.tasks_completed % 5 == 0:
            self.speed += random.randint(1, 3)
            print(f"{self.name} leveled up!")

    def check_promotion(self):
        if self.role == "Intern" and self.tasks_completed >= promotion_threshold["Intern"]:
            choice = input(f"""{self.name} is ready for promotion!
Do you want to promote {self.name} to an Employee(y/n): """).lower()
            match choice:
                case "y":
                    self.role = "Employee"
                    print(f"{self.name} is now an Employee.")
                case "n":
                    print(f"You have not promoted {self.name}.")
        elif self.role == "Employee" and self.tasks_completed >= promotion_threshold["Employee"]:
            choice = input(f"""{self.name} is ready for promotion!
Do you want to promote {self.name} to an Senior(y/n): """).lower()
            match choice:
                case "y":
                    self.role = "Senior"
                    print(f"{self.name} is now a Senior.")
                case "n":
                    print(f"You have not promoted {self.name}.")
        elif self.role == "Senior" and self.tasks_completed >= promotion_threshold["Senior"]:
            choice = input(f"""{self.name} is ready for promotion!
Do you want to promote {self.name} to a Manager(y/n): """).lower()
            match choice:
                case "y":
                    self.role = "Manager"
                    print(f"{self.name} is now a Manager.")
                case "n":
                    print(f"You have not promoted {self.name}.")


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
