from collections import defaultdict
from Classes.items import items

class Inventory:
    def __init__(self):
        self.items = defaultdict(lambda: {"Small": 0, "Medium": 0, "Large": 0, "Base Price": 0})
        self.cash = 100000.00

    def add_item(self, name, size, quantity):
        self.items[name][size] += quantity
        self.items[name]["Base Price"] = items[name]

    def remove_item(self, name, size, quantity):
        if self.items[name][size] >= quantity:
            self.items[name][size] -= quantity


    def get_price(self, name, size):
        size_multipliers = {"Small": 1, "Medium": 1.5, "Large": 2}
        return items[name] * size_multipliers.get(size, 1)
    
    def total_stock_and_price(self):
        total_stock = 0
        total_price = 0
        for name, sizes in self.items.items():
            total_stock += sum(sizes.values()) - sizes["Base Price"]
            for size, quantity in sizes.items():
                if size != "Base Price":
                    total_price += self.get_price(name, size) * quantity
        return total_stock, total_price
    
def show_inventory(self):
    print("\n" + "=" * 70)
    print(f"{'INVENTORY':^70}")
    print("=" * 70)
    if self.items:
        print(f"{'Item Name':<20} {'Small':>10} {'Medium':>10} {'Large':>10} {'Base Price':>15}")
        print("=" * 70)
        for name, sizes in self.items.items():
            print(f"{name.title():<20} {sizes['Small']:>10} {sizes['Medium']:>10} {sizes['Large']:>10} {sizes['Base Price']:>15.2f}")
    else:
        print(f"{'No items yet':^70}")
    print("=" * 70 + "\n")