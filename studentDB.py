import mysql.connector
import json
import matplotlib.pyplot as plt
from os import system

#Connecting to the database:
conn = mysql.connector.connect(user = 'root',
                                host = 'localhost',
                                database = 'studentDatabase',
                                password = "Pass!word"
                            )

cur = conn.cursor(buffered=True)


#Defining functions for the database:
def addStudent():
    admNum = int(input("Admission Number: "))
    name = input("Name: ")
    ofClass = int(input("Class: "))
    section = input("Section: ")
    rollNum = int(input("Roll Number: "))
    fCore = input("5th core (Math, IP, PE, Fine Arts, Psychology): ")
    cur.execute(f"insert into studentinformation(admNum, ename, class, section, rollNum, fcore) values({admNum}, '{name}', {ofClass}, '{section}', {rollNum}, '{fCore}')")
    conn.commit()
    print("Student added successfully.")
#End of addStudent function


def editStudent():
    #Editing the values in a student's row
    admNum = int(input("Admission Number: "))
    cur.execute(f"select * from studentinformation where admNum={admNum}")
    results = cur.fetchall()
    if len(results) == 0:
        print("Student not found")
    else:
        toEdit = input(f"What do you want to edit in given profile? (Name, Class, Section, Roll Number, 5th Core): ").lower()

        if toEdit == 'name':
            nameChange = input("What do you want to change the name to? ")
            cur.execute(f"update studentinformation set ename='{nameChange}' where admNum={admNum}")
            conn.commit()
            print("Name changed successfully.")

        elif toEdit == 'class':
            classChange = int(input("What do you want to change the class to? "))
            cur.execute(f"update studentinformation set class={classChange} where admNum={admNum}")
            conn.commit()
            print("Class changed successfully.")

        elif toEdit == 'section':
            sectionChange = input("What do you want to change the section to? ")
            cur.execute(f"update studentinformation set section='{sectionChange}' where admNum={admNum}")
            conn.commit()
            print("Section changed successfully.")

        elif toEdit == 'roll number':
            rollChange = int(input("What do you want to change the roll number to? "))
            cur.execute(f"update studentinformation set rollNum={rollChange} where admNum={admNum}")
            conn.commit()
            print("Roll Number changed successfully.")

        elif toEdit == 'fifth core' or toEdit == '5th core':
            fCoreChange = int(input("What do you want to change the fifth core to? "))
            cur.execute(f"update studentinformation set fcore={fCoreChange} where admNum={admNum}")
            conn.commit()
            print("5th core changed successfully.")
#End of editStudent function


def delStudent():
    #Deleting a student from the database
    admNum = int(input("Admission Number: "))
    cur.execute(f"select * from studentinformation where admNum={admNum}")
    results = cur.fetchall()

    if len(results) == 0:
        print("Student not found")
        
    else:
        areYouSure = input("Are you sure you want to delete this profile? This change is irreversible. Please type 'Yes' if you want to delete: ").lower()
        if areYouSure == "yes":
            cur.execute(f"delete from studentinformation where admNum={admNum}")
            conn.commit()
            print("Profile deleted successfully.")
        else:
            print("Deletion interrupted. Please restart the program if you want to delete.")
#End of delStudent function


def addEntry():
    #Adds the marks in a student's record
    admNum = int(input("Admission Number: "))
    cur.execute(f"select * from studentinformation where admNum={admNum}")
    results = cur.fetchall()

    if len(results) == 0:
        print("Student not found")
        
    else:
        if results[0][3] == 'A1':
            su1 = 'English'
            su2 = 'Mathematics'
            su3 = 'Physics'
            su4 = 'Chemistry'
            su5 = results[0][14]

        elif results[0][3] == 'A2':
            su1 = 'English'
            su2 = 'Biology'
            su3 = 'Physics'
            su4 = 'Chemistry'
            su5 = results[0][14]

        elif results[0][3] == 'B' or results[0][3] == 'B1':
            su1 = 'English'
            su2 = 'Accounts'
            su3 = 'Business Studies'
            su4 = 'Economics'
            su5 = results[0][14]

        elif results[0][3] == 'C' or results[0][3] == 'C1':
            su1 = 'English'
            su2 = 'History'
            su3 = 'Political Science'
            su4 = 'Economics'
            su5 = results[0][14]
        while True:
            try:
                s1 = int(input(f"Marks in {su1}: "))
                if s1 < 0 or s1 > 80:
                    raise ValueError
                s2 = int(input(f"Marks in {su2}: "))
                if s2 < 0 or s2 > 80:
                    raise ValueError
                s3 = int(input(f"Marks in {su3}: "))
                if s3 < 0 or s3 > 80:
                    raise ValueError
                s4 = int(input(f"Marks in {su4}: "))
                if s4 < 0 or s4 > 80:
                    raise ValueError
                s5 = int(input(f"Marks in {su5}: "))
                if s5 < 0 or s5 > 80:
                    raise ValueError
                break

            except ValueError:
                print("Given marks are invalid, please provide marks between 0-80.")

        total = s1 + s2 + s3 + s4 + s5
        average = total/5

        if average >= 70:
            grade = 'A+'
            remarks = 'Excellent performance!'

        elif average >= 60:
            grade = 'A'
            remarks = 'Great performance!'

        elif average >= 50:
            grade = 'B'
            remarks = 'Good performance, can do better!'

        elif average >= 40:
            grade = 'C'
            remarks = 'Needs improvement.'

        elif average < 40:
            grade = 'F'
            remarks = 'Needs extra classes for considerable improvement.'

        cur.execute(f"update studentinformation set sub1='{s1}' where admNum={admNum}")
        cur.execute(f"update studentinformation set sub2='{s2}' where admNum={admNum}")
        cur.execute(f"update studentinformation set sub3='{s3}' where admNum={admNum}")
        cur.execute(f"update studentinformation set sub4='{s4}' where admNum={admNum}")
        cur.execute(f"update studentinformation set sub5='{s5}' where admNum={admNum}")
        cur.execute(f"update studentinformation set total='{total}' where admNum={admNum}")
        cur.execute(f"update studentinformation set average='{average}' where admNum={admNum}")
        cur.execute(f"update studentinformation set grade='{grade}' where admNum={admNum}")
        cur.execute(f"update studentinformation set remarks='{remarks}' where admNum={admNum}")
        conn.commit()
        print("Added record successfully.")
#End of addEntry function


def editEntry():
    admNum = int(input("Admission Number: "))
    cur.execute(f"select * from studentinformation where admNum={admNum}")
    results = cur.fetchall()

    if len(results) == 0:
        print("Student not found")
        
    else:
        if results[0][3] == 'A1':
            su1 = 'English'
            su2 = 'Mathematics'
            su3 = 'Physics'
            su4 = 'Chemistry'
            su5 = results[0][14]

        elif results[0][3] == 'A2':
            su1 = 'English'
            su2 = 'Biology'
            su3 = 'Physics'
            su4 = 'Chemistry'
            su5 = results[0][14]

        elif results[0][3] == 'B' or results[0][3] == 'B1':
            su1 = 'English'
            su2 = 'Accounts'
            su3 = 'Business Studies'
            su4 = 'Economics'
            su5 = results[0][14]

        elif results[0][3] == 'C' or results[0][3] == 'C1':
            su1 = 'English'
            su2 = 'History'
            su3 = 'Political Science'
            su4 = 'Economics'
            su5 = results[0][14]
        while True:
            try:
                s1 = int(input(f"Marks in {su1}: "))
                if s1 < 0 or s1 > 80:
                    raise ValueError
                s2 = int(input(f"Marks in {su2}: "))
                if s2 < 0 or s2 > 80:
                    raise ValueError
                s3 = int(input(f"Marks in {su3}: "))
                if s3 < 0 or s3 > 80:
                    raise ValueError
                s4 = int(input(f"Marks in {su4}: "))
                if s4 < 0 or s4 > 80:
                    raise ValueError
                s5 = int(input(f"Marks in {su5}: "))
                if s5 < 0 or s5 > 80:
                    raise ValueError
                break

            except ValueError:
                print("Given marks are invalid, please provide marks between 0-80.")

        total = s1 + s2 + s3 + s4 + s5
        average = total/5

        if average >= 70:
            grade = 'A+'
            remarks = 'Excellent performance!'

        elif average >= 60:
            grade = 'A'
            remarks = 'Great performance!'

        elif average >= 50:
            grade = 'B'
            remarks = 'Good performance, can do better!'

        elif average >= 40:
            grade = 'C'
            remarks = 'Needs improvement.'

        elif average < 40:
            grade = 'F'
            remarks = 'Needs extra classes for considerable improvement.'

        cur.execute(f"update studentinformation set sub1='{s1}' where admNum={admNum}")
        cur.execute(f"update studentinformation set sub2='{s2}' where admNum={admNum}")
        cur.execute(f"update studentinformation set sub3='{s3}' where admNum={admNum}")
        cur.execute(f"update studentinformation set sub4='{s4}' where admNum={admNum}")
        cur.execute(f"update studentinformation set sub5='{s5}' where admNum={admNum}")
        cur.execute(f"update studentinformation set total='{total}' where admNum={admNum}")
        cur.execute(f"update studentinformation set average='{average}' where admNum={admNum}")
        cur.execute(f"update studentinformation set grade='{grade}' where admNum={admNum}")
        cur.execute(f"update studentinformation set remarks='{remarks}' where admNum={admNum}")
        conn.commit()
        print("Edited record successfully.")
#End of editEntry function


def delEntry():
    admNum = int(input("Admission Number: "))
    cur.execute(f"select * from studentinformation where admNum={admNum}")
    results = cur.fetchall()

    if len(results) == 0:
        print("Student not found")
        
    else:
        areYouSure = input("Are you sure you want to delete the records from this student? Type 'Yes' if you are sure: ").lower()
        if areYouSure == 'yes':
            cur.execute(f"update studentinformation set sub1=NULL where admNum={admNum}")
            cur.execute(f"update studentinformation set sub2=NULL where admNum={admNum}")
            cur.execute(f"update studentinformation set sub3=NULL where admNum={admNum}")
            cur.execute(f"update studentinformation set sub4=NULL where admNum={admNum}")
            cur.execute(f"update studentinformation set sub5=NULL where admNum={admNum}")
            cur.execute(f"update studentinformation set total=NULL where admNum={admNum}")
            cur.execute(f"update studentinformation set average=NULL where admNum={admNum}")
            cur.execute(f"update studentinformation set grade=NULL where admNum={admNum}")
            cur.execute(f"update studentinformation set remarks=NULL where admNum={admNum}")
            conn.commit()
            print("Successfully deleted the records.")
        else:
            print("Could not delete the records.")
#End of delEntry function


def showReport():
    #Shows the report card of a given student
    admNum = int(input("Admission Number: "))
    system('cls')
    cur.execute(f"select * from studentinformation where admNum={admNum}")
    results = cur.fetchall()

    if len(results) == 0:
        print("Student not found")
        
    else:

        print(f"Report card for {results[0][1]}\n")
        print(f"Admission Number: {admNum}")
        print(f"Class: {results[0][2]}")
        print(f"Section: {results[0][3]}")
        print(f"Roll Number: {results[0][4]}")

        if results[0][3] == 'A1':
            su1 = 'English'
            su2 = 'Mathematics'
            su3 = 'Physics'
            su4 = 'Chemistry'
            su5 = results[0][14]

        elif results[0][3] == 'A2':
            su1 = 'English'
            su2 = 'Biology'
            su3 = 'Physics'
            su4 = 'Chemistry'
            su5 = results[0][14]

        elif results[0][3] == 'B' or results[0][3] == 'B1':
            su1 = 'English'
            su2 = 'Accounts'
            su3 = 'Business Studies'
            su4 = 'Economics'
            su5 = results[0][14]

        elif results[0][3] == 'C' or results[0][3] == 'C1':
            su1 = 'English'
            su2 = 'History'
            su3 = 'Political Science'
            su4 = 'Economics'
            su5 = results[0][14]

        print("Marks obtained in:")
        print(f"- {su1}: {results[0][5]}")
        print(f"- {su2}: {results[0][6]}")
        print(f"- {su3}: {results[0][7]}")
        print(f"- {su4}: {results[0][8]}")
        print(f"- {su5}: {results[0][9]}")

        print(f"Total: {results[0][10]}")
        print(f"Average: {results[0][11]}")
        print(f"Grade: {results[0][12]}")
        print(f"Remarks: {results[0][13]}")
#End of showReport function


def graph():
    admNum = int(input("Admission Number: "))
    system('cls')
    cur.execute(f"select * from studentinformation where admNum={admNum}")
    results = cur.fetchall()

    if len(results) == 0:
        print("Student not found")
        
    else:

        if results[0][3] == 'A1':
            su1 = 'English'
            su2 = 'Mathematics'
            su3 = 'Physics'
            su4 = 'Chemistry'
            su5 = results[0][14]

        elif results[0][3] == 'A2':
            su1 = 'English'
            su2 = 'Biology'
            su3 = 'Physics'
            su4 = 'Chemistry'
            su5 = results[0][14]

        elif results[0][3] == 'B' or results[0][3] == 'B1':
            su1 = 'English'
            su2 = 'Accounts'
            su3 = 'Business Studies'
            su4 = 'Economics'
            su5 = results[0][14]

        elif results[0][3] == 'C' or results[0][3] == 'C1':
            su1 = 'English'
            su2 = 'History'
            su3 = 'Political Science'
            su4 = 'Economics'
            su5 = results[0][14]

        subjectList = [su1, su2, su3, su4, su5]
        marksList = [results[0][5], results[0][6], results[0][7], results[0][8], results[0][9]]

        plt.bar(subjectList, marksList, color=(0.2, 0.4, 0.6, 0.6))
        plt.xlabel('Subjects')
        plt.ylabel('Marks')
        plt.title("Marks Analysis on a graph")
        plt.show()
#End of graph function

#Printing choices for user to pick from
print("Database system for Indus Universal")
print("Press 1 to add student to database")
print("Press 2 to edit student in the database")
print("Press 3 to delete a student from the database")
print("Press 4 to add student's marks to database")
print("Press 5 to edit student's marks from database")
print("Press 6 to delete student's marks from database")
print("Press 7 to show student's report card")
print("Press 8 to show graph based on student's score")

choice = int(input("Please enter your choice: "))

#Calling functions based on choices
if choice == 1:
    addStudent()

elif choice == 2:
    editStudent()

elif choice == 3:
    delStudent()

elif choice == 4:
    addEntry()

elif choice == 5:
    editEntry()

elif choice == 6:
    delEntry()

elif choice == 7:
    showReport()

elif choice == 8:
    graph()
