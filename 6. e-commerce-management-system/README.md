Inventory Management System is a Python-based application that helps manage product inventory. The system allows users to add, update, remove, and search for products while storing product information permanently using JSON files. It also generates a basic inventory report containing useful statistics about the stored products.

Features

- Add new products
- Prevent duplicate product IDs
- Update product quantity
- Remove products from inventory
- Search products by Product ID or Product Name
- Display inventory statistics
- Store product information permanently using JSON
- Automatically create the required data file if it does not exist

Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects
- File Handling
- JSON Serialization and Deserialization
- Exception Handling
- Dictionaries
- Lists
- Loops and Conditional Statements
- Lambda Functions
- File and Directory Management ("os" module)

Project Structure

Inventory-Management-System/
│
├── inventory_management_system.py
├── product_data.json
└── README.md

Requirements

- Python 3.x

How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the following command:

python inventory_management_system.py

«Replace "inventory_management_system.py" with your actual Python filename if it has a different name.»

Menu Options

1. Add Product
2. Update Product
3. Remove Product
4. Search Product
5. Inventory Report
6. Exit

Inventory Report

The report displays:

- Total number of products
- Total stock available
- Most expensive product
- Least expensive product

Data File

- product_data.json – Stores product information permanently.

Author

Developed by Palak as part of a Python learning journey.