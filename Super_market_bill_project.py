#SUPER-MARKET-BILL-PROJECT

name = input("Enter your name :")

#List of items and prices..

lists = '''
Rice     Rs 10/kg
Sugar    Rs 8/kg
Milk     Rs 30/packet
Oil      Rs  30/liter
Salt     Rs   30/kg
Paneer   Rs   40/kg
Maggie   Rs    15/packet
Boost    Rs    240/packet
meraj    Rs      25/packet
'''
print(lists)

#declarations

price = 0
total_price = 0
final_amount = 0
pricelist = []
itemslist = []
plist = []
quantitylist = []

items = {'rice': 10, 'milk': 30, 'sugar' : 8, 'oil': 30, 'salt':30, 'paneer':40, 'maggie':15, 'boost':240 , 'meraj':25}

while True:
    choice = input("select 1 for list or 2 for exit :")
    if choice == "2":
        print("Thanks for visiting")
        break
    if choice == "1":
        print("lists")

        while True:
            option = input("Enter 1 for buying or 2 for exit :")
            if option == "2":
                print('Thanks for visitig')
                break
            elif option == "1":
                item = input("choose your items :").lower()
                
            while True:
                 quantity_input = input("Enter your quantity:")
                 if quantity_input.isdigit():
                   quantity = int(quantity_input)
                   break
                 else:
                     print("Enter valid quantity")

            if item in items:
               price = quantity * items[item]
               pricelist.append((item , quantity , items[item], price))  
               total_price+= price
               itemslist.append(item)
               quantitylist.append(quantity)
               plist.append(price)
            else:
                print("Selected item is not items list")
         
        if total_price > 0:
            tax = (total_price*18)/100
            final_amount = tax + total_price

            print(30*"=","Naidu's supermarket", 30*"=")
            print(25*" ", "Seetharamapuram")
            print('name:',name,25*" ", "August 06 2026")
            print(100*"-")
            print("sno",20*" ","items", 20*" ", "quantity",20*" ","price")
            for i in range(len(pricelist)):
                print(i, 22*" ",itemslist[i], 23*" ", quantitylist[i], 24*" ",plist[i])
            print(100*"-")
            print(50*" ", 'TOTAL AMOUNT','RS.',total_price)
            print('TAX amount',50*" ",'RS.',tax)
            print(100*"-")
            print(50*" ",'FINAL AMOUNT','RS.',final_amount)
            print(100*"-")
            print(25*" ",' Thank you & visit again ')
            print(100*"-")
            
               




