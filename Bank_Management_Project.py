# BANK-MANAGEMENT-USING OOPS AND FUNCTIONS..

class bank_account():
    def __init__(self,username,balance,pin):
        self.username = username
        self.balance = balance
        self.pin = pin
        self.credited = []
        self.debited = []

    def credit(self,amount):    
        if amount > 0:
            self.balance+= amount
            print(f'Successfully ur money deposited {amount}.')
            self.credited.append(amount)

        else:
            print('Valid amount, Try again.')

    def check_balance(self):
        print(f'Available balance is {self.balance}.')

    def debit(self,amount):
        if amount<=self.balance:
            self.balance-= amount
            self.debited.append(amount)
            print(f'The debited amount is {amount}.')

        else:
            print('Try again, Thank You.')   

    def ministatement(self):
        if len(self.debited) == 0 and len(self.credited) == 0:
            print('Result not found')

        else:
            for i in self.debited:
                print(f'The balance is {self.balance}')
            for j in self.credited:
                print(f'The credited balance {j}')

    def exit(self):
        print('Thank You For Visiting, Welcome')


class bank_account():
    def __init__(self):
            self.account={}

    def new_account(self,username,pin,balance):
        if username in self.account:
            print(f'User already exist...')

        else:
            self.account[username]=account(username,pin,balance)
            print(f'User account created succesfully...')

    def login(self,username,pin):
        if username in self.account:
            account = self.account[username]
            if account.pin == pin:
                print(f"Account created succesfully...")
                return account
            else:
                print('print vaild details..')


bank = bank_account()

while True:

    print('='*25,'Bank Management System','='*25)
    print('1.Create Account.')
    print('2.Login.')
    print('3.exit...')

    option = input('Enter a option:')

    if option == '1':
        username = input('Enter username:')
        pin = input('Enter ur pass:')
        balance = int(input('Enter a initial balance:'))
        bank.new_account(username,pin,balance)

    elif option == '2':
        username = input('Enter username:')
        pin = input('Enter ur pass:')
        acc = bank.login(username,pin)
        if acc:

            while True:

                print('='*25,'ATM-MENU','='*25)
                print('1.credit')
                print('2.debit') 
                print('3.check_balance')
                print('4.mini statement')
                print('5.exit')

                option = input('Enter a option:')

                if option == 1:
                    amount = int(input('Enter crediting amount:'))
                    acc.credit(amount) 

                elif option == '2':
                    amount = input('Enter ur debiting amount:')
                    acc.debit(amount) 

                elif option == '3':
                    acc.check_balance() 

                elif option == '4':
                    acc.ministatement() 

                elif option == '5':
                    acc.exit()
                    break
                else:
                    print('Enter valid option...')


        elif option == '3':
            bank.exit()
            print(f'Thanks for using, Good Bye...')
            break 

        else:
            print('Enter a valid option....')                        






