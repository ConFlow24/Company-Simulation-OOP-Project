import random
from Classes.items import items
from Classes.employee import EmpGen


class CEOPanel:
    """
    This class represents the CEO Panel in the company simulation.
    It includes three main categories of options: Employee Options, Financial Options, and Inventory Options.
    The CEO can use this panel to manage employees (hire, fire, promote, demote), adjust salaries, and buy/sell inventory items.
    Each option is implemented as a method within this class, and the show_panel method provides an
    interactive menu for the CEO to access these options.
    """

    # Emplotee Options
    def hire_employee(self, company, empgen):
        """
        This function calls Emp_Gen to generate 4 candidates for the CEO to choose
        from when hiring a new employee. The CEO can only choose from the 4 candidates.
        Args:
            company (Company): The company object to which the new employee will be added.
            empgen (EmpGen): The employee generator object used to create candidate employees.

        """
        Emp_Gen = EmpGen()
        Emp_Gen.roles = ["Employee", "Intern"]
        Emp_Gen.weights = [0.8, 0.2]
        # this generates 4 (first becomes the CEO)
        Emp_Gen.generate_employee(4, company)
        candidates = Emp_Gen.employees
        candidates.pop(0)  # this will remove the CEO candidate from the list.
        # will remove temporarily added candidates from company.
        del company.employees[-3:]

        print("\n" + "=" * 70)
        print(f"{'CANDIDATES':^70}")
        print("=" * 70)
        print(f"{'#':<4} {'Name':<25} {'Role':<15} {'Pay':>20}")
        print("=" * 70)
        for i, emp in enumerate(candidates, 1):
            print(f"{i:<4} {emp.name:<25} {emp.role:<15} {emp.pay:>20,}")
        print("=" * 70 + "\n")

        while True:
            choice = input("Pick candidate (1-3): ").strip()
            if choice not in ["1", "2", "3"]:
                print("Invalid choice.")
            else:
                break

        chosen = candidates[int(choice) - 1]
        empgen.employees.append(chosen)
        company.add_employee(chosen)
        print(f"{chosen.name} hired as {chosen.role}!")

    def fire_employee(self, company, emp_gen):
        """
        This functions lets the USER (or CEO) select and remove an employee from the company.

        If the USER tries to fire the CEO, it will ask if they want to transfer the CEO
        position to another employee. 

        Args:
            company (Company): The company to remove the employee from.
            emp_gen (EmpGen): The employee generator list where the employee to be fired
            is also removed.
        """
        company.list_employees()
        employee = company.get_employee_input(
            "Choose a number from the list to fire: ", company.employees)

        if employee.role == "CEO":
            while True:
                choice = input(
                    "Cannot fire the CEO! Transfer the position to another employee(y/n): ")
                match choice:
                    case "y":
                        company.list_employees()
                        new_ceo = company.get_employee_input(
                            "Choose a number from the list to promote: ", company.employees)
                        new_ceo.role = "CEO"
                        company.remove_employee(employee.name, emp_gen)
                        break
                    case "n":
                        print(f"{employee.name} will remain CEO.")
                        break
                    case _: print("Invalid choice.")
            return

        company.remove_employee(employee.name, emp_gen)
        print(f"{employee.name} has been fired.")

    def promote_employee(self, company):
        """
        This function allows the USER (or CEO) to select an employee (by number) and promote
        them to the next role (Intern -> Employee -> Senior -> Manager). 

        The USER can also skip the Senior role when promoting an Employee.
        CEO cannot be promoted, and Managers cannot be promoted further.

        Args:
            company (Company): The company object containing the employees to be promoted.s
        """
        company.list_employees()
        employee = company.get_employee_input(
            "Choose a number from the list to promote: ", company.employees)

        # it counts the number of managers to ensure there are no more than 5 in the company.
        # if there are already 5 manager, the USER cannot promote another employee to manager.
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
        """
        This function allows the USER (or CEO) to select an employee (by number) and demote
        them to the previous role (Manager -> Senior -> Employee -> Intern).

        It is the same as promote_employee but in reverse. 
        The CEO cannot be demoted, and Interns cannot be demoted further.

        Args:
            company (Company): The company object containing the employees to be demoted.
        """
        company.list_employees()
        employee = company.get_employee_input(
            "Choose a number from the list to demote: ", company.employees)

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

    # Financial Options (this includes increasing and decreasing salary of employees)
    def increase_salary(self, company):
        """
        This function allows the USER (or CEO) to select an employee (by number) and 
        increase their salary by a specified amount.

        Args:
            company (Company): The company object containing the employees whose salary can be increased.
        """
        company.list_employees()
        employee = company.get_employee_input(
            "Choose a number from the list to increase salary: ", company.employees)

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
        """
        This function allows the USER (or CEO) to select an employee (by number) and 
        decrease their salary by a specified amount. The salary cannot be decreased below 1000.

        Args:
            company (Company): The company object containing the employees whose salary can be decreased.
        """
        company.list_employees()
        employee = company.get_employee_input(
            "Choose a number from the list to decrease salary: ", company.employees)

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

    # Inventory Options (includes buying, selling, and deleting items from the inventory)
    def buy_item(self, inventory):
        """
        This function allows the USER (or CEO) to manually buy an item for the inventory. 

        It deducts the price of the item from the inventory cash and adds the item to the inventory stock.

        Args:
            inventory (Inventory): The inventory object to buy items for.
        """
        item_list = []

        print("\n" + "=" * 45)
        print(f"{'AVAILABLE ITEMS':^45}")
        print("=" * 45)
        print(f"{'#':<5} {'Item':<25} {'Price':>10}")
        print("=" * 45)

        for i in range(5):
            random_item = random.choice(list(items))
            size = random.choice(["Small", "Medium", "Large"])
            print(
                f"{i+1}. {random_item.title()} - ${inventory.get_price(random_item, size):.2f}")
            item_list.append((random_item, size))

        print("=" * 45)

        while True:
            choice = input("\nPick item to buy (1-5): ").strip()
            if choice not in ["1", "2", "3", "4", "5"]:
                print("Invalid choice.")
            else:
                inventory.add_item(
                    item_list[int(choice) - 1][0], item_list[int(choice) - 1][1], 1)
                inventory.cash -= inventory.get_price(
                    item_list[int(choice) - 1][0], item_list[int(choice) - 1][1])
                print(
                    f"You have bought {item_list[int(choice) - 1][0].title()}. | Remaining cash {inventory.cash}")
                break

    def sell_item(self, inventory, company, sell=True):
        """
        This function allows the USER (or CEO) to manually sell an item from the inventory.

        If sell is True, it sells the item and adds the price to the inventory cash. 
        If sell is False, it simply deletes the item from the inventory without adding cash.

        Args:
            inventory (Inventory): The inventory object to sell items from.
            company (Company): The company object to get employee input for selecting items.
            sell (bool): If true, the item is sold. If false, it just deletes the item.
        """
        inventory.show_inventory()
        if not inventory.items:
            print("No items yet.")
            return

        item_names = list(inventory.items.keys())
        chosen_item = company.get_employee_input(
            "\nPick an item using a number (chronological) from the list: ", item_names)

        while True:
            choice_size = input(
                "\nWhat size? (Small, Medium, Large): ").strip()
            if choice_size in ["Small", "Medium", "Large"]:
                break
            print("Invalid size.")

        if inventory.items[chosen_item][choice_size] == 0:
            print("No stock of that size.")
            return

        while True:
            try:
                choice_amount = int(input("\nHow many do you want?: "))
                if choice_amount <= 0:
                    print("Amount must be positive.")
                elif choice_amount > inventory.items[chosen_item][choice_size]:
                    print("Not enough stock.")
                else:
                    break
            except ValueError:
                print("Invalid input.")

        inventory.remove_item(chosen_item, choice_size, choice_amount)
        if sell:
            earned = inventory.get_price(
                chosen_item, choice_size) * choice_amount
            inventory.cash += earned
            print(
                f"Sold {choice_amount}x {chosen_item.title()} ({choice_size}) for ${earned:.2f}. Cash: ${inventory.cash:.2f}")
        else:
            print(
                f"Deleted {choice_amount}x {chosen_item.title()} ({choice_size}) from inventory.")

    def show_panel(self, company, inventory, emp_gen):
        """"
        This function basically shows the CEO panel menu, which allows the USER (or CEO)
        to access all the options in the panel.

        The 4th option means quit, going back to the end of day menu.

        Args: 
            company (Company): The company object to access employee and financial options.
            inventory (Inventory): The inventory object to access inventory options.
            emp_gen (EmpGen): The employee generator object to access employee options.
        """
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
                        case "1": self.hire_employee(company, emp_gen)
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
                        case "2": self.sell_item(inventory, company)
                        case "3": self.sell_item(inventory, company, sell=False)
                        case _: print("Choice is not an option")
                case _: break
