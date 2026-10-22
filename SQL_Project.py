import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="210918104033",
        database="code99_project"
    )

    if mydb.is_connected():
        print("MySQL connection is active!")

    mydb.close()

except mysql.connector.Error as err:
    print("Connection failed:", err)