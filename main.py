#main program file
from creating_account import CreateAccount
from atm_operations import ATMoperations
from account_security import AccountSecurity
import database_operations
account=CreateAccount()
database_operations.inserting_details_into_customers(account)
database_operations.inserting_into_accounts(account)
database_operations.connection.close()
#security=AccountSecurity(account)
#operations=ATMoperations(account,security)
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

