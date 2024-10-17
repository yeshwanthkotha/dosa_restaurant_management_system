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
        # Avoid overwriting if the phone number already exists
        if phone not in customers:
            customers[phone] = name
    return customers


orders = load_orders('example_orders.json')
#print(orders)
customers = extract_customers(orders)
print(customers)