
import pg8000.dbapi
from getpass import getpass

password = getpass("Enter PostgreSQL password: ")

connection = pg8000.dbapi.connect(
    host="localhost",
    database="atm_database",
    user="postgres",
    password=password,
    port=5432
)

print("Successfully connected to PostgreSQL!")

connection.close()
