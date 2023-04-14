from admin import Admin
from user import User

obj = Admin()
use = User()


def admin_data():
    print('******* WELCOME TO THE ADMIN PANEL FOR ZOMATO  *****************')
    print('*******  PLEASE CHOOSE AN APPROPRIATE OPTION  *****************')
    while True:
        print('Enter D to Dispay Menu : ')
        print('Enter A to Add an Item : ')
        print('Enter E to Edit Food : ')
        print('Enter Q to Quit Menu : ')
        print('Enter R to Remove an Item : ')
        action = input('Please enter your action : ')

        if action == 'D':
            obj.displayList()

        elif action == 'A':
            obj.addFood()

        elif action == 'E':
            obj.editFood()

        elif action == 'Q':
            break
        
        elif action == 'R':
            obj.removeFood()

def user_data():
        
    print('******* WELCOME TO ZOMATO FOOD DELIVERY *****************')
    print('*******PLEASE CHOOSE AN APPROPRIATE OPTION BELOW ********')

    while True:
        print('Enter H to Show Order History : ')
        print('Enter U to Update Profile : ')
        print('Enter P to Place new order : ')
        print('Enter Q to Quit Menu : ')
        action = input('Please enter your action : ')

        if action == 'H':
            use.order_history()

        elif action == 'U':
            use.edit_user()

        elif action == 'P':
            use.place_order()

        elif action == 'Q':
            break

        else:
            print('Invalid Entry, Please try Again* ')

while True:

    x = input("Enter A for Admin\nEnter U for User\nEnter E to Exit App : ")
    if x == 'A':
        username = input('Please Enter your Username :')
        password = input('Please Enter your Password :')
        check = obj.admin_login(username, password)
        if check == True:
            print('Login Successful!!!!')
            admin_data()
        else:
            print('Invalid Login credentials')

    elif x =='E':
        break
    elif x == 'U':
        while True:
            d = input('Enter L to Login\nEnter R to Register in App\nEnter E to Return in Main Menu :')

            if d == 'L':
                email = input('Please Enter your Email :')
                password = input('Please Enter your Password :')
                check = use.user_login(email, password)
                if check == True:
                    print('Login Successful!!!')
                    user_data()
                else:
                    print('Invalid Login credentials!!')

            elif d == 'R':
                use.user_reg()
            elif d == 'E':
                break
        
    else:
        print('Invalid Entry, Please try again.')