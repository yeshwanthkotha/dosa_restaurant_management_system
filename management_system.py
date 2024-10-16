import json

def load_orders(file):
    with open(file, 'r') as f:
        orders = json.load(f)
    return orders

orders = load_orders('example_orders.json')
print(orders)
