import random
import datetime as dt
import dataHandle

class Food:
    food_List = dataHandle.getFood()
    
    def __init__(self) -> None:
        pass
    
    def set_item(self, name, quantity, price, discount, stock):
        self.name = name
        self.quantity = quantity
        self.price= price
        self.discount = discount
        self.stock = stock
        ItemDict = {}
        def foodId():
            id_list=[2,3,5,6,7]
            while True:
                food_Id = random.randint(100,999)
                print("Food Id :",food_Id)
                if food_Id not in id_list: 
                    id_list.append(food_Id)
                    break
            return food_Id
        ItemDict['Food ID']= foodId()
        ItemDict['Name']= self.name
        ItemDict['Quantity']= self.quantity
        ItemDict['Price']= self.price
        ItemDict['Discount']= self.discount
        ItemDict['Stock']= self.stock
        Food.food_List.append(ItemDict)
        dataHandle.setFood(Food.food_List)
        print("Item Added Successfully!!!")
    
    def edit_item(self):
        while True:
            Id_input = int(input("Please enter the food id that you want to edit: "))
            if ItemPresentorNot(Food.food_List,Id_input):
                for item in Food.food_List:
                    if Id_input == item['Food ID']:
                        item['Name']= input("Enter Food Name: ")
                        item['Quantity']= input("Enter Food Quantity: ")
                        item['Price']= input("Enter Food Price: ")
                        item['Discount']= input("Enter Food Discount(%): ")
                        item['Stock']= input("Enter Food Stock: ")
                        dataHandle.setFood(Food.food_List)
                        print("Item Update Successfully!")
                        
                break
            else:
                print("Warn- Wrong id! Please try again!!")
    
    def get_all_item(self):
        for i in Food.food_List:
            print(i)

    def remove_item(self):
        while True:
            Id_input = int(input("Please enter the food id that you want to remove: "))
            if ItemPresentorNot(Food.food_List,Id_input):
                for item in Food.food_List:
                    if item['Food ID']==Id_input:
                        Food.food_List.remove(item)
                        dataHandle.setFood(Food.food_List)
                        print("Item was successfully removed of food id: ",Id_input)
                break
            else:
                print("Warn- Wrong id! Please try again!!")

def ItemPresentorNot(Lists,value):
    for elem in Lists:
        if value in elem.values():
            return True
    return False

def addNewFoodItem():
    Name= input("Enter Food Name: ")
    Quantity= input("Enter Food Quantity: ")
    Price= input("Enter Food Price: ")
    Discount= input("Enter Food Discount(%): ")
    Stock= input("Enter Food Stock: ")
    food_object.set_item(Name,Quantity,Price,Discount,Stock)

def PlaceNewOrder(email):
    foodItems = food_object.food_List
    # print(foodItems)
    sr_no = 1
    for item in foodItems:
        print(sr_no,'. ',item['Name'],' (',item['Quantity'],')  [ INR',item['Price'],']')
        sr_no += 1
    inputFoodList = [int(item)-1 for item in input("Enter the number of food that you want to eat : ").split()]
    # print(inputFoodList)
    totalPrice = 0
    chooseFoodList = []
    for i in inputFoodList:
        cal = int(foodItems[i]['Price'])-(((int(foodItems[i]['Price'])/100))*int(foodItems[i]['Discount']))
        foodName = foodItems[i]['Name']
        chooseItem = f'{foodName}(*with discount) -  INR {round(cal,2)}'
        chooseFoodList.append(chooseItem)
        print(chooseItem)
        totalPrice += cal
    print('\nTotal Price (*with discount) =  INR',round(totalPrice,2))
    while True:
        placeOrderInput= input("\nDo you want to place this order: \n1. YES \n2. NO \n")
        if placeOrderInput=='1':
            now = dt.datetime.now().strftime("[%d/%m/%Y | %H:%M:%S]")
            fp = open(email + '_Orders.txt', 'a+')
            fp.write(now + ' :- \n\t\t' + '\n\t\t'.join(chooseFoodList)+ '\n\tTotal Price (*with discount) =  INR '+str(totalPrice) + '\n')
            fp.close()
            print("---Thank you for ordering---\n")
            break
        elif placeOrderInput=='2':
            break
        else:
            print("Invalid choice! Try again... ")
    

food_object = Food()