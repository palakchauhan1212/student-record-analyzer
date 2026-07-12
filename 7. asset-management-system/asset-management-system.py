import os
import json
from datetime import datetime

class ManagementSystem:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    asset_file = os.path.join(base_dir,"assets_file.json")
    employee_file = os.path.join(base_dir,"employees_file.json")
    assign_file = os.path.join(base_dir,"assigns_activities_file.json")
    log_file = os.path.join(base_dir,"logs.txt")

    def __init__(self):
        self.create_file_if_not_exist()
        self.assets = self.load_data(self.asset_file)
        self.employees = self.load_data(self.employee_file)
        self.assigns = self.load_data(self.assign_file)

    def create_file_if_not_exist(self):
        if not os.path.exists(self.asset_file):
            with open(self.asset_file,'w')as file:
                json.dump({},file)
        if not os.path.exists(self.employee_file):
            with open(self.employee_file,'w')as file:
                json.dump({},file)
        if not os.path.exists(self.assign_file):
            with open(self.assign_file,'w')as file:
                json.dump({},file)
        if not os.path.exists(self.log_file):
            with open(self.log_file,'w')as file:
                file.write('===Employee Attendance Logs===\n')

    def load_data(self,filename):
        try:
            with open(filename,'r')as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return{}
    
    def save_data(self):
        with open(self.asset_file,'w')as file:
            json.dump(self.assets,file, indent=4)
        with open(self.employee_file,'w')as file:
            json.dump(self.employees,file, indent=4)
        with open(self.assign_file,'w')as file:
            json.dump(self.assigns,file, indent=4)
    
    def log_action(self,message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file,'a')as file:
            file.write(f"[{timestamp}] {message}\n")

    def add_asset(self,asset_id,asset_name):
        if asset_id in self.assets:
            print('Asset ID already exist')
            return
        if asset_name.strip() == '' or asset_id == '' :
            print('Invalid Username or ID')
            return
        self.assets[asset_id] = {'Asset Name':asset_name, 'Status':'Available'}
        try:
            self.save_data()
            self.log_action(f"Asset added: {asset_id}")
        except Exception as e:
            print('Error:',e)
            return
        print("Asset added successfully")

    def add_employee(self,employee_id,employee_name,employee_department):
        if employee_id in self.employees:
            print('Employee ID already exist')
            return
        if employee_name.strip() == '' or employee_id == '':
            print('Invalid Username or ID')
            return
        self.employees[employee_id] = {'Name':employee_name,'Department':employee_department}
        try:
            self.save_data()
            self.log_action(f"Employee added: {employee_id}")
        except Exception as e:
            print('Error:',e)
            return
        print("Employee added successfully")

    def assign_asset(self,asset_id,employee_id):
        if asset_id not in self.assets or employee_id not in self.employees:
            print("Invalid ID's")
            return
        if self.assets[asset_id]['Status'] == 'Unavailable':
            print('Asset Unavailable')
            return
        if self.employees[employee_id]["Name"] in self.assigns:
            new_assign = self.assigns[self.employees[employee_id]["Name"]]["Assets"]
            new_assign.append(self.assets[asset_id]['Asset Name'])
            self.assigns[self.employees[employee_id]['Name']] = {"Assets":new_assign}
        else:
            new_assign = [self.assets[asset_id]['Asset Name']]
            self.assigns[self.employees[employee_id]["Name"]] = {"Assets":new_assign}
        self.assets[asset_id]['Status'] = 'Unavailable'
        try:
            self.save_data()
            self.log_action(f"Assign: {self.employees[employee_id]['Name']}(Employee ID:{employee_id}) -> {self.assets[asset_id]['Asset Name']}(Asset ID:{asset_id})")
        except Exception as e:
            print('Error:',e)
            return
        print("Asset assigned successfully")

    def return_asset(self,asset_id,employee_id):
        if asset_id not in self.assets or employee_id not in self.employees:
            print("Invalid ID's")
            return
        if self.assets[asset_id]['Status'] == 'Available':
            print('Asset is already Available')
            return
        if self.employees[employee_id]['Name'] not in self.assigns:
            print('This employee do not have any asset')
            return
        check = 0
        for employee, details in list(self.assigns.items()):
            assign_assets = details['Assets']
            if employee == self.employees[employee_id]['Name'] and self.assets[asset_id]['Asset Name'] in assign_assets:
                if len(assign_assets)>1:
                    assign_assets.remove(self.assets[asset_id]['Asset Name'])
                    check += 1
                else:
                    self.assigns.pop(employee)
                    check += 1
                self.assets[asset_id]['Status'] = 'Available'
                try:
                    self.save_data()
                    self.log_action(f"Unassign: {self.employees[employee_id]['Name']}(Employee ID:{employee_id}) -> {self.assets[asset_id]['Asset Name']}(Asset ID:{asset_id})")
                except Exception as e:
                    print('Error:',e)
                    return
                print("Asset unassigned successfully")
                break
        if check == 0:
            print('This asset is not with this employee')

    def search_asset(self,asset_id):
        try:
            print('Asset Name:',self.assets[asset_id]['Asset Name'])
            print('Asset Status:',self.assets[asset_id]['Status'])
            for employee, details in self.assigns.items():
                if self.assets[asset_id]['Asset Name'] in details['Assets']:
                    print('Assigned Employee:',employee)
        except Exception as e:
            print('Error:',e)

    def search_employee(self,employee_id):
        try:
            print('Employee Name:',self.employees[employee_id]['Name'])
            print('Employee Department',self.employees[employee_id]['Department'])
            for employee, details in self.assigns.items():
                if self.employees[employee_id]['Name'] == employee:
                    print('Assigned Assets:',details['Assets'])
        except Exception as e:
            print('Error:',e)

    def generate_report(self):
        available_assets = 0
        try:
            print('Total Assets:',len(self.assets))
            for asset, details in self.assets.items():
                if details['Status'] == 'Available':
                    available_assets += 1
            print('Available Assets:',available_assets)
            print('Assigned Assets:',len(self.assets)-available_assets)
        except Exception as e:
            print('Error:',e)

def main():
    system = ManagementSystem()
    while True:
        print('''
1. Add Asset
2. Add Employee
3. Assign Asset
4. Return Asset
5. Search Asset
6. Search Employee
7. Generate Reports
8. Exit
          ''')
        choice = input('Enter your choice:')
        try:
            if choice == '1':
                asset_id = input('Enter the Asset ID:')
                asset_name = input('Enter the Asset Name:')
                system.add_asset(asset_id,asset_name)

            elif choice == '2':
                employee_id = input('Enter Employee ID:')
                employee_name = input('Enter Employee Name:')
                employee_department = input('Enter Employee Department:')
                system.add_employee(employee_id,employee_name,employee_department)

            elif choice == '3':
                asset_id = input('Enter the Asset ID:')
                employee_id = input('Enter Employee ID:')
                system.assign_asset(asset_id,employee_id)

            elif choice == '4':
                asset_id = input('Enter the Asset ID:')
                employee_id = input('Enter Employee ID:')
                system.return_asset(asset_id,employee_id)

            elif choice == '5':
                asset_id = input('Enter the Asset ID:')
                system.search_asset(asset_id)

            elif choice == '6':
                employee_id = input('Enter the Employee ID:')
                system.search_employee(employee_id)

            elif choice == '7':
                system.generate_report()

            elif choice == '8':
                print('GOODBYE !!')
                break

            else:
                print('Invalid choice')
        except Exception as e:
            print('Error:',e)

if __name__ == "__main__":
    main()