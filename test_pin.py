from pin_security import hash_pin, verify_pin
pin=input("enter your pin : ")
stored_hash=hash_pin(pin)
print("PIN hashed successfully!")
print(stored_hash)
entered_pin = input("Enter PIN again: ")

#if verify_pin(entered_pin, stored_hash):
#    print("PIN verified successfully!")
#else:
#    print("Incorrect PIN!")