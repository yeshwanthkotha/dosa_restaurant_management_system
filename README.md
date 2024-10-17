# **dosa_restaurant_management_system**

##Project Overview

This project is designed to process the order data from a JSON file for a dosa restaurant. It extracts customer information and item statistics from the orders and saves them into separate JSON files. The project implements the following functionalities:

* Extracts customer details (phone numbers and names) and stores them in #customers.json.

* Extracts item details (item names, prices, and number of times ordered) and stores them in items.json.

##How It Is Designed

The project processes a JSON file containing multiple orders. Each order includes:

*A timestamp (ignored in the processing)
*Customer details (name and phone number)
*A list of ordered items (name and price)
*Optional notes (ignored in the processing)
