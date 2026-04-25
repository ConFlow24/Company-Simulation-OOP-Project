from email import generator

from People.employee import Employee, Intern, Manager, Senior


class CEO(Employee):
    def __init__(self, name, pay):
        super().__init__(name, role="CEO", pay=pay)

    def fire_employee(self, company):
        name = input("Enter the name of the employee to fire: ")
        employee = company.get_employee(name)
        if employee.role == "CEO":
            print("Cannot fire the CEO!")
            return

        if employee is None:
            print("Employee not found.")
            return
        company.remove_employee(name)

    def hire_employee(self, company, generator_cls):
        generator = generator_cls(self.first_names, self.last_names, self.role_pay_hash)
        generator.roles = ["Employee", "Intern"]
        generator.weights = [0.71, 0.29]
        generator.generate_employee(3)

        while True:
            for i, emp in enumerate(generator.employees):
                print(f"{i+1}. {emp.name} | {emp.role} | {emp.pay:,}")

            choice = input("Choose an employee to hire (1, 2, or 3): ")
            if choice in ["1", "2", "3"]:
                break
            print("Invalid choice.")
        company.add_employee(generator.employees[int(choice) - 1])
        return generator.employees[int(choice) - 1]

    def promote_employee(self, company):
        name = input("Enter the name of the employee: ")
        employee = company.get_employee(name)

        if employee is None:
            print("Employee not found.")
            return

        while True:
            match employee.role:
                case "CEO":
                    print("Cannot promote the CEO!")
                case "Manager":
                    print("Cannot promote a Manager!")
                case "Intern":
                    employee.role = "Employee"
                    break
                case "Employee":
                    choice = input("Promote to Senior, or Manager?: ").lower()
                    if choice == "senior":
                        employee.role = "Senior"
                        break
                    elif choice == "manager":
                        employee.role = "Manager"
                        break
                    else:
                        print("Invalid choice.")
                        continue
                case "Senior":
                    employee.role = "Manager"
                    break
                case _:
                    print("Unknown role.")
                    break
        return employee
        

    def demote_employee(self, company):
        name = input("Enter the name of the employee: ")
        employee = company.get_employee(name)

        if employee is None:
            print("Employee not found.")
            return

        while True:
            match employee.role:
                case "CEO":
                    print("Cannot demote the CEO!")
                case "Manager":
                    choice = input("Demote to Senior, or Employee?: ").lower()
                    if choice == "senior":
                        employee.role = "Senior"
                        break
                    elif choice == "employee":
                        employee.role = "Employee"
                        break
                    else:
                        print("Invalid choice.")
                        continue
                case "Intern":
                    employee.role = "Employee"
                    break
                case "Employee":
                    employee.role = "Intern"
                    break
                case "Senior":
                    employee.role = "Employee"
                    break
                case _:
                    print("Unknown role.")
                    break
        return employee

    def give_bonus(self, employee, company, salary):
        name = input("Enter the name of the employee: ")
        employee = company.get_employee(name)
        if employee is None:
            print("Employee not found.")
            return
        bonus = int(input("Enter the bonus amount: "))
        salary.apply_bonus(employee, bonus)

    def apply_deduction(self, employee, company, salary):
        name = input("Enter the name of the employee: ")
        employee = company.get_employee(name)
        if employee is None:
            print("Employee not found.")
            return
        deduction = int(input("Enter the deduction amount: "))
        salary.apply_deduction(employee, deduction)

    def buy_stock(self, inventory):
        pass

    def sell_stock(self, inventory):
        pass

    def adjust_inventory(self, inventory):
        pass
