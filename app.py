import mysql.connector

def establish_db_connection():
    try:
        # Connecting python script with local sql database server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",               
            password="your_password",   # Remember to change this to your password
            database="school_db"       
        )
        return conn
    except mysql.connector.Error as error_msg:
        print("Database Connection Failed:", error_msg)
        return None

def insert_new_entry(student_name, roll_number, final_marks):
    conn = establish_db_connection()
    if conn:
        my_cursor = conn.cursor()
        sql_query = "INSERT INTO students (roll_no, name, marks) VALUES (%s, %s, %s)"
        data_values = (roll_number, student_name, final_marks)
        
        my_cursor.execute(sql_query, data_values)
        conn.commit()
        
        print("🚀 Successfully saved into the Database!")
        my_cursor.close()
        conn.close()

def display_student_list():
    conn = establish_db_connection()
    if conn:
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM students")
        all_rows = my_cursor.fetchall()
        
        print("\n--- PRINTING ALL REGISTERED STUDENTS ---")
        for row in all_rows:
            # Using your familiar CBSE style to display data cleanly
            # row[0] is Roll No, row[1] is Name, row[2] is Marks
            print("Roll Number:", row[0], "|| Name:", row[1], "|| Marks:", row[2])
            
        my_cursor.close()
        conn.close()

# The Main Menu loop
while True:
    print("\n-------------------------------------")
    print("   RANCHI STUDENT DATABASE SYSTEM   ")
    print("-------------------------------------")
    print("Press 1 -> Add a Student")
    print("Press 2 -> Display All Students")
    print("Press 3 -> Close Program")
    
    user_input = input("Enter option numbers: ")
    
    if user_input == '1':
        s_name = input("Enter Student Full Name: ")
        s_roll = int(input("Enter Roll No: "))
        s_marks = float(input("Enter Board Marks: "))
        insert_new_entry(s_name, s_roll, s_marks)
        
    elif user_input == '2':
        display_student_list()
        
    elif user_input == '3':
        print("Exiting system. Thank you!")
        break
        
    else:
        print("❌ Invalid input string! Please choose a number between 1 and 3.")
