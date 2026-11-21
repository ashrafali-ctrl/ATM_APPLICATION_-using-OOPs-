#account creation
import pin_security
from datetime import datetime
import random
class CreateAccount:
    def __init__(self,database_operations):
        self.database_operations=database_operations
        self.customer_info()
        
    def customer_info(self):
                self.cname=input("Enter your Name => ")
                self.fname=input("Enter your Father Name => ")
                self.DOB()
                self.mobile_num()
                self.address=input("Enter you Address => ")
                self.customer_id_generation()
        #        self.customer_id='C4824'
                self.account_number()
        #        self.account_id='6602261426'
        #        self.data=database_operations.validating_customer(self.customer_id)
                self.validate()
                print("=> Your account ID is ", self.account_id)
                self.coded_pin=pin_security.creating_pin()
                self.account_type='SAVINGS'
                self.intial_deposite()
                self.account_status='ACTIVE'
                self.time()
                self.account_info()
                input('=> PRESS ENTER TO STORE DATA INTO DATA-BASE : ')
    
    def account_number(self):
        account_number=random.randint(1000000000,9999999999)
        self.account_id=str(account_number)

    def validate_account_id(self):
        while True:
            self.data=self.database_operations.fetch_single_record('accounts','account_id',self.account_id)
            if self.data is not None:
                self.account_number()
            else:
                return
    
    def intial_deposite(self):
        while True:
            self.amount=input("Intial Deposite = ")
            if self.amount.isdigit():
                self.amount=int(self.amount)
                if self.amount >= 1:
                    print(f"--- You deposited {self.amount} /- in your account as Intial Deposite --- ")
                    break
                else:
                    print("!- AMOUNT MUST BE GREATER THAN ZERO -!")
            else:
                print("!- INVALID -!")


    def customer_id_generation(self):
        self.customer_id = "C" + str(random.randint(1, 9999)).zfill(4)

    def validating_customer_id(self):
        while True:
            self.data=self.database_operations.fetch_single_record('customers','customer_id',self.customer_id)
            if self.data is not None:
                self.customer_id_generation()
            else:
                return
    
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
            self.phone_number=self.phone_number.strip()
            if self.phone_number.isdigit() and len(self.phone_number) == 10 and self.phone_number[0] in "6789":
                self.data=self.database_operations.fetch_single_record('customers','phone_number',self.phone_number)
                if self.data is None:
                    break
                else:
                    print("!--- PHONE NUMBER ALREADY EXISTS ---!")
            else:
                print("!----- INVALID DATA ENTERED -----!")
    
    def time(self):
        self.created_at= datetime.now()

    def validate(self):
            self.validating_customer_id()
            self.validate_account_id()
    
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