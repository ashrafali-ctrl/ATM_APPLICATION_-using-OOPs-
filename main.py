#main program file
from creating_account import CreateAccount
from customer import CustomerOperations
from account_security import AccountSecurity
import database_operations

#account=CreateAccount(database_operations)
#database_operations.inserting_details_into_customers(account)
#database_operations.inserting_into_accounts(account)
#security=AccountSecurity(account)
#operations=ATMoperations(database_operations)
#print('--- DEPOSITE ---')
#operations.deposit()
#print('--- WITHDRAW ---')
#operations.withdraw()
#print('--- CHECK BALANCE ---')
#operations.check_balance()
#print('--- change pin ---')
#security.change_pin()
#print('--- CHECK BALANCE ---')
#operations.check_balance()

while True:
    print("\n" + "*" * 35)
    print(" " * 12, "BANKNEXUS ATM")
    print("*" * 35)
    print("1. Create Account")
    print("2. Customer Operations")
    print("3. Exit")
    print("-" * 35)

    choice = input("Select an option (1-3) => ").strip().upper()

    if choice in ('1', 'CREATE ACCOUNT','CA'):
        account = CreateAccount(database_operations)
        database_operations.inserting_details_into_customers(account)
        database_operations.inserting_into_accounts(account)
    elif choice in ('2', 'CUSTOMER OPERATIONS', 'CO'):
        CustomerOperations(database_operations)
    elif choice in ('3', 'EXIT'):
        print("&----- Thank you for using BankNexus ATM -----&")
        if database_operations.connection is not None:
            database_operations.connection.close()
        break
    else:
        print("!----- INVALID CHOICE! Please enter 1, 2, or 3 -----!")
