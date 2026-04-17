class Employee:
    def __init__(self, name = "John Doe", role = "Employee", pay = 50000, speed = 1, punctuality = 1, total_hours = 0, late_count = 0, absent_count = 0):#could add more
        self.name = name
        self.role = role
        self.pay = pay
        self.speed = speed
        self.punctuality = punctuality
        self.total_hours = total_hours
        self.late_count = late_count
        self.absent_count = absent_count

    def work(self):
        pass

    def complete_task(self):
        pass

    def show_info(self):
        pass

class Manager(Employee):
    def __init__(self, name, role, pay, speed = 1, punctuality = 1, total_hours = 0, late_count = 0, absent_count = 0):
        super().__init__(name, role, pay, speed, punctuality, total_hours, late_count, absent_count)
    def manage(self):
        pass

class CEO(Employee):
    def __init__(self, name, role, pay, speed = 1, punctuality = 1, total_hours = 0, late_count = 0, absent_count = 0):
        super().__init__(name, role, pay, speed, punctuality, total_hours, late_count, absent_count)
    def make_decision(self):
        pass

class Intern(Employee):
    def __init__(self, name, role, pay, speed = 1, punctuality = 1, total_hours = 0, late_count = 0, absent_count = 0):
        super().__init__(name, role, pay, speed, punctuality, total_hours, late_count, absent_count)
    def learn(self):
        pass

class Senior(Employee):
    def __init__(self, name, role, pay, speed = 1, punctuality = 1, total_hours = 0, late_count = 0, absent_count = 0):
        super().__init__(name, role, pay, speed, punctuality, total_hours, late_count, absent_count)
    def mentor(self):
        pass
