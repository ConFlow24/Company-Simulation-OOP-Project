from People.employee import Employee, Intern, Manager, Senior


class CEO(Employee):
    def __init__(self, name, pay):
        super().__init__(name, role="CEO", pay=pay)

    def fire_employee(self, company):
        company.list_employees()
        name = input("Enter the name of the employee to fire: ")

        if name == "CEO":
            print("Cannot fire the CEO!")
            return

        employee = company.get_employee(name)

        if employee is None:
            print("Employee not found.")
            return
        company.remove_employee(name)

    def hire_employee(self, company):
        name = input("Enter the name of the new employee: ")
        role = input(
            "Enter the role of the new employee (Employee/Manager/Intern/Senior): ")

        if role == "CEO":
            print("Cannot hire another CEO!")
            return

        if role not in ["Employee", "Manager", "Intern", "Senior"]:
            print("Invalid role. Employee not hired.")
            return
        else:
            pay = int(input("Enter the annual pay for the new employee: "))

            if pay < 30000 or pay > 150000:
                print("Invalid pay. Employee not hired.")
                return
            role_map = {
                "Employee": Employee,
                "Manager": Manager,
                "Intern": Intern,
                "Senior": Senior
            }
            new_employee = role_map[role](name=name, pay=pay)
            company.add_employee(new_employee)

    def promote_employee(self, company):
        pass

    def demote_employee(self, company):
        pass

    def give_bonus(self, employee, company):
        pass

    def apply_deduction(self, employee, company):
        pass

    def buy_stock(self, inventory):
        pass

    def sell_stock(self, inventory):
        pass

    def adjust_inventory(self, inventory):
        pass
