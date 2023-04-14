import  csv
from admin import Admin

obj = Admin()

class User:
    def __init__(self):
        self.historyfields = ['Item_Name','Quantity','Price']
        self.filename = 'user_reg_data.csv'
        self.fields = ['User_Name', 'Phone_Number', 'Email', 'Address', 'Password']
        self.ordered_item = []


        with open(self.filename, 'r+') as reader:
            read = csv.reader(reader)
            if self.fields != next(read, []):
                writer = csv.DictWriter(reader, self.fields)
                writer.writeheader()

        with open('order_history.csv', 'r+') as reader1:
            read1 = csv.reader(reader1)
            if self.historyfields != next(read1, []):
                writer1 = csv.DictWriter(reader1, self.historyfields)
                writer1.writeheader()

    def user_reg(self):
        user_name = input("Enter your full name : ")
        phone_no = int(input("Enter your 10 digit phone number : "))
        email = input("Enter your email id : ")
        address = input("Enter your address with area PIN code ")
        password = input("Enter your password : ")


        with open(self.filename, 'a', newline='') as file:
            user_data = [user_name, phone_no, email, address, password]
            writer = csv.writer(file)
            writer.writerow(user_data)
            print('User Registered Successfully')


    def user_login(self, email, password):
        data = {}
        with open(self.filename) as read:
            read1 = csv.DictReader(read)
            for i in read1:
                if email == i['Email']:
                    if password == i['Password']:
                        return True
                # else:
                #     return False


    def show_user(self):
        with open(self.filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)


    def place_order(self):
        try:
            print("Our Menu is :")
            menu = []
            cart = []
            with open('food_data.csv') as read:
                reader = csv.DictReader(read)
                for food in reader:
                    menu.append([food['Name'], food['Quantity'], int(food['Price'])])
                print('Item_Name\tQuantity\tPrice')
                i = 1
                for food in menu:
                    print(i, end =' '),print(food[0], end='\t\t'),print(food[1], end='\t\t'),print(food[2])
                    i+=1
                while True: 
                    x = input('Enter 1 to choose items\nEnter 2 to see cart and confirm order\nEnter 3 to exit :')
                    if x == '1':
                        choose = input("Enter the Food number you want to order separated by comma :")
                        value = choose.split(',')
                        for i in value:
                            z = int(i)
                            if z <= len(menu):
                                cart.append(menu[z-1])                            
                            else:
                                print('Please select the valid food number')
                        print('Item Added to cart Successfully')
                    elif x == '2':
                        if len(cart) > 0:
                            print('Item_Name\tQuantity\tPrice')
                            for food in cart:
                                print(food[0], end='\t\t'),print(food[1], end='\t\t'),print(food[2])
                            c = input('Press 1 to confirm and place the order\nPress 2 to cancel the order')
                            if c =='1':
                                self.ordered_item = cart.copy()
                                print('Order placed successfully')
                            elif c=='2':
                                cart.clear()
                                print('Items removed from cart')
                            else:
                                print('Invalid entry please choose correct option')
                        else:
                            print('Your cart is empty, Please add items in cart')
                    elif x == '3':
                        break
                    else:
                        print('Invalid Entry please choose valid option') 
            with open('order_history.csv','a') as wr:
                write  = csv.writer(wr)
                write.writerows(self.ordered_item)
        except:
            print('Something wrong happened, Please try again later')

    def order_history(self):
        print("The Order History till now is :")
        with open('order_history.csv') as read:
            read1 = csv.DictReader(read)
            for i in read1:
                print(i)

    def edit_user(self):
        try:
            with open(self.filename) as file:
                reader = csv.DictReader(file)
            # self.show_user()
                username = input('Please confirm your Full Name :')
                current = [row for row in reader if row['User_Name'] == username]
            if len(current) > 0:
                print("Your current details are : ")
                print(current)
                value = input('Choose what would you like to edit(i.e User_Name, Phone_Number, Email, Address, Password) :')
                new_value = input('Please enter the new value :')
                rows = []
                with open(self.filename, 'r+') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['User_Name'] == username:
                            row[value] = new_value
                        rows.append(row)
                with open(self.filename, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=self.fields)
                    writer.writeheader()
                    writer.writerows(rows)
                    print('Details updated successfully')
            else:
                print('You must enter the correct name in order to edit details')
        except:
            print('Something wrong happened, Please try again later')


# use = User()
# use.edit_user()
# use.show_user()
# use.place_order()
# use.order_history()
# print(use.user_login('aakash123@gmail.com','Ragnar12'))