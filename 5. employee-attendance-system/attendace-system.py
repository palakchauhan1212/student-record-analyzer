import os
import json
from datetime import datetime

class EmployeeAttendanceSystem:
    BAS_DIR = os.path.dirname(os.path.abspath(__file__))
    EMPLOYEE_FILE = os.path.join(BAS_DIR,"employee_data.json")
    ATTENDANCE_FILE = os.path.join(BAS_DIR,"attendance_data.json")
    LOG_FILE = os.path.join(BAS_DIR,"logs.txt")

    def __init__(self):
        self.create_file_if_not_exist()
        self.employees = self.load_data(self.EMPLOYEE_FILE)
        self.attendance = self.load_data(self.ATTENDANCE_FILE)
    
    def create_file_if_not_exist(self):
        if not os.path.exists(self.EMPLOYEE_FILE):
            with open(self.EMPLOYEE_FILE,"w")as file:
                json.dump({},file)
        if not os.path.exists(self.ATTENDANCE_FILE):
            with open(self.ATTENDANCE_FILE,"w")as file:
                json.dump({},file)
        if not os.path.exists(self.LOG_FILE):
            with open(self.LOG_FILE,"w")as file:
                file.write("===Employee Attendance Logs===\n")

    def load_data(self,filename):
        try:
            with open(filename,"r")as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return{}
    
    def save_data(self):
        with open(self.EMPLOYEE_FILE,"w")as file:
            json.dump(self.employees, file, indent=4)
        with open(self.ATTENDANCE_FILE,"w")as file:
            json.dump(self.attendance, file, indent=4)

    def log_action(self,message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.LOG_FILE,"a")as file:
            file.write(f"[{timestamp}] {message}\n")
    
    def register_employee(self,employee_id,name,department):
        if employee_id in self.employees:
            print("Employee already exist")
            return
        self.employees[employee_id] = {"name":name, "department":department}
        self.save_data()
        self.log_action(f"Employee added: {employee_id}")
        print("Employee added successfully")

    def mark_attendance(self,date):
        if date in self.attendance:
            print("Attendance already marked for this date")
        daily_record = {}
        for employee_id,details in self.employees.items():
            while True:
                status = input(f"{details['name']} (Present/Absent):").strip().title()
                if status in ("Present","Absent"):
                    break
                print("Invalid status.Enter Present or Absent.")
            daily_record[employee_id] = status
        self.attendance[date] = daily_record
        self.save_data()
        self.log_action(f"Attendance marked: {date}")
        print("Attendance stored successfully")

    def emloyee_report(self,employee_id):
        if employee_id not in self.employees:
            print("Employee not found")
            return
        total_days = len(self.attendance)
        present_days = 0
        absent_days = 0
        for daily_record in self.attendance.values():
            status = daily_record.get(employee_id)
            if status == "Present":
                present_days += 1
            elif status == "Absent":
                absent_days += 1

        attendance_percent = 0
        if total_days>0:
            attendance_percent = (present_days/total_days)*100
        employee = self.employees[employee_id]

        print("\nEmployee Report")
        print("-"*40)
        print("ID:",employee_id)
        print("Name:",employee['name'])
        print("Department:",employee['department'])
        print("Working Days:",total_days)
        print("Present:",present_days)
        print("Absent:",absent_days)
        print(f"Attendance %: {attendance_percent:.2f}%")

        self.log_action(f"Report Generated: {employee_id}")

    def display_employees(self):
        if not self.employees:
            print("No employees registered")
            return
        print("\nEmployee Databse:")
        print("-"*40)
        for emp_id, details in self.employees.items():
            print(f"{emp_id} -> " f"{details['name']} -> " f"{details['department']}")

def main():
    system = EmployeeAttendanceSystem()
    while True:
        print('''
1. Register employee
2. Mark attendance
3. Employee report
4. Display employees
5. Exit''')
        choice = input("Enter choice:")
        if choice == "1":
            employee_id = input("Employee ID:")
            name = input("Name:")
            department = input("Department:")
            system.register_employee(employee_id,name,department)
        elif choice == "2":
            date = input("Date (YYY-MM-DD):")
            system.mark_attendance(date)
        elif choice == "3":
            employee_id = input("Employee ID:")
            system.emloyee_report(employee_id)
        elif choice == "4":
            system.display_employees()
        elif choice == "5":
            print("Goodbye")
            break   
        else:
            print("Invalid Choice!")
if __name__=="__main__":
    main()