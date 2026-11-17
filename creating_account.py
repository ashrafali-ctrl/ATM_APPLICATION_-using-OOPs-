#account creation
import pin_security
from datetime import datetime
import random
import getpass
class CreateAccount:
    def __init__(self):
        self.cname=input("Enter your Name => ")
        self.fname=input("Enter your Father Name => ")
        self.DOB()
        self.mobile_num()
        self.address=input("Enter you Address => ")
        self.customer_id_generation()
        self.creating_pin()
        self.account_number()
        print("=> Your account ID is ", self.account_id)
        self.account_type='SAVINGS'
        self.intial_deposite()
        self.account_status='ACTIVE'
        self.time()
        self.account_info()
        
        
    
    
    def creating_pin(self):
        print("*" * 41)
        print(" " * 12, "PIN CREATION")
        print("*" * 41)
        pin=getpass.getpass("=> Enter Your PIN :  ")
        self.coded_pin=pin_security.hash_pin(pin)
        
        
        
    
    def account_number(self):
        account_number=random.randint(1000000000,9999999999)
        self.account_id=str(account_number)
    
    def intial_deposite(self):
        while True:
            self.amount=int(input("Intial Deposite = "))
            if str(self.amount).isdigit():
                if self.amount >= 1:
                    print(f"--- You deposited {self.amount} /- in your account as Intial Deposite --- ")
                    break
                else:
                    print("!- AMOUNT MUST BE GREATER THAN ZERO -!")
            else:
                print("!- INVALID -!")


    def customer_id_generation(self):
        self.customer_id = "C" + str(random.randint(1, 9999)).zfill(4)
    
    def DOB(self):
        while True:
            try:
                date_of_birth=input("Enter your date of birth (DD-MM-YYYY): ")
                self.date_of_birth=datetime.strptime(date_of_birth, "%d-%m-%Y").date()
            except ValueError:
                print("!--- INVALID DATE FORMATE ENTERED ---!")
            else:
                print("Your Date of Birth : ",self.date_of_birth)
                break

    def mobile_num(self):
        while True:
            self.phone_number=input("Enter your phone number : ")
            if self.phone_number.isdigit() and len(self.phone_number) == 10 and self.phone_number[0] in "6789":
                break
            else:
                print("!----- INVALID DATA ENTERED -----!")
    
    def time(self):
        self.created_at= datetime.now()
    
    def account_info(self):
         print('*'*41)
         print('-'*10, 'ACCOUNT INFORMATION', '-'*10)
         print(f" -> Account Holder ID   : {self.customer_id}")
         print(f" -> Account Holder Name : {self.cname}")
         print(f" -> Father's Name       : {self.fname}")
         print(f" -> Date of Birth       : {self.date_of_birth}")
         print(f" -> Your Phone Number   : {self.phone_number}")
         print(f" -> Your Address        : {self.address}")
         print(f" -> Account ID          : {self.account_id}")
         print(f" -> Account Type        : {self.account_type}")
         print(f" -> Account Balance     : {self.amount}")
         print(f" -> Account Status      : {self.account_status}")
         print(f" -> Account created at  : {self.created_at}")
         print('*'*41)