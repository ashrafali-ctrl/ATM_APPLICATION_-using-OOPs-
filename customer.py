#customer
from atm_operations import ATMoperations
import pin_security
class CustomerOperations:
    def __init__(self,database_operations):
        self.database_operations=database_operations
        self.account_id=input("Enter your Account ID : ")
        self.record_from_db()
        self.status=self.checking_status()
        if not self.status:
            return
        self.atmOperations=ATMoperations(self.account_id,self.database_operations)
        self.Atm_operations()
        
    def record_from_db(self):
        self.data=self.database_operations.fetch_single_record('accounts','account_id',self.account_id)   

    def checking_status(self):
        if self.data is None:
            print("!----- ACCOUNT NOT FOUND -----!")
            return False
        if self.data["account_status"] in ("FROZEN", "CLOSED"):
            print(f"!----- WE'RE SORRY, YOUR ACCOUNT IS {self.data['account_status']} -----!")
            return False
        return True


    def Atm_operations(self):
        while True:
            print("\n" + "*" * 35)
            print(" " * 9, "ATM OPERATIONS")
            print("*" * 35)
            print("1 =>  Deposit")
            print("2 => Withdraw")
            print("3 => Check Balance")
            print('4 => Change PIN')
            print("5 => Exit")
            print("-" * 35)
            
            choice = input("Select an operation => ".title()).strip().upper()

            if choice in ('5', 'EXIT'):
                print("&----- Thank you for using BankNexus ATM -----&")
                break

            if choice not in ('1', 'DEPOSITE', '2', 'WITHDRAW', '3', 'CHECK BALANCE', '4', 'CHANGE PIN','D','W','CB','CP'):
                print("!- INVALID CHOICE! Please enter 1, 2, 3, 4, 5 or the operation name -!")
                continue
            if choice in ('1', 'DEPOSITE', 'D'):
                self.atmOperations.deposit()
                return
            elif choice in ('2', 'WITHDRAW', 'W'):
                self.atmOperations.withdraw()
                return
            elif choice in ('3', 'CHECK BALANCE', 'CB'):
                self.atmOperations.check_balance()
                return
            elif choice in ('4', 'CHANGE PIN', 'CP'):
                pin_security.changing_pin(self.data['account_id'])
        