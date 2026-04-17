#main simulation engine, responsible for generating days and managing the flow of the simulation
from People.attendance import Attendance
from People.salary import Salary


class main_simulation_engine:
    def simEngine(weeks_to_simulate, employees):
        for i in range(weeks_to_simulate * 5): # simulates 5 days per week
            print(f"Day {i+1}")
            #generate attendance for each employee
            for employee in employees:
                Attendance.clock_in(i+1, employee.name)
            print("Attendance for the day:")
            Attendance.show_attendance()
            #compute salary for each employee based on attendance
            Salary.update_salary(Attendance.records[i+1])
