from collections import defaultdict

class Salary:
    def __init__(self, salary_record):
        self.salary_record = salary_record


    def apply_bonus(self, employee, total_hours, original_salary):
        # If worked hours more than 12 hours add 15% for bonus.
        if total_hours > 12:
            employee.pay += 1000
            self.salary_record[employee]["Bonuses"] += 1000

        return original_salary

    def apply_deduction(self, employee):
        if employee.late_count > 6 or employee.absent_count > 3:
            employee.pay -= 1000
            self.salary_record[employee]["Deductions"] -= 1000
        pass

    def apply_top5_bonus(self, top5_list, employees_list):
        # top 5 employees sa month may bonus
        for employee in top5_list:
            if employee in employees_list:
                employee.pay += 1000
                self.salary_record[employee]["Bonuses"] += 1000

    def apply_top5_deduct(self, bottom5_list, employees_list):
        # top 5 employees sa month may bonus
        for employee in bottom5_list:
            if employee in employees_list:
                employee.pay -= 1000
                self.salary_record[employee]["Deductions"] -= 1000

    def show_salary_report(self, employees_list):
        for employee in employees_list:
            print(f"""Current salary: {employee.pay}
Bonuses received over time: {self.salary_record[employee]["Bonuses"]}
Deductions received over time: {self.salary_record[employee]["Bonuses"]}""")
