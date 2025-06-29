import mysql.connector 
from mysql.connector import errorcode 
try:
    print ("Connecting to MySQL...")
    connection = mysql.connector.connect(
          host="localhost",
          user="root",
          password="ginnytanui2005!",
    ) 
    cursor = connection.cursor() 
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    print("Failed to connect or create database.")
    print("Error:", err)

finally:
    # Close everything properly
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔒 Connection closed.")