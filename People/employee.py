promotion_threshold = {"INTERN": 10, "EMPLOYEE": 20, "SENIOR": 35}

class Employee:
    def __init__(self, name="John Doe", role="Employee", pay=50000, speed=1, punctuality=1, total_hours=0, late_count=0, absent_count=0, tasks_completed=0):
        self.name = name
        self.role = role
        self.pay = pay
        self.speed = speed
        self.punctuality = punctuality
        self.total_hours = total_hours
        self.late_count = late_count
        self.absent_count = absent_count
        self.tasks_completed = tasks_completed

    def work(self):
        self.tasks_completed += 1
        print(f"{self.name} is working. Tasks completed: {self.tasks_completed}.")
        if self.tasks_completed >= promotion_threshold["SENIOR"]:
            print(f"{self.name} is ready for promotion to EMPLOYEE!")

class Manager(Employee):
    def __init__(self, name, pay, role="Manager", speed=1, punctuality=1,
                 total_hours=0, late_count=0, absent_count=0, tasks_completed=0):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, late_count, absent_count, tasks_completed)

    def manage(self):
        self.tasks_completed += 1

class CEO(Employee):
    def __init__(self, name, pay, role="Manager", speed=1, punctuality=1,
                 total_hours=0, late_count=0, absent_count=0, tasks_completed=0):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, late_count, absent_count, tasks_completed)


class Intern(Employee):
    def __init__(self, name, pay, role="Manager", speed=1, punctuality=1,
                 total_hours=0, late_count=0, absent_count=0, tasks_completed=0):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, late_count, absent_count, tasks_completed)

    def learn(self):
        self.tasks_completed += 1
        print(f"{self.name} is learning. Tasks completed: {self.tasks_completed}.")
        if self.tasks_completed >= promotion_threshold["INTERN"]:
            print(f"{self.name} is ready for promotion to EMPLOYEE!")


class Senior(Employee):
    def __init__(self, name, pay, role="Manager", speed=1, punctuality=1,
                 total_hours=0, late_count=0, absent_count=0, tasks_completed=0):
        super().__init__(name, role, pay, speed, punctuality,
                         total_hours, late_count, absent_count, tasks_completed)

    def mentor(self):
        self.tasks_completed += 1
        print(f"{self.name} is working. Tasks completed: {self.tasks_completed}.")
        if self.tasks_completed >= promotion_threshold["SENIOR"]:
            print(f"{self.name} is ready for promotion to MANAGER!")

