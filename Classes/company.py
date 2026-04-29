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
    
    def get_employee_input(self, prompt, options):
        while True:
            try:
                choice = int(input(prompt))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                print("Invalid choice.")
            except ValueError:
                print("Invalid input.")

    def list_employees(self):
        print("\n--- Employees ---")
        print(f"{'#':<4} {'Name':<15} {'Role':<15} {'Pay':>10} {'Speed':>8} {'Punctuality':>12}")
        print("-" * 65)
        for i, emp in enumerate(self.employees, 0):
            print(f"{i:<4} {emp.name:<15} {emp.role:<15} {emp.pay:>10,} {emp.speed:>8} {emp.punctuality:>12}")
        print("\n")

    def list_available_employees(self, available_emps):
        print("\n--- Employees ---")
        print(f"{'#':<4} {'Name':<22} {'Role':<18} {'Pay':>8} {'Speed':>6} {'Punctuality':>11}")
        print("-" * 70)
        for i, emp in enumerate(available_emps, 1):
            print(f"{i:<4} {emp.name:<22} {emp.role:<18} {emp.pay:>8,} {emp.speed:>6} {emp.punctuality:>11}")

    def advance_day(self): # unused
        self.day += 1

    def run_daily_attendance(self): # unused
        for emp in self.employees:
            if emp.role != "CEO":
                self.attendance.clock_in(self.day, emp)
                self.attendance.clock_out(self.day, emp)

    def show_daily_report(self):
        print(f"\n--- Day {self.day} Report ---")
        print(f"Cash: {self.inventory.cash:,.2f}")

    def show_full_report(self, day):
        print(f"""
\n--- Company Report ---\n
Company Name: {self.name}
Days Simulated: {day}
Total Employees: {len(self.employees)}
Cash: {self.inventory.cash:,.2f}
Items in Inventory: {self.inventory.total_stock_and_price()[0]}
Invetory Price: {self.inventory.total_stock_and_price()[1]}
\n--- Employees ---\n""")

        for emp in self.employees:
            print(f"{emp.name} | {emp.role} | {emp.pay:,.2f} |")# Tasks: {emp.tasks_completed} | Late: {emp.late_count} | Absent: {emp.absent_count}, removed
        #add inventory report and task report here

    def upgrade_employee(self):
        for employee in self.employees:
            employee.upgrade_stats()
            employee.check_promotion()
