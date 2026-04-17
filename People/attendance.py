import random
from collections import defaultdict
class Attendance:
    def __init__(self):
      # Yung init, purpose niya mag-store ng employee id, status (present or not), hours worked, late, overtime hours using dictionary.
        self.records = defaultdict(dict) # has status, hours worked, overtime hours

    def clock_in(self, day, employee_name):# day is from day generator when implemented into the manin program
        attendance_hash = ["Present", "Late", "Absent"]
        weights = [0.9, 0.07, 0.03]
        attendance = random.choices(attendance_hash, weights=weights, k=1)[0] #weighted randomness
        self.records[day][employee_name] = {
            "status": attendance
        }
        match attendance:
            case "Present":
                self.records[day][employee_name]["hours_worked"] = 8
            case "Late":
                self.records[day][employee_name]["hours_worked"] = 8- random.randint(1, 2)
            case "Absent":
                self.records[day][employee_name]["hours_worked"] = 0

    def clock_out(self, day, employee_name):
        if self.records[day][employee_name]["status"] == "Present" or self.records[day][employee_name]["status"] == "Late":
            overtime_chance = random.random()
            if overtime_chance < 0.1:  # 10% chance of working overtime
                self.records[day][employee_name]["overtime_hours"] = random.randint(1, 4)
                self.records[day][employee_name]["hours_worked"] += self.records[day][employee_name]["overtime_hours"]
            else:
                self.records[day][employee_name]["overtime_hours"] = 0
        else:
            self.records[day][employee_name]["overtime_hours"] = 0


    def show_attendance(self):
        for day, employees in self.records.items():
            print(f"Day {day}:")
            for employee_name, record in employees.items():
                print(f"  {employee_name}: {record['status']}, Hours Worked: {record['hours_worked']}, Overtime Hours: {record['overtime_hours']}")
