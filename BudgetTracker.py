# I started with this greet_user function so that it will be creating a 
# personalized experience for the user(s)
# I included the  datetime library because I think the project will involve some kind of time manipulation

from datetime import datetime, timedelta

Transactions=[]

def greet_user():
    print("welcome to your BudgetTracker\n")
    name=input("please enter your name: ")
    print("Hello"+" "+name+" "+"let's get started with your budget tracking!\n")
    return name

#I added in a menu section that would allow users to have options to choose from
def menu():
    print("choose one of the options below")
    print("1. add transactions")
    print("2. list transactions")
    print("3. summarize budget")
    print("4. view transaction history")
    print("5. exit")
    
# I created the validate_date function so that only valid date inputs can be used for the date of transaction.
# Otherwise, it loops and prompts the user to put in the correct date. It is also limited between 
# 2024-2028 and above cause those match the current years we are in.

def validate_date():
    while True:
        date=input("Enter the date of the transaction (dd/mm/yyyy): \n")
        try:
            date_object = datetime.strptime(date, "%d/%m/%Y")
            if date_object.year < 2024:
                print("Year cannot be below 2024! Please enter a valid year \n")
                continue
            if date_object.year > 2028:
                print("Year cannot be beyond 2028! Please enter a valid year \n")
                continue
            return date_object
        except ValueError:
            print("Please enter a valid date and year \n")

#I defined the add_transactions function so that it can give the user options to add in their transaction
def add_transactions():
    t_date= validate_date()
    amount=input("enter amount of transaction: ")
    transaction_type=input("enter type of transaction: ")
    description=input("enter description of transaction: ")
    transaction = {
        "date": t_date,
        "amount": amount,
        "description": description,
        "transaction_type": transaction_type
    }
    Transactions.append(transaction)
    print("transaction added successfully\n")

def list_transactions():
    if not Transactions:
        print("No transactions recorded yet.\n")
        return
    for y, x in enumerate(Transactions, start=1):
        print(f"transaction 1: {x['date']} | {x['amount']} | {x['transaction_type']} | {x['description']}\n")

greet_user()

while True:
    menu()
    choice=int(input("enter your choice: "))
    if choice==1:
        add_transactions()
    elif choice==2:
        list_transactions()
    else:
        print("You entered a wrong choice")







