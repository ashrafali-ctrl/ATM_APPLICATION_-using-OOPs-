from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

password_hasher = PasswordHasher()

def hash_pin(pin): #receives pin and generates a salted argon2 hash
    while True:
        print("-"*41)
        if  pin.isdigit() and len(pin) ==4:
            return password_hasher.hash(pin) #returns coded pin
        else:
            print('PIN must contain exactly 4 digits.')
            

def verify_pin(pin, stored_hash):
    try:
        return password_hasher.verify(stored_hash, pin)
    except VerificationError:
        return False