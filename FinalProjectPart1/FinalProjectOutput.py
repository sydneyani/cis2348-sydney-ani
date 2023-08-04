# Sydney Ani PID: 1869076

# Bringing in the csv files
import csv

# Bringing in the class(index) I made
class Item:
    def __init__(self, item_id, manufacturer, item_type, price, service_date, is_damaged):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.price = price
        self.service_date = service_date
        self.is_damaged = is_damaged

# Allowing for the csv files to be read
def read_csv(file_path, delimiter=','):  #Added a parameter to specify the delimiter
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)  # Use the specified delimiter
        for row in reader:
            item_id = row[0]
            data[item_id] = [col.strip() for col in row[1:]]  # Remove leading/trailing whitespace
    return data

# Custom comparison function for sorting by manufacturer
def sort_by_manufacturer(item):
    return item.manufacturer

# Custom comparison function for sorting by item_id
def sort_by_item_id(item):
    return item.item_id

# Custom comparison function for sorting by service_date
def sort_by_service_date(item):
    return item.service_date

# Custom comparison function for sorting by price
def sort_by_price(item):
    return item.price

# Listing the csv files to specifically read for the input
def process_inventory():
    manufacturer_data = read_csv('ManufacturerList.csv')
    price_data = read_csv('PriceList.csv')
    service_date_data = read_csv('ServiceDatesList.csv')

    inventory = {}

    # Combine the data from the input files
    for item_id, manufacturer in manufacturer_data.items():
        if item_id in price_data and item_id in service_date_data:
            item_type = manufacturer[1]
            price = price_data[item_id][0]
            service_date = service_date_data[item_id][0]
            is_damaged = manufacturer[2] if len(manufacturer) > 2 else ''
            inventory[item_id] = Item(item_id, manufacturer[0], item_type, price, service_date, is_damaged)

   # Call the interactive query function
    interactive_query(inventory)

def interactive_query(inventory):
    while True:
        manufacturer = input("Enter the manufacturer (or 'q' to quit): ").strip().lower()
        if manufacturer == 'q':
            break

        item_type = input("Enter the item type: ").strip().lower()  # Strip whitespace from item type

        # Find matching items in the inventory (converted the input to lowercase and stripped whitespace for exact matching)
        matching_items = [item for item in inventory.values() if
                          item.manufacturer.lower() == manufacturer and item.item_type.lower() == item_type
                          and not item.is_damaged and item.service_date >= '2023-07-18']

        if not matching_items:
            print("No such item in inventory")
        else:
            # Sort by price in descending order
            matching_items.sort(key=sort_by_price, reverse=True)

            # Output the most expensive item
            expensive_item = matching_items[0]
            print("Your item is: Item ID: {}, Manufacturer: {}, Item Type: {}, Price: {}".format(
                expensive_item.item_id, expensive_item.manufacturer, expensive_item.item_type, expensive_item.price
            ))

            # Find items from another manufacturer with the closest price
            other_manufacturer_items = [item for item in inventory.values() if
                                        item.manufacturer.lower() != manufacturer and item.item_type.lower().strip() == item_type
                                        and not item.is_damaged and item.service_date >= '2023-07-18']

            if other_manufacturer_items:
                # Sort by price in ascending order
                other_manufacturer_items.sort(key=sort_by_price)
                closest_price_item = other_manufacturer_items[0]
                print("You may, also, consider: Item ID: {}, Manufacturer: {}, Item Type: {}, Price: {}".format(
                    closest_price_item.item_id, closest_price_item.manufacturer,
                    closest_price_item.item_type, closest_price_item.price
                ))

def main():
    process_inventory()

if __name__ == "__main__":
    main()
