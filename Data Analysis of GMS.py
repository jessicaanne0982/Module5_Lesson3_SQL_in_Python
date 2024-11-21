# Task 1 - SQL BETWEEN Usage
 
import mysql.connector
from mysql.connector import Error
 
def get_members_in_age_range(start_age, end_age):
  try:
    cursor = conn.cursor()
    start_age = start_age
    end_age = end_age
   
    #sql query to find all the members between 25 and 30-years-old
    query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"
    #execute the query
    cursor.execute(query, (start_age, end_age))
    #To print each member between the ages of 25 and 30
    for row in cursor.fetchall():
      print(row)
    cursor.close()
 
  except Error as e:
    print(f"Error: {e}")

db_name = "fitness_center_db"
user = "root"
password = "password" # generic password, actual password removed
host = "localhost"
 
try:
  conn = mysql.connector.connect(
    database = db_name,
    user = user,
    password = password,
    host = host
    )
  if conn is not None:
    print("Database successfully connected to")
    get_members_in_age_range(25, 30)
  
except Error as e:
  print(f"Error: {e}")
 
finally:
    if conn and conn.is_connected():
        conn.close() # close database connection when done
        print("MySQL connection is closed")