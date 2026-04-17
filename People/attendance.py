# Dito papasok kung paano gumagalaw ung attendance sa totoong buhay. 
# Based sa rubrics "add, edit, delete, view" need nito. Ang naisip ko, sa employee at inventory lang to i-apply hindi sa attendance at salary.
# Bale may choices

# 1. Start Simulation
# 2. Manage (Add / Edit / Delete)
# 3. Next Day
# 4. View Report
# 5. End

# Para sa menu 2 na manage dito iaaply yung add edit delete
# 1. Add Employee, 2. Edit Employee, 3. Remove Employee, 4. Manage Inventory 5. Back

class Attendance:
    def __init__(self):
      # Yung init, purpose niya mag-store ng employee id, status (present or not), hours worked, late, overtime hours using dictionary.
        self.records = {}
        self.day = 1
        self.records[self.day] = {}

    def clock_in(self, employee_id):
        pass

    def clock_out(self, employee_id):
        pass

    def mark_absent(self, employee_id):
        pass

    def next_day(self):
        pass

    def show_attendance(self):
        pass
