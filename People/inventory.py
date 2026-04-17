class Inventory:
    def __init__(self):
        # Format: {item_id: {name, quantity/progress, assigned_employee}}
        self.items = {}
        # Auto ID for items/tasks
        self.item_id_counter = 1

    def add_item(self, name, quantity=1):
        # add item to inventory
        pass

    def assign_item(self, item_id, employee_id, name):
        # Assigns item or task to employee id and name
        pass

    def update_item(self, item_id):
        # update progress or quanitty
        pass

    def remove_item(self, item_id):
        #delete
        pass

    def view_inventory(self):
        #view all items or tasks
      # ID: 1, Task: Design Logo, Assigned: Jeff (0001), Progress: 50%
        pass

    def view_employee_tasks(self, employee_id):
        # show ano meron ung employee id
        pass

    def daily_update(self, employees):
        # update tasks per day automatic
        pass
