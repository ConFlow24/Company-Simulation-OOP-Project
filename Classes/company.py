class Company:
    """
    This class handles the main company data and operations, such as employee management, daily reports, 
    and interactions with the inventory and salary systems.

    Attributes:
        name (str): The name of the company.
        day (int): Internal day counter (tracked externally in main.py).
        employees (list): List of all current Employee objects in the company.
        attendance (Attendance): Reference to the shared Attendance system.
        salary (Salary): Reference to the shared Salary system.
        inventory (Inventory): Reference to the shared Inventory system.
        daily_log (list): Reserved for future daily event logging.
    """

    def __init__(self, name, attendance, salary, inventory):
        """
        Initializes the Company with a name and references to other systems.

        Args:
            name (str): The name of the company.
            attendance (Attendance): The shared Attendance system instance.
            salary (Salary): The shared Salary system instance.
            inventory (Inventory): The shared Inventory system instance.
        """

        self.name = name
        self.day = 0
        self.employees = []
        self.attendance = attendance
        self.salary = salary
        self.inventory = inventory
        self.daily_log = []

    def add_employee(self, employee):
        """
        Adds employee objects to the company's employee list.

        Args:
            employee (Employee): The Employee object to be added to the company.
        """

        self.employees.append(employee)

    def remove_employee(self, name, emp_gen):
        """
        Removes an employee from the company based on their name.

        Args:
            Same as the get_employee function but it removes the employee from the company instead of returning it.
        """

        employee = self.get_employee(name)
        if employee:
            self.employees.remove(employee)
            emp_gen.employees.remove(employee)

    def get_employee(self, name):
        """
        Retrieves an employee object based on their name.

        Args:
            Same as the remove_employee function but it returns the employee object instead of removing it.

        """
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def get_employee_input(self, prompt, options):
        """
        Asks the user to select an item from a numbered list.

        Used thoughout the program for various employee selection prompts.

        Args:
            prompt (str): The input prompt shown to the user.
            options (list): The list of options to choose from.
        """

        while True:
            try:
                choice = int(input(prompt))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                print("Invalid choice.")
            except ValueError:
                print("Invalid input.")

    def list_employees(self):
        """
        This function prints all the employees in the company, along with their role and pay, in a formatted table.
        """

        print("\n" + "=" * 70)
        print(f"{'EMPLOYEES':^70}")
        print("=" * 70)
        print(
            f"{'#':<4} {'Name':<18} {'Role':<12} {'Pay':>10} {'Speed':>10} {'Punctuality':>11}")
        print("=" * 70)
        for i, emp in enumerate(self.employees, 1):
            print(
                f"{i:<4} {emp.name:<18} {emp.role:<12} {emp.pay:>10,} {emp.speed:>10} {emp.punctuality:>11}")
        print("=" * 70 + "\n")

    def list_available_employees(self, available_emps):
        """
        Displays a formatted table of only available (not working, not absent) employees.

        Args:
            available_emps (list): Filtered list of available Employee objects.
        """

        print("\n" + "=" * 70)
        print(f"{'AVAILABLE EMPLOYEES':^70}")
        print("=" * 70)
        print(
            f"{'#':<4} {'Name':<18} {'Role':<12} {'Pay':>10} {'Speed':>10} {'Punctuality':>11}")
        print("=" * 70)
        for i, emp in enumerate(available_emps, 1):
            print(
                f"{i:<4} {emp.name:<18} {emp.role:<12} {emp.pay:>10,} {emp.speed:>10} {emp.punctuality:>11}")
        print("=" * 70 + "\n")

    def advance_day(self):  # unused
        self.day += 1

    def run_daily_attendance(self):  # unused
        for emp in self.employees:
            if emp.role != "CEO":
                self.attendance.clock_in(self.day, emp)
                self.attendance.clock_out(self.day, emp)

    def show_daily_report(self):
        print(f"\n--- Day {self.day} Report ---")
        print(f"Cash: {self.inventory.cash:,.2f}")

    def show_full_report(self, day):
        """
        Displays a comprehensive report of the company's status, including financials and employee details.
        """
        stock, price = self.inventory.total_stock_and_price()
        print(f"""\n{"=" * 70}
{'COMPANY REPORT':^70}
{"=" * 70}
{'Company Name:':<20} {self.name}
{'Days Simulated:':<20} {day}
{'Total Employees:':<20} {len(self.employees)}
{'Cash:':<20} {self.inventory.cash:,.2f}
{'Items in Inventory:':<20} {stock}
{'Inventory Value:':<20} {price:,.2f}

{"=" * 70}
{'EMPLOYEE LIST':^70}
{"=" * 70}
{'Name':<30} {'Role':<20} {'Pay':>18}
{"-" * 70}""")
        for emp in self.employees:
            print(f"{emp.name:<30} {emp.role:<20} {emp.pay:>18,.2f}")
        print("=" * 70 + "\n")

    def upgrade_employee(self, day):
        """
        Runs end-of-day upgrades for all employees.

        For each employee, this method:
            - Checks and applies stat upgrades (speed level-up)
            - Checks eligibility for role promotion
            - Applies any salary bonuses for overtime
            - Applies salary deductions for excessive lates or absences

        Args:
            day (int): The current day, used for attendance bonus checks.
        """

        for employee in self.employees:
            employee.upgrade_stats()
            employee.check_promotion()
            self.salary.apply_bonus(employee, self.attendance, day)
            self.salary.apply_deduction(employee, self.attendance)
