#Sydney Ani PID: 1869076

#Bringing in the csv files
import csv

#Bringing in the class(index) I made
class Item:
    def __init__(self, item_id, manufacturer, item_type, price, service_date, is_damaged):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.price = price
        self.service_date = service_date
        self.is_damaged = is_damaged

#Allowing for the csv files to be read
def read_csv(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            item_id = row[0]
            data[item_id] = row[1:]
    return data

#Listing the csv files to specifically read for the input
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

    # Generate FullInventory.csv
    sorted_inventory = sorted(inventory.values(), key=lambda x: x.manufacturer)
    with open('FullInventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])
        for item in sorted_inventory:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.is_damaged])

    # Generate LaptopInventory.csv
    item_types = set(item.item_type for item in inventory.values())
    for item_type in item_types:
        items_of_type = [item for item in inventory.values() if item.item_type == item_type]
        items_of_type_sorted = sorted(items_of_type, key=lambda x: x.item_id)
        file_name = f'{item_type}Inventory.csv'
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item ID', 'Manufacturer', 'Price', 'Service Date', 'Damaged'])
            for item in items_of_type_sorted:
                writer.writerow([item.item_id, item.manufacturer, item.price, item.service_date, item.is_damaged])

    # Generate PastServiceDateInventory.csv
    past_service_date_items = [item for item in inventory.values() if item.service_date < '2023-07-18']
    past_service_date_items_sorted = sorted(past_service_date_items, key=lambda x: x.service_date)
    with open('PastServiceDateInventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])
        for item in past_service_date_items_sorted:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.is_damaged])

    # Generate DamagedInventory.csv
    damaged_items = [item for item in inventory.values() if item.is_damaged]
    damaged_items_sorted = sorted(damaged_items, key=lambda x: x.price, reverse=True)
    with open('DamagedInventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date'])
        for item in damaged_items_sorted:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date])

process_inventory()

#Code finished and ready to generate outputs