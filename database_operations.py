#DATA BASE OPERATIONS
import os
import pg8000.dbapi
#from getpass import getpass
from dotenv import load_dotenv

#password = getpass("Enter PostgreSQL password: ")
load_dotenv()
connection = None
cursor = None

try:
    connection = pg8000.dbapi.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )
    cursor = connection.cursor()
except pg8000.dbapi.Error as error:
    print(f"Database connection failed, due to {error}")
except Exception as error:
    print(f"UNEXPECTED ERROR : {error}")

def connection_check():
    if connection is None or cursor is None:
        print("Database connection is not available.")
        return False
    return True
    
def validating_customer(account):
    if not connection_check():
        return
    data=None
    try:
        cursor.execute("""
                SELECT c.customer_id, a.account_id, c.phone_number
                FROM customers AS c
                JOIN accounts AS a
                ON c.customer_id = a.customer_id
                WHERE c.customer_id = %s;""", (account.customer_id,))
        data=cursor.fetchone()
    except Exception as error:
        print(f"UNEXPECTED ERROR : {error}")
    else:
        return data

def inserting_details_into_customers(account):
    if not connection_check():
        return

    try:
        cursor.execute("""
                INSERT INTO customers ( 
                customer_id,
                customer_name,
                father_name,
                date_of_birth,
                phone_number,
                address,
                created_at)
                values (%s,%s,%s,%s,%s,%s,%s);
            """, (account.customer_id,account.cname,account.fname,account.date_of_birth,
                account.phone_number,account.address,account.created_at))
        connection.commit()
    except pg8000.dbapi.Error as error:
        print(f"Database operations failed, due to {error}")
        if connection is not None:
            connection.rollback()
    except Exception as error:
        print(f"UNEXPECTED ERROR : {error}")
    else:
        print("Customers data inserted successfully!")

def inserting_into_accounts(account):
    if not connection_check():
           return

    try:
        cursor.execute("""
        INSERT INTO ACCOUNTS (
        account_id,
        customer_id,
        account_type,
        pin_hash,
        balance,
        account_status)
        values (%s,%s,%s,%s,%s,%s);
        """,(account.account_id,account.customer_id,account.account_type,
             account.coded_pin,account.amount,account.account_status))
        connection.commit()
    except pg8000.dbapi.Error as error:
        print(f"Database operations failed, due to {error}")
        if connection is not None:
                connection.rollback()
    except Exception as error:
        print(f"UNEXPECTED ERROR : {error}")
    else:
        print("Customers data inserted successfully!")
    
    
