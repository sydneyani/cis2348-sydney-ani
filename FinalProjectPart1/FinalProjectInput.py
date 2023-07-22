#Sydney Ani PID: 1869076

#Allowing the csv files to be read by my output code
import csv

def read_csv(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            item_id = row[0]
            data[item_id] = row[1:]
    return data

#Here I list the csv input files that MUST be read for the output
manufacturer_data = read_csv('ManufacturerList.csv')
price_data = read_csv('PriceList.csv')
service_date_data = read_csv('ServiceDatesList.csv')

process_inventory()
