# 1. Gym Database Management with Python and SQL

import mysql.connector
from mysql.connector import Error

# Task 1: Add a member function
def add_member(id, name, age):
    try:
        cursor = conn.cursor()
        new_member = (id, name, age)
        new_id = (id, )

        #check to see if the member to add is already a member
        query_check = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(query_check, new_id)
        current_member = cursor.fetchall()
        print(current_member)
  
        if current_member:
            print("This member already exists in the database")
        else:
            # sql query to add member
            query = "INSERT INTO Members(id, name, age) VALUES (%s, %s, %s)"

            #execute the query
            cursor.execute(query, new_member)

            conn.commit()
            print("New member has successfully been added to the database")
            cursor.close()
    except Error as e:
        print(f"Error: {e}")

# Task 2: Add a workout function
def add_workout_session(session_id, member_id, session_date, duration_minutes, calories_burned):
    try:
        cursor = conn.cursor()
    
        new_workout = (session_id, member_id, session_date, duration_minutes, calories_burned)
        member_check = (member_id, )
    
        #check to see the member exists in the database
        query_check = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(query_check, member_check)
        current_member = cursor.fetchall()
    
        if not current_member:
            print("Invalid Member ID or Member ID not found in database")
        else:
            # sql query to add a new workout
            query = """INSERT INTO WorkoutSessions(session_id, member_id, session_date, duration_minutes, calories_burned) 
                VALUES (%s, %s, %s, %s, %s)"""
        
            #execute the query
            cursor.execute(query, new_workout)
            conn.commit()
            print("A new workout has successfully been added to the database")
            cursor.close()
    except Error as e:
        print(f"Error: {e}")
 
# Task 3: Update a member's age function
def update_member_age(id, new_age):
    try:
        cursor = conn.cursor()
 
        update_age = (new_age, id)
        member_check = (id, )
        
        #check to see if the member is already a member
        query_check = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(query_check, member_check)
        current_member = cursor.fetchall()
        
        if not current_member:
            print("Invalid Member ID or Member ID not found in database")
        else:
            # sql query to update member's age
            query = "UPDATE Members SET age = %s WHERE id = %s"
        
            #execute the query
            cursor.execute(query, update_age)
            conn.commit() 
            print("Member's age has successfully been updated in the database")
            cursor.close()
    except Error as e:
        print(f"Error: {e}")
 
# Task 4: Delete a workout function
def delete_workout_session(session_id):
    try:
        cursor = conn.cursor()
 
        workout_to_remove = (session_id, )
        
        #check to see the workout exists in the database
        query_check = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(query_check, workout_to_remove)
        valid_workout = cursor.fetchall()
 
        if not valid_workout:
            print("Invalid Workout ID or workout session not found in database")
        else:
            # sql query to add a new workout
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        
            #execute the query
            cursor.execute(query, workout_to_remove)
            conn.commit()
            print("Workout has successfully been deleted from the database")
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

    if conn.is_connected():
        print("Connected to MySQL database successfully")

        add_member(9, "John Smith", 25)
        add_workout_session(7, 6, "2024-11-21", 45, 182)
        update_member_age(8, 43)
        delete_workout_session(3)


except Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        conn.close() # Close the database connection
        print("MySQL connection is closed")













