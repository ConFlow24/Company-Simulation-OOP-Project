from collections import defaultdict

class Inventory:
    def __init__(self):
        self.items = defaultdict(lambda: {"Small": 0, "Medium": 0, "Large": 0, "Base Price": 0})
        self.cash = 100000.00

    def add_item(self, name, size, quantity, base_price):
        self.items[name][size] += quantity
        self.items[name]["Base Price"] = base_price

    def remove_item(self, name, size, quantity):
        if self.items[name][size] >= quantity:
            self.items[name][size] -= quantity
            return True
        return False

    def get_price(self, name, size):
        size_multipliers = {"Small": 1, "Medium": 1.5, "Large": 2}
        return self.items[name]["Base Price"] * size_multipliers.get(size, 1)
    
    def total_stock_and_price(self):
        total_stock = 0
        total_price = 0
        for name, sizes in self.items.items():
            total_stock += sum(sizes.values()) - sizes["Base Price"]
            for size, quantity in sizes.items():
                if size != "Base Price":
                    total_price += self.get_price(name, size) * quantity
        return total_stock, total_price