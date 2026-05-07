from collections import defaultdict
from Classes.items import items


class Inventory:
    """
    This class manages the company's inventory, where it includes the items, their quantities
    for each size (small, medium, large), and their base price.

    Also handles the buying and selling of items, as well as the total stock
    and price calculations.

    Attributes:
        items (defaultdict): A nested dictionary that stores item names as keys, and their sizes and base price as values.
        cash (float): The current cash available for the company.
    """

    def __init__(self):
        """
        Initializes the inventory with an empty items dictionary and a starting cash of 100,000.00.

        The items dictionary is a defaultdict that automatically 
        creates nested dictionaries for new item names,
        """

        self.items = defaultdict(
            # lambda sets the default value for any new item key — avoids KeyErrors on first access.
            lambda: {"Small": 0, "Medium": 0, "Large": 0, "Base Price": 0})
        self.cash = 10000.00  # company's starting cash.

    def add_item(self, name, size, quantity):
        """
        Adds items to the inventory based on the name, size, and quantity specified.
        It also updates the base price for the item based on the predefined items dictionary.

        Args:
            name (str): The name of the item to be added.
            size (str): The size of the item (Small, Medium, Large).
            quantity (int): The quantity of the item to be added.
        """

        self.items[name][size] += quantity
        self.items[name]["Base Price"] = items[name]

    def remove_item(self, name, size, quantity):
        """
        Same as the add_item function, but it removes the specified quantity of the item from the inventory.
        It checks if there is enough stock of the item before removing it.

        Args:
            Same as the add_item function.
        """

        if self.items[name][size] >= quantity:
            self.items[name][size] -= quantity

    def get_price(self, name, size):
        """
        Return the price of the given item name and size.
        The price is calculated based on the base price of the item and a multiplier for the size.

        Size multipliers are defined as follows:
        - Small: 1
        - Medium: 1.5
        - Large: 2

        Args: 
            name (str): The name of the item.
            size (str): The size of the item (Small, Medium, Large).
        """

        size_multipliers = {"Small": 1, "Medium": 1.5, "Large": 2}
        return items[name] * size_multipliers.get(size, 1)

    def total_stock_and_price(self):
        """
        Calculates the total stock and total price of all items in the inventory and returns them as a tuple.
        """

        total_stock = 0
        total_price = 0
        for name, sizes in self.items.items():
            # subtract Base Price entry to avoid counting it as stock

            total_stock += sum(sizes.values()) - sizes["Base Price"]
            for size, quantity in sizes.items():
                if size != "Base Price":
                    total_price += self.get_price(name, size) * quantity
        return total_stock, total_price

    def show_inventory(self):
        """
        Basically print the inventory in a nice format. Includes item name, its quantities for each size,
        and its base price.
        """

        print(f"""{'=' * 70}
{'INVENTORY':^70}
{'=' * 70}""")
        if self.items:
            print(
                f"{'Item Name':<20} {'Small':>10} {'Medium':>10} {'Large':>10} {'Base Price':>15}")
            print("=" * 70)
            for name, sizes in self.items.items():
                print(
                    f"{name.title():<20} {sizes['Small']:>10} {sizes['Medium']:>10} {sizes['Large']:>10} {sizes['Base Price']:>15.2f}")
        else:
            print(f"{'No items yet':^70}")
        print("=" * 70 + "\n")
