
# I imported the datetime library because the project will involve time manipulation

from datetime import datetime, timedelta

#class definition
class BudgetTracker:
# initializing the transaction list to be accessed by other self-functions
    def __init__(self):
        self.Transactions=[]
    def greet_user(self):
        print("Welcome to BudgetTracker!\n")
        print("welcome to your BudgetTracker\n")
        name = input("please enter your name: \n").upper()
        print("Hello" + " " + name + " " + "let's get started with your budget tracking!\n")
        return name
# I added in a menu section that would allow users to have options to choose from
    def menu(self):
        print("choose one of the options below")
        print("1. add transactions")
        print("2. list transactions")
        print("3. summarize budget")
        print("4. filter transactions")
        print("5. exit")
# I created the validate_date function so that only valid date inputs can be used for the date of transaction.
# Otherwise, it loops and prompts the user to put in the correct date. It is also limited to the current year
# we are in which is 2025
    def validate_date(self):
        while True:
            date=input("Enter the date of the transaction (dd/mm/yyyy): \n")
            try:
                date = datetime.strptime(date, "%d/%m/%Y").date()
                if date.year < 2025:
                    print("Year cannot be below 2025! Please enter a valid year \n")
                    continue
                if date.year > 2025:
                    print("Year cannot be beyond 2025! Please enter a valid year \n")
                    continue
                return date
            except ValueError:
                print("Please enter a valid date and year \n")

# I defined the add_transactions function so that it can give the user options to add in their transaction
    def add_transactions(self):
        t_date = self.validate_date()
        # I used the while true loop to make sure the user would always be prompted to write a valid amount if they put in a negative number
        # Currencies are also not supported. The try is to handle invalid inputs gracefully instead of python crashing
        while True:
            try:
                amount = (input("enter amount of transaction: "))
                if int(amount) < 0:
                    print("Invalid amount!! Please input a positive amount \n")
                    continue
                break
            except ValueError:
                print("please enter a valid amount \n")
        transaction_type = input("enter type of transaction(income/expense): ")
        description = input("enter description of transaction: ")
        transaction = {
            "date": t_date,
            "amount": amount,
            "description": description,
            "transaction_type": transaction_type
        }
        self.Transactions.append(transaction)
        print("transaction added successfully\n")
# this is the list transaction function which access the Transaction list at the beginning and the user is able
# to see all the transactions they recorded in order through using enumerate.
    def list_transactions(self):
        if not self.Transactions:
            print("No transactions recorded yet.\n")
            return
        for y, x in enumerate(self.Transactions, start=1):
            print(f"transaction {y}: {x['date']} | {x['amount']} | {x['transaction_type']} | {x['description']}\n")

    def filter_transactions(self):
        print("choose one of the filter options below: ")
        print("1. filter by date")
        print("2. filter by transaction type")
        print("3. filter by description")
        print("4. filter by amount")
        option=int(input("enter your choice: "))
        if option==1:
            while True:
                month_input = input("enter month of transaction you want to filter(yyyy-mm): ")
                results = []
                for x in self.Transactions:
                    date = x['date'].strftime("%Y-%m")
                try:
                    if date==month_input:
                        results.append(x)
                    if not results:
                        print("please enter a valid month")
                        recorded_months=sorted({x['date'].strftime("%Y-%m") for x in self.Transactions})
                        print("these are the recorded months to filter:" ," ," .join(recorded_months),"\n")
                        continue
                    return results
                except ValueError:
                    print("please enter a valid month")
        elif option==2:
            while True:
                transaction_type_input = input("enter transaction type(income/expense): ").lower()
                if transaction_type_input=="income" not in ["income", "expense"]:
                    print("please enter a valid transaction type")
                    continue
                results=[]
                for x in self.Transactions:
                    if x['transaction_type'].lower()==transaction_type_input:
                        results.append(x)
                    if not results:
                        print("please enter a valid transaction type")
                    else:
                        return results

# this is the function that runs the whole program and the while true loop helps make sure the user is always given
# the menu option after completing a process

Main_program=BudgetTracker()

while True:
    Main_program.menu()
    choice=int(input("enter your choice: "))
    try:
        if choice==1:
            Main_program.add_transactions()
        elif choice==2:
            Main_program.list_transactions()
        elif choice==4:
            Main_program.filter_transactions()
        else:
            print("please enter a valid choice\n")
    except ValueError:
        print("please enter a valid choice\n")






