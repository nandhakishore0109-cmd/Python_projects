# ATM PROJECT USING OOPS CONCEPT.....

class ATM():

    def __init__(self,name,branch,village,balance):
        self.name = name 
        self.branch = branch
        self.village = village
        self.balance = balance
        self.transactions =[]

    def credit(self):
        amount = float(input("Enter a crediting amount :"))
        if amount <= 0:
            print("Enter a crediting amount")

        else:
            self.balance+= amount
            self.transactions.append(amount)
            print(f"Your credited amount is {amount}")

    def debit(self):
        amount = float(input("Enter a debiting amount:"))
        if amount > self.balance:
            print("Insufficient balane")    

        else:
            self.balance-= amount
            self.balance.append(amount) 

    def check_balance(self):
        print(f"Your current balance is {self.balance}")

class ministatement(ATM):
    def mini_statement(self):
        if len(self.transactions) == 0:
            print("Your data is not found.")
        else:
            for i in self.transactions:
                print(f'Transactions',i)

    def exit(self):
        print(f"Thank you.Welcome")


object = ministatement('sbi','canara', 'seetharampuram',1000)

while True:

    print("1.credit")
    print("2.debit")
    print("3.check_balance")
    print("4.mini_statement")
    print("5.exit")


    choice = input("Enter your choice (1-5)")

    if choice == '1':
        object.credit()
    elif choice == '2':
        object.debit()
    elif choice == '3':
        object.check_balance()
    elif choice == '4':
        object.mini_statement()
    else:
        object.exit
        break    
