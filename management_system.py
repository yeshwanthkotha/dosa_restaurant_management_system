import json

def load_orders(file):
    with open(file, 'r') as f:
        orders = json.load(f)
    return orders

def extract_customers(orders):
    customers = {}
    for order in orders:
        phone = order["phone"]
        name = order["name"]
        if phone not in customers:
            customers[phone] = name
    return customers

def extract_items(orders):
    items = {}
    for order in orders:
        for item in order["items"]:
            name = item["name"]
            price = item["price"]

            if name not in items:
                items[name] = {"price": price, "orders": 0}

            items[name]["orders"] += 1
    return items

def write_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

file_name = input("enter the file name(*.json files only):-")        
orders = load_orders('example_orders.json')
#print(orders)
customers = extract_customers(orders)
items = extract_items(orders)
#print(customers)
#print(items)
write_to_json(customers, 'customers.json')
write_to_json(items, 'items.json')