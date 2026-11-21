import mysql.connector
mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1309",
      database="college_db"   
)
cursor = mydb.cursor()
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
         id = input("Enter student id: ")
         name = input("Enter student name: ")
         roll_no = input("Enter student roll_no: ")

         course = input("Enter student course: ")
         semester = input("Enter student semester: ")
         sql = "INSERT INTO students (id, name, roll_no, course, semester) VALUES (%s, %s, %s, %s, %s)"
         val = (id, name, roll_no, course, semester)
         cursor.execute(sql, val)
         mydb.commit()
         print(cursor.rowcount, "record inserted.")
        
    elif choice == '2':
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        for row in result:
            print(row)
            
    elif choice == '3':
        id = input("Enter  ID to update: ")
        name = input("Enter new name: ")
        roll_no = input("Enter new roll_no: ")
        course = input("Enter new course: ")
        semester = input("Enter new semester: ")
        sql = "UPDATE students SET name=%s, roll_no=%s, course=%s, semester=%s WHERE id=%s"
        val = (name, roll_no, course, semester, id)
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record(s) updated.")
        
    elif choice == '4':
        id = input("Enter student ID to delete: ")
        sql = "DELETE FROM students WHERE id=%s"
        val = (id)
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record(s) deleted.")
        
    elif choice == '5':
        break
        
    else:
        print("Invalid choice. Please try again.")

