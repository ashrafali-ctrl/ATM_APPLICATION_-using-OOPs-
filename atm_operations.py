#ATM OPERATIONS
#from creating_account import CreateAccount
class ATMoperations:
    def __init__(self, account,security):
        self.account = account
        self.security=security
    
    def deposit(self):
        if self.security.verify_pin():
         print("-"*10,'DEPOSITE SECTION','-'*10)
         while True:
                amount = input("Enter amount to deposit => ")
                

                if amount.isdigit():
                        amount = int(amount)

                        if amount >= 1:
                            self.account.amount = int(self.account.amount) + amount
                            print(f"--- Successfully deposited {amount}/- ---")
                            print(f"Available Balance: {self.account.amount}/-")
                            break
                        else:
                            print("!--- Amount must be greater than zero ---!")
                else:
                        print("!- Invalid Amount -!")
         print("-"*36)
        
    
    def withdraw(self):
        if self.security.verify_pin():
            print("-"*10,'WITHDRAW SECTION','-'*10)
            while True:
                amount = input("Enter amount to withdraw => ")
                
                if amount.isdigit():
                        amount = int(amount)

                        if amount >= 1:
                            if amount <= int(self.account.amount):
                                self.account.amount = int(self.account.amount) - amount

                                print(f"--- Successfully withdrawn {amount}/- ---")
                                print(f"Available Balance: {self.account.amount}/-")
                                break
                            else:
                                print("!- INSUFFICIENT BALANCE -!")
                                break
                        else:
                            print("!- Amount must be greater than zero -!")
                else:
                        print("!- INVALID AMOUNT -!")
            print("-"*36)

    def check_balance(self):
       if self.security.verify_pin():
            print("\n------ ACCOUNT BALANCE ------")
            print(f"Account Holder : {self.account.cname}")
            print(f"Account ID     : {self.account.account_id}")
            print(f"Available Balance : {self.account.amount}/-")
            print("-----------------------------")
