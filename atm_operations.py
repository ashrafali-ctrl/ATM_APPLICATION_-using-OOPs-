#ATM OPERATIONS
import pin_security
class ATMoperations:
    def __init__(self,account_id,database_operations):
        self.database_operations=database_operations
        self.account_id=account_id
        self.db_data()
    
    def db_data(self):
         self.data=self.database_operations.fetch_single_record('accounts','account_id',self.account_id)
         self.amount=self.data['balance']
    
    def deposit(self):
        if pin_security.checking_pin(self.account_id):
            print("-"*10,'DEPOSITE SECTION','-'*10)
            while True:
                    amount = input("Enter amount to deposit => ")
                    

                    if amount.isdigit():
                            amount = int(amount)

                            if amount >= 1:
                                self.amount = self.amount + amount
                                self.update_db()
                                print(f"--- Successfully deposited {amount}/- ---")
                                print(f"Available Balance: {self.amount}/-")
                                break
                            else:
                                print("!--- Amount must be greater than zero ---!")
                    else:
                            print("!- Invalid Amount -!")
            print("-"*36)
        else:
             return
        
    
    def withdraw(self):
        if pin_security.checking_pin(self.account_id):
            print("-"*10,'WITHDRAW SECTION','-'*10)
            while True:
                amount = input("Enter amount to withdraw => ")
                
                if amount.isdigit():
                        amount = int(amount)

                        if amount >= 1:
                            if amount <= self.amount:
                                self.amount = self.amount - amount
                                self.update_db()
                                print(f"--- Successfully withdrawn {amount}/- ---")
                                print(f"Available Balance: {self.amount}/-")
                                break
                            else:
                                print("!- INSUFFICIENT BALANCE -!")
                                break
                        else:
                            print("!- Amount must be greater than zero -!")
                else:
                        print("!- INVALID AMOUNT -!")
            print("-"*36)
        else:
             return

    def check_balance(self):
        if pin_security.checking_pin(self.account_id):
            self.db_data()
            print("\n------ ACCOUNT BALANCE ------")
            print(f"Customer ID        : {self.data['customer_id']}")
            print(f"Account ID        : {self.data['account_id']}")
            print(f"Available Balance : {self.data['balance']}/-")
            print("-----------------------------")
        else:
             return

    def update_db(self):
         self.database_operations.updating_record('accounts','balance',self.amount,'account_id',self.data['account_id'])