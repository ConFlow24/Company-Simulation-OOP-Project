class Employee:
    def __init__(self, name = "John Doe", employee_id = 0001, role = "Employee", pay = 50000):#could add more
        self.name = name
        self.employee_id = employee_id
        self.role = role
        self.pay = pay
        
    def work(self):
        pass

    def complete_task(self):
        pass
    
    def clock_in(self):
        pass
        
    def clock_out(self):
        pass

    def show_info(self):
        pass

class Manager(Employee):
    def __init__(self, name, employee_id, role, pay):
        super().__init__(name, employee_id, role, pay)
    def manage(self):
        pass

class CEO(Employee):
    def __init__(self, name, employee_id, role, pay):
        super().__init__(name, employee_id, role, pay)
    def make_decision(self):
        pass

class Intern(Employee):
    def __init__(self, name, employee_id, role, pay):
        super().__init__(name, employee_id, role, pay)
    def learn(self):
        pass

class Senior(Employee):
    def __init__(self, name, employee_id, role, pay):
        super().__init__(name, employee_id, role, pay)
    def mentor(self):
        pass
