#Sydney Ani PID: 1869076

#Creating class for the inputs and outputs
class Item:
    def __init__(self, item_id, manufacturer, item_type, price, service_date, is_damaged):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.price = price
        self.service_date = service_date
        self.is_damaged = is_damaged
