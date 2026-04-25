import random
from collections import defaultdict
class Attendance:
    def __init__(self):
        # Yung init, purpose niya mag-store ng employee id, status (present or not), hours worked, late, overtime hours using dictionary.
        self.records = defaultdict(lambda: defaultdict(dict)) # per employee has status, hours worked, overtime hours. defaultdict automatically makes keys for no errors, lambda para pwede nested dicts
        # has total lates and absences for each employee for salary deductions and bonuses.
    def clock_in(self, day, employee_name):# day is from day generator when implemented into the manin program
        attendance_list = ["Present", "Late", "Absent"]
        weights = [0.9, 0.07, 0.03]
        attendance = random.choices(attendance_list, weights=weights, k=1)[0] #weighted randomness
        self.records[day][employee_name] = {
            "status": attendance
        }
        match attendance:
            case "Present":
                self.records[day][employee_name]["hours_worked"] = 8
            case "Late":
                self.records[day][employee_name]["hours_worked"] = 8- random.randint(1, 2)
                self.records[employee_name]["late_count"] = self.records[employee_name].get("late_count", 0) + 1 # adds to employee late count for salary deductions and bonuses
            case "Absent":
                self.records[day][employee_name]["hours_worked"] = 0
                self.records[employee_name]["absent_count"] = self.records[employee_name].get("absent_count", 0) + 1 # adds to employee absent count for salary deductions
        self.records[day][employee_name]["total_hours"] = self.records[day][employee_name].get("total_hours", 0) + self.records[day][employee_name]["hours_worked"] # adds to employee total hours for salary bonuses and ranking

    # def clock_out(self, day, employee_name):
    #     if self.records[day][employee_name]["status"] == "Present" or self.records[day][employee_name]["status"] == "Late":
    #         overtime_chance = random.random()
    #         if overtime_chance < 0.1:  # 10% chance of working overtime
    #             self.records[day][employee_name]["overtime_hours"] = random.randint(1, 4)
    #             self.records[day][employee_name]["hours_worked"] += self.records[day][employee_name]["overtime_hours"]
    #         else:
    #             self.records[day][employee_name]["overtime_hours"] = 0
    #     else:
    #         self.records[day][employee_name]["overtime_hours"] = 0
    #outdated sa tasks system na lang overitme

    def get_total_work_hours(self, employee_name):
        total_hours = 0
        for day, employees in self.records.items():
            if employee_name in employees:
                total_hours += employees[employee_name]["hours_worked"]
        return total_hours

    def show_attendance(self):
        for day, employees in self.records.items():
            print(f"Day {day}:")
            for employee_name, record in employees.items():
                print(f"  {employee_name}: {record['status']}")

class Salary:
    def __init__(self):
        self.salary_record = defaultdict(dict)

    def apply_bonus(self, employee, attendance, day, bonus = 1000):
        # If worked hours more than 12 hours add 15% for bonus.
        if attendance.records[day][employee.name]["hours_worked"] > 12:
            employee.pay += bonus
            self.salary_record[employee]["Bonuses"] += bonus

        return employee.pay

    def apply_deduction(self, employee, deduction = 1000):
        if employee.late_count > 6:
            if employee.pay > 1000:
                employee.pay -= deduction
                self.salary_record[employee]["Deductions"] -= deduction
                employee.late_count = 0 # reset late count after applying deduction
            else:
                return "Employee's salary cannot be any lower than 1000."
        if employee.absent_count > 3:
            if employee.pay > 1000:
                employee.pay -= deduction
                self.salary_record[employee]["Deductions"] -= deduction
                employee.absent_count = 0 # reset absent count after applying deduction
            else:
                return "Employee's salary cannot be any lower than 1000."
            
        

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