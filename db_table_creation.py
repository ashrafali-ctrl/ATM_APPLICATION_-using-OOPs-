import pg8000.dbapi
from getpass import getpass

password = getpass("Enter PostgreSQL password: ")

connection = None
cursor = None

try:
    connection = pg8000.dbapi.connect(
        host="localhost",
        database="banknexus",
        user="postgres",
        password=password,
        port=5432
    )
    cursor = connection.cursor()
    cursor.execute("""
        
    CREATE TABLE IF NOT EXISTS accounts (
        account_id VARCHAR(10) PRIMARY KEY,
        customer_id VARCHAR(5) NOT NULL,
        account_type VARCHAR(7) NOT NULL,
        pin_hash VARCHAR(255) NOT NULL,
        balance NUMERIC(15) NOT NULL,
        account_status VARCHAR(10) NOT NULL DEFAULT 'ACTIVE',

        CONSTRAINT fk_customer
            FOREIGN KEY (customer_id)
            REFERENCES customers(customer_id),

        CONSTRAINT chk_account_type
            CHECK (account_type IN ('SAVINGS', 'CURRENT')),

        CONSTRAINT chk_account_status
            CHECK (account_status IN ('ACTIVE', 'FROZEN', 'CLOSED'))
    );
    """)
    connection.commit()

except pg8000.dbapi.Error as error:
    print(f"Database operation failed, due to {error}")
    if connection is not None:
        connection.rollback()
except Exception as error:
    print(f"UNEXPECTED ERROR : {error}")

else:
    print("table created successfully!")

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
