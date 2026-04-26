#parang may queue like for example nagbuy yung employee, mapupunta siya sa to_store = []
#tas for each item sa to_store gagawa ng isang task kada item
#may size din each item na nakakaapekto sa speed ng pagkumpleto ng task na yun

#purely inventory lang to, like isang dictionary lang


# from dataclasses import dataclass, field

# @dataclass #auto generate init method
# class Item:
#     name: str
#     price:float #base price ng item, nagbabago depende sa size
#     stock: dict = field(default_factory=dict) #{"Small": 10, "Large": 4}, bawal daw dict = {} kasi idk

#     def get_price(self, size: str) -> float: #-> means it returns a flaot
#         size_multipliers = {"small": 1, "medium": 1.5, "large": 2}
#         return self.price * size_multipliers.get(self.stock.get(size), 1)
    
#     def total_stock_n_price(self):
#         return sum(self.stock.values()), sum(self.get_price("small"), self.get_price("medium"), self.get_price("large"))
    

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