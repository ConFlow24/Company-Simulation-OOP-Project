class Salary:

    def apply_bonus(self, employee, total_hours, original_salary):
        # If worked hours more than 12 hours add 15% for bonus.
        if total_hours > 12:
            employee.pay += 10000
        return original_salary

    def apply_deduction(self, employee):
        if employee.late_count > 6 or employee.absent_count > 3:
            employee.pay -= 10000
        pass

    def apply_monthly_bonus(self):
        # top 5 employees sa month may bonus
        pass

    def show_salary_report(self):
        # Show salary, bonuss, deductions, and totals.
        pass
