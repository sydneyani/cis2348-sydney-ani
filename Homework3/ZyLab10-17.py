#Sydney Ani PID: 1869076


class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")


# Create objects of the ItemToPurchase class and set their attributes
item1 = ItemToPurchase()
item1.item_name = "Chocolate Chips"
item1.item_price = 3.0
item1.item_quantity = 1

item2 = ItemToPurchase()
item2.item_name = "Vanilla Extract" or  "Bottled Water"
item2.item_price = 2.5
item2.item_quantity = 2

# Add the costs of the two items together and output the total cost
total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity

# Output the total cost and item details
print("Item 1")
print("Enter the item name:")
print("Enter the item price:")
print("Enter the item quantity:\n")
print("Item 2")
print("Enter the item name:")
print("Enter the item price:")
print("Enter the item quantity:\n")
print("TOTAL COST\n")
item1.print_item_cost()
item2.print_item_cost()
print(f"\nTotal: ${total_cost:.0f}")
