import random
from Classes.items import items


class CEOPanel:
    """
    This class represents the CEO Panel in the company simulation.
    It includes three main categories of options: Employee Options, Financial Options, and Inventory Options.
    The CEO can use this panel to manage employees (hire, fire, promote, demote), adjust salaries, and buy/sell inventory items.
    Each option is implemented as a method within this class, and the show_panel method provides an
    interactive menu for the CEO to access these options.
    """

    def __init__(self, company, empgen, inventory):
        self.company = company
        self.empgen = empgen
        self.inventory = inventory
        self.employees = company.employees

    # Emplotee Options
    def hire_employee(self):
        """
        This function calls Emp_Gen to generate 4 candidates for the CEO to choose
        from when hiring a new employee. The CEO can only choose from the 4 candidates.
        Args:
            company (Company): The company object to which the new employee will be added.
            empgen (EmpGen): The employee generator object used to create candidate employees.

        """
        self.empgen.roles = ["Employee", "Intern"]
        self.empgen.weights = [0.8, 0.2]
        # this generates 4 (first becomes the CEO)
        self.empgen.generate_employee(4, self.company)
        candidates = self.empgen.employees
        # will remove temporarily added candidates from company.
        del self.employees[-4:]

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
        self.empgen.employees.append(chosen)
        self.company.add_employee(chosen)
        print(f"{chosen.name} hired as {chosen.role}!")
        self.empgen.roles = ["Employee", "Manager", "Intern", "Senior"]
        self.empgen.weights = [0.71, 0.09, 0.1, 0.1]

    def fire_employee(self):
        """
        This functions lets the USER (or CEO) select and remove an employee from the company.

        If the USER tries to fire the CEO, it will ask if they want to transfer the CEO
        position to another employee. 

        Args:
            company (Company): The company to remove the employee from.
            emp_gen (EmpGen): The employee generator list where the employee to be fired
            is also removed.
        """
        self.company.list_employees()
        employee = self.company.get_employee_input(
            "Choose a number from the list to fire: ", self.employees)

        if employee.role == "CEO":
            while True:
                choice = input(
                    "Cannot fire the CEO! Transfer the position to another employee(y/n): ")
                match choice:
                    case "y":
                        self.company.list_employees()
                        new_ceo = self.company.get_employee_input(
                            "Choose a number from the list to promote: ", self.employees)
                        new_ceo.role = "CEO"
                        self.company.remove_employee(
                            employee.name, self.empgen)
                        break
                    case "n":
                        print(f"{employee.name} will remain CEO.")
                        break
                    case _: print("Invalid choice.")
            return

        self.company.remove_employee(employee.name, self.empgen)
        print(f"{employee.name} has been fired.")

    def promote_employee(self):
        """
        This function allows the USER (or CEO) to select an employee (by number) and promote
        them to the next role (Intern -> Employee -> Senior -> Manager). 

        The USER can also skip the Senior role when promoting an Employee.
        CEO cannot be promoted, and Managers cannot be promoted further.

        Args:
            company (Company): The company object containing the employees to be promoted.s
        """
        self.company.list_employees()
        employee = self.company.get_employee_input(
            "Choose a number from the list to promote: ", self.employees)

        # it counts the number of managers to ensure there are no more than 5 in the company.
        # if there are already 5 manager, the USER cannot promote another employee to manager.
        manager_count = 0
        for emp in self.employees:
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

    def demote_employee(self):
        """
        This function allows the USER (or CEO) to select an employee (by number) and demote
        them to the previous role (Manager -> Senior -> Employee -> Intern).

        It is the same as promote_employee but in reverse. 
        The CEO cannot be demoted, and Interns cannot be demoted further.

        Args:
            company (Company): The company object containing the employees to be demoted.
        """
        self.company.list_employees()
        employee = self.company.get_employee_input(
            "Choose a number from the list to demote: ", self.employees)

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
    def increase_salary(self):
        """
        This function allows the USER (or CEO) to select an employee (by number) and 
        increase their salary by a specified amount.

        Args:
            company (Company): The company object containing the employees whose salary can be increased.
        """
        self.company.list_employees()
        employee = self.company.get_employee_input(
            "Choose a number from the list to increase salary: ", self.employees)

        while True:
            amount = input("Enter amount to increase: ").strip()
            if not amount.isdigit():
                print("Invalid amount.")
                continue
            break
        amount = int(amount)
        employee.pay += amount
        print(f"Salary of {employee.name} increased by {amount}!")

    def decrease_salary(self):
        """
        This function allows the USER (or CEO) to select an employee (by number) and 
        decrease their salary by a specified amount. The salary cannot be decreased below 1000.

        Args:
            company (Company): The company object containing the employees whose salary can be decreased.
        """
        self.company.list_employees()
        employee = self.company.get_employee_input(
            "Choose a number from the list to decrease salary: ", self.employees)

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
    def buy_item(self):
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
                f"{i+1}. {random_item.title()} - ${self.inventory.get_price(random_item, size):.2f}")
            item_list.append((random_item, size))

        print("=" * 45)

        while True:
            choice = input("\nPick item to buy (1-5): ").strip()
            if choice not in ["1", "2", "3", "4", "5"]:
                print("Invalid choice.")
            else:
                self.inventory.add_item(
                    item_list[int(choice) - 1][0], item_list[int(choice) - 1][1], 1)
                self.inventory.cash -= self.inventory.get_price(
                    item_list[int(choice) - 1][0], item_list[int(choice) - 1][1])
                print(
                    f"You have bought {item_list[int(choice) - 1][0].title()}. | Remaining cash {self.inventory.cash}")
                break

    def sell_item(self, sell=True):
        """
        This function allows the USER (or CEO) to manually sell an item from the inventory.

        If sell is True, it sells the item and adds the price to the inventory cash. 
        If sell is False, it simply deletes the item from the inventory without adding cash.

        Args:
            inventory (Inventory): The inventory object to sell items from.
            company (Company): The company object to get employee input for selecting items.
            sell (bool): If true, the item is sold. If false, it just deletes the item.
        """
        print(self.inventory)
        if not self.inventory.items:
            print("No items yet.")
            return

        item_names = list(self.inventory.items.keys())
        chosen_item = self.company.get_employee_input(
            "\nPick an item using a number (chronological) from the list: ", item_names)

        while True:
            choice_size = input(
                "\nWhat size? (Small, Medium, Large): ").strip()
            if choice_size in ["Small", "Medium", "Large"]:
                break
            print("Invalid size.")

        if self.inventory.items[chosen_item][choice_size] == 0:
            print("No stock of that size.")
            return

        while True:
            try:
                choice_amount = int(input("\nHow many do you want?: "))
                if choice_amount <= 0:
                    print("Amount must be positive.")
                elif choice_amount > self.inventory.items[chosen_item][choice_size]:
                    print("Not enough stock.")
                else:
                    break
            except ValueError:
                print("Invalid input.")

        self.inventory.remove_item(chosen_item, choice_size, choice_amount)
        if sell:
            earned = self.inventory.get_price(
                chosen_item, choice_size) * choice_amount
            self.inventory.cash += earned
            print(
                f"Sold {choice_amount}x {chosen_item.title()} ({choice_size}) for ${earned:.2f}. Cash: ${self.inventory.cash:.2f}")
        else:
            print(
                f"Deleted {choice_amount}x {chosen_item.title()} ({choice_size}) from inventory.")

    def show_panel(self):
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
                        case "1": self.hire_employee()
                        case "2": self.fire_employee()
                        case "3": self.promote_employee()
                        case "4": self.demote_employee()
                        case _: print("Choice is not an option")
                case "2":
                    choice2 = input("""
1. Increase salary
2. Decrease salary
                                    
Choose (1-2): """)
                    match choice2:
                        case "1": self.increase_salary()
                        case "2": self.decrease_salary()
                        case _: print("Choice is not an option")
                case "3":
                    choice2 = input("""
1. Manually buy item
2. Manually sell item
3. Delete item
                                    
Choose (1-3): """)
                    match choice2:
                        case "1": self.buy_item()
                        case "2": self.sell_item()
                        case "3": self.sell_item(sell = False)
                        case _: print("Choice is not an option")
                case _: break
