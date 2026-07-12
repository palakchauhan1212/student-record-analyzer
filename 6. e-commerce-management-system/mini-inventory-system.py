import os
import json
class ManagementSystem:
    BAS_DIR = os.path.dirname(os.path.abspath(__file__))
    PRODUCT_FILE = os.path.join(BAS_DIR, "product_data.json")

    def __init__(self):
        self.create_file_if_not_exist()
        self.products = self.load_data(self.PRODUCT_FILE)

    def create_file_if_not_exist(self):
        if not os.path.exists(self.PRODUCT_FILE):
            with open(self.PRODUCT_FILE,"w")as file:
                json.dump({},file)

    def load_data(self,PRODUCT_FILE):
        try:
            with open(PRODUCT_FILE,'r')as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return{}
    
    def save_data(self):
        with open(self.PRODUCT_FILE,'w')as file:
            json.dump(self.products, file, indent=4)

    def add_product(self,product_id,product_name,price,quantity):
        if product_id in self.products:
            print("This product ID already exists.")
            return
        self.products[product_id] = {'Name':product_name, 'Price':price, 'Quantity':quantity}
        self.save_data()

    def update_product(self,product_id,new_quantity):
        if product_id not in self.products:
            print("ID donot exist")
            return
        self.products[product_id]['Quantity'] = new_quantity
        self.save_data()

    def remove_product(self,product_id):
        if product_id not in self.products:
            print("ID donot exist")
            return
        del self.products[product_id]
        self.save_data()

    def search_product(self,product_info):
        if product_info in self.products:
            for product_id, details in self.products.items():
                if product_info == product_id:
                    print(f"ID -> {product_id}\nName -> {details['Name']}\nPrice -> {details['Price']}\nQuantity -> {details['Quantity']}")
        elif product_info in [item['Name'] for item in self.products.values()]:
            for product_id, details in self.products.items():
                if product_info == details['Name']:
                    print(f"ID -> {product_id}\nName -> {details['Name']}\nPrice -> {details['Price']}\nQuantity -> {details['Quantity']}")
        else:
            print("Product donot exist")

    def inventory_report(self):
        print("Total Products:",len(self.products))
        stock = [int(item['Quantity']) for item in self.products.values()]
        print("Total Stock:",sum(stock))
        price_list = [item['Price'] for item in self.products.values()]
        max_price = max(self.products.values(), key= lambda x: int(x['Price']))
        print("Most Expensive Product:",max_price['Name'])
        min_price = min(self.products.values(), key= lambda x: int(x['Price']))
        print("Least Expensive Product:",min_price['Name'])

def main():
    system = ManagementSystem()
    while True:
        print('''
1. Add Product
2. Update Product
3. Remove Product
4. Search Product
5. Inventory Report
6. Exit''')
        choice = input("Enter Choice:")
        if choice == "1":
            product_id = input("Product ID:")
            product_name = input("Product Name:")
            price = input("Price:")
            quantity = input("Quantity:")
            system.add_product(product_id,product_name,price,quantity)
        elif choice == "2":
            product_id = input("Product ID:")
            new_quantity =  input("New Quantity:")
            try:
                if int(new_quantity) < 0:
                    print("Quantity cannot be negative!!")
                    return
                else:
                    system.update_product(product_id,new_quantity)
            except (TypeError):
                print("Type Error")
        elif choice == "3":
            product_id = input("Product ID:")
            system.remove_product(product_id)
        elif choice == "4":
            product_info = input("Product ID or Name:")
            system.search_product(product_info)
        elif choice == "5":
            system.inventory_report()
        elif choice == "6":
            print("GoodBye!!")
            break
        else:
            print("Invalid Choice")
if __name__ == "__main__":
    main()