#main program file
from creating_account import CreateAccount
from atm_operations import ATMoperations
from account_security import AccountSecurity
account=CreateAccount()
security=AccountSecurity(account)
#operations=ATMoperations(account,security)
#print('--- DEPOSITE ---')
#operations.deposit()
#print('--- WITHDRAW ---')
#operations.withdraw()
#print('--- CHECK BALANCE ---')
#operations.check_balance()
#print('--- change pin ---')
security.change_pin()
print('--- CHECK BALANCE ---')
#operations.check_balance()