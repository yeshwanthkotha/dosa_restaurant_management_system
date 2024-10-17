# **dosa_restaurant_management_system**

## Project Overview

This project is designed to process the order data from a JSON file for a dosa restaurant. It extracts customer information and item statistics from the orders and saves them into separate JSON files. The project implements the following functionalities:

* Extracts customer details (phone numbers and names) and stores them in <mark>customers.json</mark>.
* Extracts item details (item names, prices, and number of times ordered) and stores them in <mark>items.json</mark>.

## How It Is Designed

The project processes a JSON file containing multiple orders. Each order includes:

* A timestamp (ignored in the processing)
* Customer details (name and phone number)
* A list of ordered items (name and price)

### Files Generated:
<mark>**customers.json:**</mark> Contains a mapping of phone numbers to customer names.

<mark>**items.json:**</mark> Contains item details with their price and the total number of times they have been ordered.


## How to Use the Project

### Running the Program
**1. Clone the repository from GitHub:**
```bash
git clone https://github.com/yourusername/dosa-orders.git
```
Navigate to the project directory:
```bash
cd dosa-orders
```
Run the program to process the orders and generate the output files:
```bash
python script.py example_orders.json
```

### Output Files:
**customers.json: This file will contain customer phone numbers as keys and customer names as values in the following format:**
```json
{
    "609-555-0124": "Karl",
    "732-555-1234": "Mike"
}
```
**items.json: This file will contain item names as keys and their details (price and number of times ordered) as values:**
```json
{
    "Butter Masala Dosa": {
        "price": 12.95,
        "orders": 52
    },
    "Butter Mysore Masala Dosa": {
        "price": 11.95,
        "orders": 12
    }
}
```
