import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  #  MySQL username
            password='your_password'  # MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # handles MySQL errors
        print(f"MySQL Error: {e}")

    finally:
        # Ensure resources are released properly
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
