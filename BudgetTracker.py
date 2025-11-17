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
    print("4. filter transactions")
    print("5. exit")
# I created the validate_date function so that only valid date inputs can be used for the date of transaction.
# Otherwise, it loops and prompts the user to put in the correct date. It is also limited to the current year
# we are in which is 2025

def validate_date():
    while True:
        date=input("Enter the date of the transaction (dd/mm/yyyy): \n")
        try:
            date= datetime.strptime(date, "%d/%m/%Y").date()
            if date.year < 2025:
                print("Year cannot be below 2025! Please enter a valid year \n")
                continue
            if date.year > 2025:
                print("Year cannot be beyond 2025! Please enter a valid year \n")
                continue
            return date
        except ValueError:
            print("Please enter a valid date and year \n")

#I defined the add_transactions function so that it can give the user options to add in their transaction
def add_transactions():
    t_date= validate_date()
    while True:
        try:
            amount = (input("enter amount of transaction: "))
            if int(amount) < 0:
                print("Invalid amount!! Please input a positive amount \n")
                continue
            break
        except ValueError:
            print("please enter a valid amount \n")
    transaction_type=input("enter type of transaction(income/expense): ")
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
    try:
        if choice==1:
            add_transactions()
        elif choice==2:
            list_transactions()
        else:
            print("please enter a valid choice\n")
    except ValueError:
        print("please enter a valid choice\n")






