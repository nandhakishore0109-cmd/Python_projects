# ATM_PROJECT USING FUNCTIONS......

balance = 0
mini_statement = []

def credit():

    global balance

    amount = float(input('Enter a credit amount :'))

    if amount <= 0:
        print("Enter a crediting amount:")

    else:
        balance+= amount
        mini_statement.append(f'Credited : ${amount}')
        print(f"${amount} credited in your account")

def debit():

    global balance

    amount = float(input("Enter a debited amount:")) 

    if amount > balance:
        print("Insufficient balance")

    else:
        balance-= amount
        mini_statement.append(f"dedited : ${amount}")
        print(f"${amount} debited from your account")

def balance_check():
    print(f"Your cuurent balance is ${balance}") 

def ministatement():
    print("--------- ministatement--------")

    if len(mini_statement) == 0:
        print(f"No transactions")

    else:
        for i in mini_statement:
            print(i)

    print(f"Available balance  ${balance}")

def menu():
    while True:

        print("\n ATM MENU")
        print("1. credit")
        print("2. debit")
        print("3. balance")
        print("4. ministatement")
        print("5 Exit")

        choice = input("Choose a num (1-5):")

        if choice == '1':
            credit()
        elif choice == '2':
            debit()
        elif choice == '3':
           balance_check()
        elif choice == '4':
            ministatement()
        elif choice == '5':
            print("Thank you for using ATM. Welcome")
            break

        else:
            print("Invalid choice,pls check once")


menu()                              
menu()

                   