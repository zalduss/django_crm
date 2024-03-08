
import mysql.connector

data_base = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="0mgfire!",   
)

cursor_object = data_base.cursor()

# Create a database
cursor_object.execute("CREATE DATABASE crm_db")
print("Database created successfully")