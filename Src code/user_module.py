import dataHandle

class User:
    user_list = dataHandle.getUser()
    
    def __init__(self) -> None:
        pass

    def registerNewUser(self, name, number, email, address, password):
        self.name = name
        self.number = number
        self.email = email
        self.address = address
        self.password = password
        userDetails= {}
        userDetails['Name'] = self.name
        userDetails['Phone No'] = self.number
        userDetails['Email ID'] = self.email
        userDetails['Address'] = self.address
        userDetails['Password'] = self.password
        User.user_list.append(userDetails)
        dataHandle.setUser(User.user_list)
        print("\nRegistration Successfull...")
    
    def get_all_users(self):
        for usr in User.user_list:
            for u in usr:
                print(f'{u} : {usr[u]}')
            print()
    
    def Log_in(self,email):
        self.LoginEmail = email
        
        while True:
            LoginPassword = input("Enter Your Password: ")
            for user in User.user_list:
                if self.LoginEmail == user['Email ID']:
                    if LoginPassword == user['Password']:
                        print('Welcome back! ',user['Name'])
                        return True
                    else:
                        print("Warn- Wrong Password. Please enter correct password!!!")
            
        return False
    
    def profile(self,email):
        self.email= email
        for user in User.user_list:
            if self.email == user['Email ID']:
                for u in user:
                    print(f'{u} : {user[u]}')
                break
    
    def Update_profile(self,email):
        self.email= email
        for user in User.user_list:
            if self.email == user['Email ID']:
                user['Name']= input("Enter Full Name: ")
                user['Phone No']= input("Enter Phone No: ")
                user['Address']= input("Enter Address: ")
                user['Password']= input("Enter New Password: ")
                dataHandle.setUser(User.user_list)
                print("Details Update Successfully!")
                

def userIdValidate():
    
    while True:
        email_input = input("Enter Your Email: ")
        if UserPresentOrNot(user_obj.user_list,email_input):
            return email_input
        else:
            print("Warn- Email id not found. Please try again!!!")

    

def UserPresentOrNot(Lists,value):
    for elem in Lists:
        if value in elem.values():
            return True
    return False

def UserOrderHistory(email):
    try:
        rp = open(email+'_Orders.txt')
        data = rp.read()
        rp.close()
        print(data)
    except Exception:
        print("History not found!")

def Registration():
    name = input("Enter your full name: ")
    number = input("Enter your Phone number: ")
    email = input("Enter your Email ID: ")
    address = input("Enter your Address: ")
    password = input("Create your password: ")
    user_obj.registerNewUser(name,number,email,address,password)


user_obj = User()

