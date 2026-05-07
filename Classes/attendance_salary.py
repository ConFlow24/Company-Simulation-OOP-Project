import random
from collections import defaultdict


class Attendance:
    """
    Manages daily attendance records for all employees.

    Tracks attendance status, hours worked, overtime, and cumulative
    late/absent counts used for salary deductions.
    """

    def __init__(self):
        # nested defaultdict: records[day][employee] = {status, hours_worked}
        # also stores records[employee]["late_count"] and ["absent_count"] for salary logic

        # lambda allows nested dicts, avoids KeyErrors on first access
        self.records = defaultdict(lambda: defaultdict(dict))

    def clock_in(self, day, employee_name, employee_punct):
        """
        Records attendance for an employee using weighted randomness based on punctuality.

        Args:
            day (int): Current simulation day.
            employee_name (str): Name of the employee.
            employee_punct (int): Punctuality rating from 1 (poor) to 5 (perfect).
        """

        attendance_list = ["Present", "Late", "Absent"]
        match employee_punct:  # less and less likely to be present
            case 5:
                weights = [1, 0, 0]  # means always present
            case 4:
                weights = [0.9, 0.07, 0.03]
            case 3:
                weights = [0.75, 0.18, 0.07]
            case 2:
                weights = [0.55, 0.30, 0.15]
            case 1:
                # means more likely to be late or absent
                weights = [0.35, 0.40, 0.25]
            case _:
                # default to punctuality 3 weights if invalid punctuality value is given
                weights = [0.75, 0.18, 0.07]
        attendance = random.choices(attendance_list, weights=weights)[0]  # weighted randomness
        self.records[day][employee_name] = {
            "status": attendance
        }

        match attendance:
            case "Present":
                self.records[day][employee_name]["hours_worked"] = 8
            case "Late":
                self.records[day][employee_name]["hours_worked"] = 8 - \
                    random.randint(1, 2)
                self.records[employee_name]["late_count"] = self.records[employee_name].get(
                    "late_count", 0) + 1  # adds to employee late count for salary deductions and bonuses
            case "Absent":
                self.records[day][employee_name]["hours_worked"] = 0
                self.records[employee_name]["absent_count"] = self.records[employee_name].get(
                    "absent_count", 0) + 1  # adds to employee absent count for salary deductions
        self.records[day][employee_name]["total_hours"] = self.records[day][employee_name].get(
            # adds to employee total hours for salary bonuses and ranking
            "total_hours", 0) + self.records[day][employee_name]["hours_worked"]

    def get_total_work_hours(self, employee_name):
        """
        Returns total hours worked by an employee across all simulated days.

        Args:
            employee_name (str): Name of the employee and it returns the total hours worked.
        """

        total_hours = 0
        for day, employees in self.records.items():
            # if day is not an integer, to avoid key errors and crashes
            if not isinstance(day, int):
                continue
            if employee_name in employees:
                total_hours += employees[employee_name].get("hours_worked", 0)
        return total_hours

    def show_attendance(self, day):
        """
        Basically print the attendance records for the day in a good format.
        Shows employee name and their attendance (Present, Late, Absent).
        """
        print("\n" + "=" * 70)
        print(f"{f'ATTENDANCE - DAY {day}':^70}")
        print("=" * 70)
        print(f"{'Employee Name':<40} {'Status':>29}")
        print("=" * 70)
        for employee_name, record in self.records[day].items():
            print(f"{employee_name:<40} {record['status']:>29}")
        print("=" * 70 + "\n")


class Salary:
    """
    Handles salary bonuses and deductions for all employees.

    Tracks cumulative bonuses and deductions per employee over the simulation.
    """

    def __init__(self):
        # salary_record[employee_name]["Bonuses"] and ["Deductions"] track running totals
        self.salary_record = defaultdict(lambda: defaultdict(int))

    def apply_bonus(self, employee, attendance, day, bonus=1000):
        """
        Awards a bonus if the employee worked more than 10 hours (overtime).

        Args:
            employee (Employee): The employee to check.
            attendance (Attendance): Attendance system with hours data.
            day (int): Current simulation day.
            bonus (int): Bonus amount. Defaults to 1000.
        """

        if attendance.records[day][employee.name].get("hours_worked", 0) > 10:  # overtime bonus
            employee.pay += bonus
            self.salary_record[employee.name]["Bonuses"] += bonus

        return employee.pay

    def apply_deduction(self, employee, attendance, deduction=1000):
        """
        Deducts salary if employee has too many lates (>6) or absences (>3).

        Resets the count after deduction. Salary floor is 1000.

        Args:
            employee (Employee): The employee to check.
            attendance (Attendance): Attendance system with cumulative counts.
            deduction (int): Amount to deduct. Defaults to 1000.
        """

        if attendance.records[employee.name].get("late_count", 0) > 6:
            if employee.pay > 1000:
                employee.pay -= deduction
                self.salary_record[employee.name]["Deductions"] += deduction
                # reset late count after applying deduction
                attendance.records[employee.name]["late_count"] = 0
            else:
                return "Employee's salary cannot be any lower than 1000."

        if attendance.records[employee.name].get("absent_count", 0) > 3:
            if employee.pay > 1000:
                employee.pay -= deduction
                self.salary_record[employee.name]["Deductions"] += deduction
                # reset absent count after applying deduction
                attendance.records[employee.name]["absent_count"] = 0
            else:
                return "Employee's salary cannot be any lower than 1000."

    def apply_top5_bonus(self, top5_list, employees_list):
        """
        Top 5 employees will get a bonus of 1000 and it will be added to their salary.

        Args:
            top5_list (list): Top performing employees.
            employees_list (list): All current company employees.
        """

        for employee in top5_list:
            if employee in employees_list:
                employee.pay += 1000
                self.salary_record[employee]["Bonuses"] += 1000

    def apply_top5_deduct(self, bottom5_list, employees_list):
        """
        Same as the top 5 bonus but it deducts 1000 from the bottom 5 employees instead of giving them a bonus.
        """

        for employee in bottom5_list:
            if employee in employees_list:
                employee.pay -= 1000
                self.salary_record[employee]["Deductions"] -= 1000

    def show_salary_report(self, employees_list):
        """
        Basically print the salary report for all employees in a good format.
        Shows employee name, current salary, total bonuses, and total deductions.
        """

        for employee in employees_list:
            print(f"""Current salary: {employee.pay}
Bonuses received over time: {self.salary_record[employee]["Bonuses"]}
Deductions received over time: {self.salary_record[employee]["Deductions"]}""")
