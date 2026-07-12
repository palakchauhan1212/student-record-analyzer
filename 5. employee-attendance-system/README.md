Employee Attendance Management System is a Python-based application that helps manage employee records and daily attendance. The system allows users to register employees, record attendance, generate individual attendance reports, and maintain persistent data using JSON files. It also keeps a log of important system activities.

Features

- Register new employees
- Prevent duplicate employee registrations
- Store employee information using JSON files
- Mark daily attendance
- Generate attendance reports for individual employees
- Calculate attendance percentage
- Display all registered employees
- Record important system activities in a log file
- Automatically create required data files if they do not exist

Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects
- File Handling
- JSON Serialization and Deserialization
- Exception Handling
- Dictionaries
- Loops and Conditional Statements
- Functions
- Date and Time ("datetime")
- File and Directory Management ("os" module)

Project Structure

Employee-Attendance-Management-System/
│
├── employee_attendance_system.py
├── employee_data.json
├── attendance_data.json
├── logs.txt
└── README.md

Requirements

- Python 3.x

How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the following command:

python employee_attendance_system.py

«Replace "employee_attendance_system.py" with your actual Python filename if it has a different name.»

Menu Options

1. Register Employee
2. Mark Attendance
3. Employee Report
4. Display Employees
5. Exit

Data Files

- employee_data.json – Stores employee details.
- attendance_data.json – Stores attendance records.
- logs.txt – Stores a log of important system actions.

Author

Developed by Palak as part of a Python learning journey.