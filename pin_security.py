from argon2 import PasswordHasher
from argon2.exceptions import VerificationError
import getpass
import database_operations

password_hasher = PasswordHasher()

def creating_pin():
        print("*" * 41)
        print(" " * 12, "PIN CREATION")
        print("*" * 41)
        while True:
            pin=getpass.getpass("=> Create Your PIN :  ")
            pin=pin.strip()
            if pin.isdigit() and len(pin) == 4:
                print("-"*41)
                d_pin=getpass.getpass("=> Confirm PIN again : ")
                if pin == d_pin.strip():
                    coded_pin=hash_pin(pin)
                    return coded_pin
                else:
                    print("---! PIN MIS-MATCHED !---")
            else:
                print("PIN MUST CONTAIN EXACTLY 4 DIGITS.")

def checking_pin(account_id):
    stored_hash=db_pin(account_id)
    attempts=3
     
    while attempts > 0:
        pin=getpass.getpass('=> Enter Your 4-Digit PIN : ')
        pin=pin.strip()
        
        if pin.isdigit() and len(pin) == 4:
            verification=verify_pin(pin,stored_hash)
            
            if not verification:
                print("!----- INCORRECT PIN -----!")
                attempts -= 1
                print(f"Remaining attempts: {attempts}")
            
            if verification:
                print(" +----- PIN VERIFIED SUCCESSFULLY -----+ ")
                return True 
        else:
             attempts -= 1
             print('!--- INVALID --- !')
             print(f"Remaining attempts: {attempts}")
    print("--- YOU HAVE REACHED MAXIMUM ATTEMPTS, SO TRY AGAIN LATER ---")
    return False

def changing_pin(account_id):
    stored_hash=db_pin(account_id)
    attempts=3

    while attempts > 0:
        pin=getpass.getpass('=> Enter Your 4-Digit PIN : ')
        pin=pin.strip()

        if pin.isdigit() and len(pin) == 4:
            verification=verify_pin(pin,stored_hash)

            if verification:
                coded_pin=creating_pin()
                print('&----- PIN CHANGED SUCCESSFULLY -----&')
                database_operations.updating_record('accounts','pin_hash',coded_pin,'account_id',account_id)
                return coded_pin
            else:
                attempts -= 1
                print("!----- INCORRECT PIN -----!")
                print(f"Remaining attempts: {attempts}")
        else:
            attempts -= 1
            print('!--- INVALID PIN ---!')
            print(f"Remaining attempts: {attempts}")
    print("--- YOU HAVE REACHED MAXIMUM ATTEMPTS, SO TRY AGAIN LATER ---")
    return None

def hash_pin(pin): #receives pin and generates a salted argon2 hash
            return password_hasher.hash(pin) #returns coded pin
            

def verify_pin(pin, stored_hash):
    try:
        return password_hasher.verify(stored_hash, pin)
    except VerificationError:
        return False

def db_pin(account_id):
     data=database_operations.fetch_single_record('accounts','account_id',account_id)
     pin=data['pin_hash']
     return pin