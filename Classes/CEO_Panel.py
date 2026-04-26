import random
from task_generator import items


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
        company.list_employees()
        name = input("Enter employee name to increase salary: ").strip()
        employee = company.get_employee(name)
        if employee is None:
            print("Employee not found.")
            return
        amount = input("Enter amount to increase: ").strip()
        if not amount.isdigit():
            print("Invalid amount.")
            return
        amount = int(amount)
        employee.pay += amount
        print(f"Salary of {employee.name} increased by {amount}!")

    def decrease_salary(self, company):
        company.list_employees()
        name = input("Enter employee name to decrease salary: ").strip()
        employee = company.get_employee(name)
        if employee is None:
            print("Employee not found.")
            return
        amount = input("Enter amount to decrease: ").strip()
        if not amount.isdigit():
            print("Invalid amount.")
            return
        amount = int(amount)
        if amount > employee.pay+1000:
            print("Cannot decrease salary below 1000.")
            return
        employee.pay -= amount
        print(f"Salary of {employee.name} decreased by {amount}!")

    # Inventory Options
    def buy_item(self, inventory):
        item_list = []
        for i in range(5):
            random_item = random.choice(list(items))
            size = random.choice(["Small", "Medium", "Large"])
            print(f"{i+1}. {random_item} - ${inventory.get_price(random_item, size):.2f}")
            item_list.append(random_item)
        while True:
            choice = input("Pick item to buy (1-5): ").strip()
            if choice not in ["1", "2", "3", "4", "5"]:
                print("Invalid choice.")
            else:
                inventory.add_item(item_list[int(choice) - 1], size, 1)
                inventory.cash -= inventory.get_price(random_item, size)

    def sell_item(self, inventory):
        inventory.show_inventory()
        choice = input("Choose an item: ")
        if choice not in inventory:
            print("Invalid choice.")
        choice_size = input("What size of the item: ")
        if inventory.items[choice][choice_size] == 0:
            print("No stock of that size. ")
        try:
            choice_amount = input("How many: ")
        except: ValueError
        else: 
            if choice_amount > inventory.items[choice][choice_size]:
                print("Choice is larger than the amount in stock.")
            elif choice_amount < 0:
                print("Choice cannot be negative.")
            else:
                inventory.remove_item(choice, choice_size, choice_amount)
                inventory.cash += inventory.get_price(choice, choice_size)

    def delete_item(self, inventory):
        inventory.show_inventory()
        choice = input("Choose an item: ")
        if choice not in inventory:
            print("Invalid choice.")
        choice_size = input("What size of the item: ")
        if inventory.items[choice][choice_size] == 0:
            print("No stock of that size. ")
        try:
            choice_amount = input("How many: ")
        except: ValueError
        else: 
            if choice_amount > inventory.items[choice][choice_size]:
                print("Choice is larger than the amount in stock.")
            elif choice_amount < 0:
                print("Choice cannot be negative.")
            else:
                inventory.remove_item(choice, choice_size, choice_amount)

    def show_panel(self, company, emp_gen, inventory):
        choice = input("""1. Employee Options
2. Financial Options
3. Inventory Options
Choose (1-3): """)
        match choice:
            case "1":
                choice2 = input("""1. Hire employee
2. Fire employee
3. Promote employee
4. Demote employee""")
                match choice2:
                    case "1": self.hire_employee(company, emp_gen)
                    case "2": self.fire_employee(company)
                    case "3": self.promote_employee(company)
                    case "4": self.demote_employee(company)
                    case _: print("Choice is not an option")
            case "2":
                choice2 = input("""1. Increase salary
2. Decrease salary""")
                match choice2:
                    case "1": self.increase_salary(company)
                    case "2": self.decrease_salary(company)
                    case _: print("Choice is not an option")
            case "3":
                choice2 = input("""1. Manually buy item
2. Manually sell item
3. Delete item""")
                match choice2:
                    case "1": self.buy_item(inventory)
                    case "2": self.sell_item(inventory)
                    case "3": self.delete_item(inventory)
                    case _: print("Choice is not an option")
            case _: print("Choice is not an option")
