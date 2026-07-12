Library Management System is a Python-based application that manages books, members, and borrowing records. The system allows librarians to add books and members, issue and return books, maintain borrowing records, and store all information permanently using CSV files. It also records system activities through a logging mechanism and displays borrowed book records in a tabular format using Pandas.

Features

- Add new books to the library
- Register library members
- Prevent duplicate Book IDs and Member IDs
- Issue books to members
- Return borrowed books
- Automatically update the number of available book copies
- Display borrowed book records in a table
- Store all data permanently using CSV files
- Automatically create required data files if they do not exist
- Log successful operations with timestamps

Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects
- File Handling
- CSV File Operations
- Exception Handling
- Dictionaries
- Functions
- Decorators
- Logging
- Date and Time ("datetime")
- File and Directory Management ("os" module)
- Pandas DataFrames
- Function Wrappers ("functools.wraps")

Requirements

- Python 3.x
- Pandas

Install Pandas using:

pip install pandas

Project Structure

Library-Management-System/
│
├── library_management_system.py
├── book.csv
├── member.csv
├── borrow.csv
├── logs.txt
└── README.md

How to Run

1. Download or clone this repository.
2. Install the required dependency:
   pip install pandas
3. Open a terminal in the project folder.
4. Run the following command:

python library_management_system.py

«Replace "library_management_system.py" with your actual Python filename if it has a different name.»

Menu Options

1. Add Book
2. Add Member
3. Borrow Book
4. Return Book
5. Display Borrowed Books
6. Exit

Data Files

- book.csv – Stores book details.
- member.csv – Stores member information.
- borrow.csv – Stores borrowing and return records.
- logs.txt – Stores activity logs with timestamps.

Author

Developed by Palak as part of a Python learning journey.