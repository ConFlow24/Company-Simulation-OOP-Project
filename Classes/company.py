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
        print("\n" + "=" * 70)
        print(f"{'EMPLOYEES':^70}")
        print("=" * 70)
        print(f"{'#':<4} {'Name':<18} {'Role':<12} {'Pay':>10} {'Speed':>10} {'Punctuality':>11}")
        print("=" * 70)
        for i, emp in enumerate(self.employees, 1):
            print(f"{i:<4} {emp.name:<18} {emp.role:<12} {emp.pay:>10,} {emp.speed:>10} {emp.punctuality:>11}")
        print("=" * 70 + "\n")

    def list_available_employees(self, available_emps):
        print("\n" + "=" * 70)
        print(f"{'AVAILABLE EMPLOYEES':^70}")
        print("=" * 70)
        print(f"{'#':<4} {'Name':<18} {'Role':<12} {'Pay':>10} {'Speed':>10} {'Punctuality':>11}")
        print("=" * 70)
        for i, emp in enumerate(available_emps, 1):
            print(f"{i:<4} {emp.name:<18} {emp.role:<12} {emp.pay:>10,} {emp.speed:>10} {emp.punctuality:>11}")
        print("=" * 70 + "\n")

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
        stock, price = self.inventory.total_stock_and_price()
        print("\n" +"=" * 70 +
f"\n{'COMPANY REPORT':^70}" +
"=" * 70 + f"""
{'Company Name:':<20} {self.name}
{'Days Simulated:':<20} {day}
{'Total Employees:':<20} {len(self.employees)}
{'Cash:':<20} {self.inventory.cash:,.2f}
{'Items in Inventory:':<20} {stock}
{'Inventory Value:':<20} {price:,.2f}\n""" +
"=" * 70 +
f"\n{'EMPLOYEE LIST':^70}\n" +
"=" * 70 +
f"\n{'Name':<30} {'Role':<20} {'Pay':>18}\n" + "-" * 70)
        for emp in self.employees:
            print(f"{emp.name:<30} {emp.role:<20} {emp.pay:>18,.2f}")
        print("=" * 70 + "\n")

    def upgrade_employee(self, day):
        for employee in self.employees:
            employee.upgrade_stats()
            employee.check_promotion()
            self.salary.apply_bonus(employee, self.attendance, day)
            self.salary.apply_deduction(employee, self.attendance)
