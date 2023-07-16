#Sydney Ani PID: 1869076


class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = "${:.0f}".format(float(price))  # Format price as currency without decimals
        self.item_quantity = int(quantity)
        self.item_description = description

    def print_item_cost(self):
        total_cost = self.item_quantity * float(self.item_price[1:])  # Calculate total cost
        print(self.item_name, self.item_quantity, "@", self.item_price, "=", "${:.0f}".format(total_cost))

    def print_item_description(self):
        print(self.item_name + ": " + self.item_description)


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, new_item):
        item_found = False
        for item in self.cart_items:
            if item.item_name == new_item.item_name:
                if new_item.item_description != "none":
                    item.item_description = new_item.item_description
                if new_item.item_price != "$0":
                    item.item_price = "${:.0f}".format(float(new_item.item_price[1:]))  # Format price as currency without decimals
                if new_item.item_quantity != 0:
                    item.item_quantity = int(new_item.item_quantity)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_quantity * float(item.item_price[1:])
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print("Number of Items:", self.get_num_items_in_cart())
            print()
            for item in self.cart_items:
                item.print_item_cost()
            print()
            total_cost = self.get_cost_of_cart()  # Calculate total cost
            print("Total:", "${:.0f}".format(total_cost))  # Format total cost as currency without decimals

    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        choice = input("\nChoose an option:\n")

        if choice == 'a':
            # Add item to cart
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = input("Enter the item price:\n")
            quantity = input("Enter the item quantity:\n")
            item = ItemToPurchase(name, price, quantity, description)
            shopping_cart.add_item(item)

        elif choice == 'r':
            # Remove item from cart
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            shopping_cart.remove_item(name)

        elif choice == 'c':
            # Change item quantity
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            new_quantity = input("Enter the new quantity:\n")
            item = ItemToPurchase(name, quantity=new_quantity)
            shopping_cart.modify_item(item)

        elif choice == 'i':
            # Output items' descriptions
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()

        elif choice == 'o':
            # Output shopping cart
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()

        elif choice == 'q':
            # Quit
            break

        else:
            print("Invalid option. Please choose again.")


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print("\nCustomer name:", customer_name)
    print("Today's date:", current_date)

    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)


if __name__ == "__main__":
    main()
