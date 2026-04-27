class Company:
    def __init__(self, name, attendance, salary, inventory):
        self.name = name
        self.day = 0
        self.employees = []
        self.attendance = attendance
        self.salary = salary
        self.inventory = inventory
        self.daily_log = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, name):
        employee = self.get_employee(name)
        if employee:
            self.employees.remove(employee)

    def get_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def list_employees(self):
        print("\n--- Employees ---")
        for emp in self.employees:
            print(f"{emp.name} | {emp.role} | {emp.pay:,}")
        print("\n")

    def advance_day(self):
        self.day += 1

    def run_daily_attendance(self):
        for emp in self.employees:
            if emp.role != "CEO":
                self.attendance.clock_in(self.day, emp)
                self.attendance.clock_out(self.day, emp)

    def show_daily_report(self):
        print(f"\n--- Day {self.day} Report ---")
        print(f"Cash: {self.inventory.cash:,.2f}")

    def show_full_report(self):
        print(f"""
\n--- Company Report ---\n
Company Name: {self.name}
Days Simulated: {self.day}
Total Employees: {len(self.employees)}
Cash: {self.inventory.cash:,.2f}
\n--- Employees ---\n""")

        for emp in self.employees:
            print(f"{emp.name} | {emp.role} | {emp.pay:,.2f} |")# Tasks: {emp.tasks_completed} | Late: {emp.late_count} | Absent: {emp.absent_count}, removed
        #add inventory report and task report here
