import csv

class Admin:
    
    def __init__(self):
        self.username = 'HackerAdmin'
        self.password = 'welcomehacker'
        self.foodId = '1000'
        self.fields = ['Food_ID', 'Name', 'Quantity', 'Price', 'Discount', 'Stock']
        self.filename = 'food_data.csv'

        with open(self.filename, 'r+') as reader:
            read = csv.reader(reader)
            if self.fields != next(read, []):
                writer = csv.DictWriter(reader, self.fields)
                writer.writeheader()

    def admin_login(self, username, password):
        if username == self.username and password == self.password:
            return True
        else:
            return False
        

    def addFood(self):
        name = input("Please Enter the Item you would like to Add: ")
        quantity = input("Please Enter the Quantity you would like to Add: ")
        price = input("Please Enter the price of Item: ")
        discount = input("Enter Discount for Item: ")
        stock = input("Enter Stock available for Item: ")
        with open(self.filename) as fr:
            r = csv.reader(fr)
            self.foodId = 0
            for i in r:
                if len(i) > 0:
                    self.foodId = i[0]
        
        with open(self.filename, 'a', newline='') as file:
            food_item = [str(int(self.foodId)+1), name, quantity, price, discount, stock]
            writer = csv.writer(file)
            writer.writerow(food_item)
            print('Food is Added Successfully!!')
            
    def displayList(self):
        with open(self.filename) as file:
            reader = csv.DictReader(file)
            print('Food_ID\t\tName\t\t\tQuantity\tPrice\t\tDiscount\tStock')
            for row in reader:
                print(row['Food_ID'],end='\t\t'),print(row['Name'],end='\t\t'),print(row['Quantity'],end='\t\t')
                print(row['Price'],end='\t\t'),print(row['Discount'],end='\t\t'),print(row['Stock'])

    def removeFood(self):
        foodid = input('Please Enter the Food ID which you would like to Remove :')
    
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader if row['Food_ID'] != foodid]

        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(rows)
    
        print(f"Food with ID {foodid} has been Removed from the list.")

    def editFood(self):
        self.displayList()

        foodid = input('Please Enter the Food ID which you would like to Edit :')
        value = input('Choose what would you like to edit(i.e Name, Quantity, Price, Discount, Stock) :')
        new_value = input('Please enter the new value :')
        with open(self.filename, 'r+') as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                if row['Food_ID'] == foodid:
                    row[value] = new_value
                rows.append(row)

        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(rows)
            print('Items is updated Successfully!!')
                
# obj = Admin()
# obj.addFood()
# obj.removeFood()
# obj.displayList()
# obj.editFood()