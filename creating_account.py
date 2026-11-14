#account creation
import random
import getpass
class CreateAccount:
    def __init__(self):
        self.cname=input("Enter your name => ")
        self.creating_pin()
        self.account_number()
        print("=> Your account ID is ", self.account_id)
        self.intial_deposite()
        self.account_info()
    
    
    def creating_pin(self):
        print("*" * 41)
        print(" " * 12, "PIN CREATION")
        print("*" * 41)

        while True:
            
            print("-" * 41)

            pin = getpass.getpass("Enter your PIN => ")

            if pin.isdigit() and len(pin) == 4:
                print("-" * 41)

                confirm_pin = getpass.getpass("Confirm your PIN => ")

                if pin == confirm_pin:
                    self.pin = pin

                    print("\n" + "*" * 41)
                    print("| PIN STATUS : Successfully Created |")
                    print("*" * 41)
                    break

                else:
                    print("\n!--- PIN DOES NOT MATCH. TRY AGAIN ---!")

            else:
                print("\n!--- PIN MUST CONTAIN FOUR DIGITS ---!")

    
    def account_number(self):
        account_number=random.randint(1000000000,9999999999)
        self.account_id=str(account_number)
    
    def intial_deposite(self):
        while True:
            self.amount=input("Intial Deposite = ").upper()
            if self.amount.isdigit():
                if int(self.amount) >= 1:
                    print(f"--- You deposited {self.amount} /- in your account as Intial Deposite --- ")
                    break
                else:
                    print("!- AMOUNT MUST BE GREATER THAN ZERO -!")
            else:
                print("!- INVALID -!")

    def account_info(self):
         print('*'*41)
         print('-'*10, 'ACCOUNT INFORMATION', '-'*10)
         print(f" -> Account Holder Name : {self.cname}")
         print(f" -> Account ID          : {self.account_id}")
         print(f" -> Account PIN         : {self.pin}")
         print(f" -> Account Balance     : {self.amount}")
         print('*'*41)

