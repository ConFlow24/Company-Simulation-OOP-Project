#parang may queue like for example nagbuy yung employee, mapupunta siya sa to_store = []
#tas for each item sa to_store gagawa ng isang task kada item
#may size din each item na nakakaapekto sa speed ng pagkumpleto ng task na yun
#baka bullshit yung nasa baba, inAI yan ni jeff


class Inventory:
    def __init__(self):
        # Format: {item_id: {name, size}}
        self.items = {}
        # Auto ID for items/tasks
        self.item_id_counter = 1

    def add_item(self, name, quantity=1):
        # add item to inventory
        pass

    def update_item(self, item_id):
        # update progress or quanitty
        pass

    def remove_item(self, item_id):
        #delete
        pass

    def view_inventory(self):
        #view all items
        pass

