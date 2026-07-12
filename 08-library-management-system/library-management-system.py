import os
import csv
import pandas as pd
from datetime import datetime
from functools import wraps

def log_activity(action_name):
    @wraps(log_activity)
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            if result is not False:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                args_str = ", ".join([str(arg) for arg in args])
                log_msg = f"[{timestamp}] SUCCESS: {action_name} | Target Details: ({args_str})\n"
                try:
                    with open(self.log_file, 'a')as f:
                        f.write(log_msg)
                except IOError as e:
                    print(f"[Warning] Failed to write to log file: {e}")
            return result
        return wrapper
    return decorator

class ManagementSystem:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
        self.books_file = os.path.join(base_dir, "book.csv")
        self.members_file = os.path.join(base_dir, "member.csv")
        self.borrowed_file = os.path.join(base_dir, "borrow.csv")
        self.log_file = os.path.join(base_dir, "logs.txt")
        self.create_file_if_not_exist()
        self.book = self.load_book()
        self.member = self.load_member()
        self.borrow = self.load_borrow()

    def create_file_if_not_exist(self):
        files = [(self.books_file, ['Book ID', 'Title', 'Author', 'Copies Available']),
                 (self.members_file, ['Member ID', 'Member Name']),
                 (self.borrowed_file, ['Member ID', 'Book ID', 'Issued Date', 'Returned Date'])]
        for file_path, headers in files:
            if not os.path.exists(file_path):
                try:
                    with open(file_path,'w', newline='', encoding='utf-8')as f:
                        writer = csv.writer(f)
                        writer.writerow(headers)
                except IOError as e:
                    print(f"Critical System Error initializing storage {file_path}: {e}")
        if not os.path.exists(self.log_file):
            try:
                with open(self.log_file,'w', encoding='utf-8')as f:
                    f.write("\n==========LOGS==========\n")
            except IOError:
                pass

    def load_book(self):
        books = {}
        try:
            with open(self.books_file, mode='r', newline='', encoding='utf-8')as f:
                reader = csv.DictReader(f)
                for row in reader:
                    books[row['Book ID']] = {
                        'Title': row['Title'],
                        'Author': row['Author'],
                        'Copies Available': row['Copies Available']
                    }
        except FileNotFoundError:
            pass
        return books

    def load_member(self):
        members = {}
        try:
            with open(self.members_file, mode='r', newline='', encoding='utf-8')as f:
                reader = csv.DictReader(f)
                for row in reader:
                    members[row['Member ID']] = {
                        'Member Name': row['Member Name']
                    }
        except FileNotFoundError:
            pass
        return members

    def load_borrow(self):
        borrow = {}
        try:
            with open(self.borrowed_file, mode='r', newline='', encoding='utf-8')as f:
                reader = csv.DictReader(f)
                for row in reader:
                    borrow[row['Member ID']] = {
                        'Book ID': row['Book ID'],
                        'Issued Date': row['Issued Date'],
                        'Returned Date': row['Returned Date']
                    }
        except FileNotFoundError:
            pass
        return borrow

    def save_data(self):
        try:
            with open(self.books_file, mode='w', newline='', encoding='utf-8')as f:
                writer = csv.DictWriter(f, fieldnames=['Book ID', 'Title', 'Author', 'Copies Available'])
                writer.writeheader()
                for b_id, info in self.book.items():
                    writer.writerow({
                        'Book ID': b_id,
                        'Title': info['Title'],
                        'Author': info['Author'],
                        'Copies Available': info['Copies Available']
                    })
            with open(self.members_file, mode='w', newline='', encoding='utf-8')as f:
                writer = csv.DictWriter(f, fieldnames=['Member ID', 'Member Name'])
                writer.writeheader()
                for m_id, info in self.member.items():
                    writer.writerow({
                        'Member ID': m_id,
                        'Member Name': info['Member Name']
                    })
            with open(self.borrowed_file, mode='w', newline='', encoding='utf-8')as f:
                writer = csv.DictWriter(f, fieldnames=['Member ID', 'Book ID', 'Issued Date', 'Returned Date'])
                writer.writeheader()
                for i_id, info in self.borrow.items():
                    writer.writerow({
                        'Member ID': i_id,
                        'Book ID': info['Book ID'],
                        'Issued Date': info['Issued Date'],
                        'Returned Date': info['Returned Date']
                    })
        except IOError as e:
            raise e

    @log_activity("Add Book")
    def add_book(self, book_id, title, author, copies):
        book_id = book_id.strip()
        title = title.strip()

        if copies<0:
            raise Exception ("Number of Copies cannot be negative")

        if not book_id or not title or not copies:
            raise Exception ("Book ID and Title and Copies cannot be blank")
        
        if book_id in self.book:
            raise Exception (f"Book ID {book_id} already exist")
        
        self.book[book_id] = {
            'Title':title,
            'Author':author.strip(),
            'Copies Available':copies
            }
        self.save_data()
        print(f"Book '{title}'(ID:{book_id}) added successfully")
        return True

    @log_activity("Add Member")
    def add_member(self, member_id, member_name):
        member_id = member_id.strip()
        member_name = member_name.strip()

        if not member_id or not member_name:
            raise Exception ("Member ID and Member Name cannot be blank")

        if member_id in self.member:
            raise Exception (f"Member ID '{member_id}' already exist")

        self.member[member_id] = {'Member Name':member_name}
        self.save_data()
        print(f"Member '{member_name}' added successfully")
        return True

    @log_activity("Issue Book")
    def borrow_book(self, book_id, member_id):
        today_date = datetime.now().strftime("%Y-%m-%d")
        if book_id not in self.book or member_id not in self.member:
            raise Exception ("Either Member ID or Book ID is wrong ")
        
        if int(self.book[book_id]['Copies Available']) <= 0:
            raise Exception (f"No copies available of {self.book[book_id]['Title']}({book_id})")

        if member_id in self.borrow and book_id not in self.borrow[member_id]['Book ID'] and self.borrow[member_id]['Returned Date']==0:
            raise Exception (f"{self.member[member_id]['Member Name']} already issued a book(ID:{self.borrow[member_id]['Book ID']})")

        self.borrow[member_id] = {
            'Book ID': book_id,
            'Issued Date': today_date,
            'Returned Date': 0
            }
        copies = int(self.book[book_id]['Copies Available'])
        copies -= 1
        self.book[book_id]['Copies Available'] = copies
        self.save_data()
        print(f"Member '{self.member[member_id]['Member Name']}' borrowed the book '{self.book[book_id]['Title']}'")
        return True

    @log_activity("Return Book")
    def return_book(self, book_id, member_id):
        today_date = datetime.now().strftime("%Y-%m-%d")
        if book_id not in self.book or member_id not in self.member:
            raise Exception ("Either Member ID or Book ID is wrong ")

        if member_id not in self.borrow or book_id not in self.borrow[member_id]['Book ID']:
            raise Exception (f"Book '{self.book[book_id]['Title']}' is not borrowed by {self.member[member_id]['Member Name']}")

        self.borrow[member_id]['Returned Date']= today_date
        copies = int(self.book[book_id]['Copies Available'])
        copies += 1
        self.book[book_id]['Copies Available'] = copies
        self.save_data()
        print(f"Member '{self.member[member_id]['Member Name']}' returned the book '{self.book[book_id]['Title']}'")
        return True

    def display_borrowed_book(self):
        print("="*16,"Borrowed Books","="*16)
        df = pd.DataFrame(self.borrow).T
        df.index.name = 'Member ID'
        df = df.reset_index()
        print(df)

def main():
    system = ManagementSystem()
    while True:
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Borrowed Books")
        print("6. Exit")
        choice = input("Enter your choice:")
        try:
            if choice == '1':
                book_id = input("Book ID:")
                title = input("Book Title:")
                author = input("Book Author:")
                copies = int(input("Copies Available:"))
                system.add_book(book_id, title, author, copies)

            elif choice == '2':
                member_id = input("Member ID:")
                member_name = input("Member Name:")
                system.add_member(member_id, member_name)

            elif choice == '3':
                book_id = input("Book ID:")
                member_id = input("Member ID:")
                system.borrow_book(book_id, member_id)

            elif choice == '4':
                book_id = input("Book ID:")
                member_id = input("Member ID:")
                system.return_book(book_id, member_id)

            elif choice == '5':
                system.display_borrowed_book()

            elif choice == '6':
                print("Session closed.\nGoodBye")
                break
            else:
                print("Invalid Choice")
        except Exception as e:
            print("Error:",e)
if __name__ == "__main__":
    main()