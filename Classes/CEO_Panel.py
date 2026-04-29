import random
from Classes.items import items
from Classes.employee_generator import EmpGen


class CEOPanel:
    
    # Employee Options
    def hire_employee(self, company):
        Emp_Gen = EmpGen()
        Emp_Gen.roles = ["Employee", "Intern"]
        Emp_Gen.weights = [0.8, 0.2]
        Emp_Gen.generate_employee(4, company)
        candidates = Emp_Gen.employees
        candidates.pop(0)
        del company.employees[-4:]

        print("\n--- Candidates ---")
        for i, emp in enumerate(candidates, 1):
            print(f"{i}. {emp.name} | {emp.role} | {emp.pay:,}")
        
        while True:
            choice = input("Pick candidate (1-3): ").strip()
            if choice not in ["1", "2", "3"]:
                print("Invalid choice.")
            else: break

        chosen = candidates[int(choice) - 1]
        Emp_Gen.employees.append(chosen)
        company.add_employee(chosen)
        print(f"{chosen.name} hired as {chosen.role}!")

    def fire_employee(self, company, emp_gen):
        company.list_employees()
        employee = company.get_employee_input("Enter employee name to fire: ")

        if employee.role == "CEO":
            while True:
                choice = input("Cannot fire the CEO! Transfer the position to another employee(y/n): ")
                match choice:
                    case "y":
                        company.list_employees()
                        new_ceo = company.get_employee_input("Enter employee name to promote: ")
                        new_ceo.role = "CEO"
                        company.remove_employee(employee.name)
                        emp_gen.employees.remove(employee)
                        break
                    case "n":
                        print(f"{employee.name} will remain CEO.")
                        break
                    case _: print("Invalid choice.")
            return

        company.remove_employee(employee.name)
        emp_gen.employees.remove(employee)
        print(f"{employee.name} has been fired.")

    def promote_employee(self, company):
        company.list_employees()
        employee = company.get_employee_input("Enter employee name to fire: ")

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
                while True:
                    skip = input("Skip Senior? (yes/no): ").strip().lower()
                    match skip:
                        case "yes":
                            if manager_count >= 5:
                                print("Cannot promote. Already have 5 managers!")
                                continue
                            employee.role = "Manager"
                            employee.pay = 80000
                            print(f"{employee.name} promoted to Manager!")
                            break
                        case "no":
                            employee.role = "Senior"
                            employee.pay = 90000
                            print(f"{employee.name} promoted to Senior!")
                            break
                        case _:
                            print("Invalid choice.")
            case "Senior":
                if manager_count >= 5:
                    print("Cannot promote. Already have 5 managers!")
                    return
                employee.role = "Manager"
                employee.pay = 80000
                print(f"{employee.name} promoted to Manager!")

    def demote_employee(self, company):
        company.list_employees()
        employee = company.get_employee_input("Enter employee name to fire: ")

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
        employee = company.get_employee_input("Enter employee name to fire: ")

        while True:
            amount = input("Enter amount to increase: ").strip()
            if not amount.isdigit():
                print("Invalid amount.")
                continue
            break
        amount = int(amount)
        employee.pay += amount
        print(f"Salary of {employee.name} increased by {amount}!")

    def decrease_salary(self, company):
        company.list_employees()
        employee = company.get_employee_input("Enter employee name to fire: ")

        while True:
            amount = input("Enter amount to decrease: ").strip()
            if not amount.isdigit():
                print("Invalid amount.")
                continue
            break
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
            print(f"{i+1}. {random_item.title()} - ${inventory.get_price(random_item, size):.2f}")
            item_list.append((random_item, size))
        while True:
            choice = input("Pick item to buy (1-5): ").strip()
            if choice not in ["1", "2", "3", "4", "5"]:
                print("Invalid choice.")
            else:
                inventory.add_item(item_list[int(choice) - 1][0], item_list[int(choice) - 1][1], 1)
                inventory.cash -= inventory.get_price(item_list[int(choice) - 1][0], size)
                print(f"You have bought {item_list[int(choice) - 1][0].title()}. | Remaining cash {inventory.cash}")
                break

    def sell_item(self, inventory, sell=True):
        inventory.show_inventory()
        if not inventory.items:
            print("No items yet.")
            return

        while True:
            choice = input("Choose an item: ").strip().lower()
            if choice in inventory.items:
                break
            print("Invalid choice.")

        while True:
            choice_size = input("What size? (Small, Medium, Large): ").strip()
            if choice_size in ["Small", "Medium", "Large"]:
                break
            print("Invalid size.")

        if inventory.items[choice][choice_size] == 0:
            print("No stock of that size.")
            return

        while True:
            try:
                choice_amount = int(input("How many: "))
                if choice_amount <= 0:
                    print("Amount must be positive.")
                elif choice_amount > inventory.items[choice][choice_size]:
                    print("Not enough stock.")
                else:
                    break
            except ValueError:
                print("Invalid input.")

        inventory.remove_item(choice, choice_size, choice_amount)
        if sell:
            earned = inventory.get_price(choice, choice_size) * choice_amount
            inventory.cash += earned
            print(f"Sold {choice_amount}x {choice.title()} ({choice_size}) for ${earned:.2f}. Cash: ${inventory.cash:.2f}")
        else:
            print(f"Deleted {choice_amount}x {choice.title()} ({choice_size}) from inventory.")

    def show_panel(self, company, inventory, emp_gen):
        while True:
            choice = input("""
1. Employee Options
2. Financial Options
3. Inventory Options
4. Quit
Choose (1-4): """)
            match choice:
                case "1":
                    choice2 = input("""
1. Hire employee
2. Fire employee
3. Promote employee
4. Demote employee
Choose (1-4): """)
                    match choice2:
                        case "1": self.hire_employee(company)
                        case "2": self.fire_employee(company, emp_gen)
                        case "3": self.promote_employee(company)
                        case "4": self.demote_employee(company)
                        case _: print("Choice is not an option")
                case "2":
                    choice2 = input("""
1. Increase salary
2. Decrease salary
Choose (1-2): """)
                    match choice2:
                        case "1": self.increase_salary(company)
                        case "2": self.decrease_salary(company)
                        case _: print("Choice is not an option")
                case "3":
                    choice2 = input("""
1. Manually buy item
2. Manually sell item
3. Delete item
Choose (1-3): """)
                    match choice2:
                        case "1": self.buy_item(inventory)
                        case "2": self.sell_item(inventory)
                        case "3": self.sell_item(inventory, sell=False)
                        case _: print("Choice is not an option")
                case _: break
