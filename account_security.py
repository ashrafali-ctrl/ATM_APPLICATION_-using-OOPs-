#maintaining account security proplerly
import getpass
class AccountSecurity:
    def __init__(self, account):
            self.account = account
    
    def verify_pin(self):
            attempts = 3
    
            while attempts > 0:
                pin = getpass.getpass("Enter your ATM PIN: ")
    
                if pin == self.account.pin:
                    print("--- PIN VERIFIED SUCCESSFULLY ---")
                    return True
                else:
                    attempts -= 1
                    print(f"!--- INCORRECT PIN ---!")
                    print(f"Remaining attempts: {attempts}")
    
            print("--- YOU HAVE REACHED MAXIMUM ATTEMPTS, SO TRY AGAIN LATER ---")
            return False

    def change_pin(self):
         if self.verify_pin():
              self.account.creating_pin()
              
        