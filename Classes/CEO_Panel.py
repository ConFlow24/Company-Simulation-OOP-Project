import random


class CEOPanel:
    # Employee Options
    def hire_employee(self, company, emp_gen):
        candidates = emp_gen.generate_candidates(3)

        print("\n--- Candidates ---")
        for i, emp in enumerate(candidates, 1):
            print(f"{i}. {emp.name} | {emp.role} | {emp.pay:,}")

        choice = input("Pick candidate (1-3): ").strip()

        if choice not in ["1", "2", "3"]:
            print("Invalid choice.")
            return

        chosen = candidates[int(choice) - 1]
        emp_gen.employees.append(chosen)
        company.add_employee(chosen)
        print(f"{chosen.name} hired as {chosen.role}!")

    def fire_employee(self, company):
        company.list_employees()
        name = input("Enter employee name to fire: ").strip()

        if name == "CEO":
            print("Cannot fire the CEO!")
            return

        employee = company.get_employee(name)
        if employee is None:
            print("Employee not found.")
            return

        company.remove_employee(name)
        print(f"{name} has been fired.")

    def promote_employee(self, company):
        company.list_employees()
        name = input("Enter employee name to promote: ").strip()

        employee = company.get_employee(name)
        if employee is None:
            print("Employee not found.")
            return

        manager_count = 0
        for emp in company.employees:
            if emp.role == "Manager":
                manager_count += 1

        match employee.role:
            case "CEO":
                print(f"{employee.name} cannot be promoted.")
            case "Manager":
                print(f"{employee.name} is already at the highest role.")
            case "Intern":
                employee.role = "Employee"
                employee.pay = 55000
                print(f"{employee.name} promoted to Employee!")
            case "Employee":
                skip = input("Skip Senior? (yes/no): ").strip().lower()
                if skip == "yes":
                    if manager_count >= 5:
                        print("Cannot promote. Already have 5 managers!")
                        return
                    employee.role = "Manager"
                    employee.pay = 80000
                    print(f"{employee.name} promoted to Manager!")
                else:
                    employee.role = "Senior"
                    employee.pay = 90000
                    print(f"{employee.name} promoted to Senior!")
            case "Senior":
                if manager_count >= 5:
                    print("Cannot promote. Already have 5 managers!")
                    return
                employee.role = "Manager"
                employee.pay = 80000
                print(f"{employee.name} promoted to Manager!")

    def demote_employee(self, company):
        company.list_employees()
        name = input("Enter employee name to demote: ").strip()

        employee = company.get_employee(name)
        if employee is None:
            print("Employee not found.")
            return

        match employee.role:
            case "CEO":
                print("Cannot demote the CEO!")
            case "Intern":
                print(f"{employee.name} is already at the lowest role.")
            case "Employee":
                employee.role = "Intern"
                employee.pay = 30000
                print(f"{employee.name} demoted to Intern!")
            case "Senior":
                employee.role = "Employee"
                employee.pay = 55000
                print(f"{employee.name} demoted to Employee!")
            case "Manager":
                employee.role = "Senior"
                employee.pay = 90000
                print(f"{employee.name} demoted to Senior!")

    # Financial Options
    def increase_salary(self, company):
        pass

    def decrease_salary(self, company):
        pass

    # Inventory Options
    def buy_item(self, company, items_list):
        pass

    def sell_item(self, company):
        pass

    def delete_item(self, company):
        pass
