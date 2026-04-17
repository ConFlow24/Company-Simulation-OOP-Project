class Salary:
    def __init__(self):
        # Daily salary per employee per day
        self.salary_records = {}

        # Total salary per employees (whole month / 30 days)
        self.total_salary = {}

        # Tracks total hours worked per employee (for ranking)
        self.total_hours = {}

        # Tracks lates 
        self.late_count = {}

        # Tracks absences
        self.absent_count = {}

        # ourly rate
        self.hourly_rate = 100

    def compute_daily_salary(self, employee_id, attendance_record):
        pass
        
    def apply_bonus(self, employee_id, daily_hours, daily_salary):
        # If worked hours more than 12 hours add 15% for bonus.
        pass
        
    def apply_deduction(self, employee_id):
        # if late more than 5 or absences more than 3 apply 10% deduction sa salary.
        pass

    def update_salary(self, attendance):
        # for attendance and salary
        pass

    def apply_monthly_bonus(self):
        # top 5 employees sa month may bonus
        pass

    def show_salary_report(self):
        # Show salary, bonuss, deductions, and totals.
        pass
