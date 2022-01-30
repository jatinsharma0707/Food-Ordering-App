import food_item
import user_module

def adminFunction():
    while True:
        print("\n1. Add New Food Items \n2. Edit Food Items \n3. View All Food Items \n4. Remove Food Items \n0. Exit")
        admin_function_entry_input = input("\nChoose one of the following:-  ")
        if admin_function_entry_input=='1':
            print("\n-----Add New Food Items-----")
            food_item.addNewFoodItem()
        elif admin_function_entry_input=='2':
            print("\n-----Edit Food Items-----")
            food_item.food_object.edit_item()
        elif admin_function_entry_input=='3':
            print("\n-----View All Food Items-----")
            food_item.food_object.get_all_item()
        elif admin_function_entry_input=='4':
            print("\n-----Remove Food Items-----")
            food_item.food_object.remove_item()
        elif admin_function_entry_input=='0':
            print("Successfully Logout!")
            break
        else:
            print("Warn:- Wrong input try again!!")

def adminLogin():
    admin_name = "Jatin"
    admin_password = "jatin@123"
    admin_entry = False
    while admin_entry != True:
        admin_pass_input = input("Enter Your Password:-  ")
        if admin_pass_input == admin_password:
            print("\n---- Welcome", admin_name,"----")
            adminFunction()
            admin_entry = True
        else:
            print("Warn:- Wrong password try again!!")

def userLoginFunction(email):
    while True:
        userLoginFunctionInput= input("\n1. Place New Order \n2. Order History \n3. Update Profile \n4. View Profile \n0. Exit \nChoose one of the following:-  ")
        if userLoginFunctionInput == '1':
            print("\n-----Place New Order-----")
            food_item.PlaceNewOrder(email)
        elif userLoginFunctionInput == '2':
            print("\n-----Order History-----")
            user_module.UserOrderHistory(email)
        elif userLoginFunctionInput == '3':
            print("\n-----Update Profile-----")
            user_module.user_obj.Update_profile(email)
        elif userLoginFunctionInput == '4':
            print("\n-----View Profile-----")
            user_module.user_obj.profile(email)
        elif userLoginFunctionInput == '0':
            print("Successfully Logout!")
            break
        else:
            print("Warn:- Wrong input try again!!")


def userLogin():
    while True:
        profile_entry_input = input("\n1. New User \n2. Existing User \n0. Exit \nChoose one of the following:-  \n")
        if profile_entry_input=='1':
            print("------Register New User------\n")
            user_module.Registration()
            
        elif profile_entry_input=='2':
            print("-----Login to order your food-----\n")
            LoginEmail = user_module.userIdValidate()
            LoginValue= user_module.user_obj.Log_in(LoginEmail)
            if LoginValue:
                userLoginFunction(LoginEmail)
        
        elif profile_entry_input=='0':
            break

        else:
            print("Warn:- Wrong input try again!!")


if __name__ == '__main__' :  
    print("==========Food Ordering App==========")
    print("\nWhich one are You? \n 1. Admin \n 2. User")
    profile_entry = False
    while profile_entry != True:
        profile_entry_input = input("\nChoose either 1 or 2:-  ")
        if profile_entry_input=='1':
            print("----Hello Admin!----")
            adminLogin()
            profile_entry = True
        elif profile_entry_input=='2':
            print("----Hello User!----")
            userLogin()
            profile_entry = True
        else:
            print("Warn:- Wrong input try again!!")
    print("\n\tThank You For Using This App! \n===== Design & Code By - Jatin Sharma =====")
