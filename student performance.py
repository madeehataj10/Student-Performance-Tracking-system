import sqlite3
#This imports the sqlite3 library, which is used to interact with SQLite databases in Python.
#Database Connection Setup
conn = sqlite3.connect("student_performance.db")
cursor = conn.cursor()
sqlite3.connect("student_performance.db")# creates a connection to a SQLite database named student_performance.db. If the file doesn't exist, it will be created automatically.

conn.cursor()# creates a cursor object, which allows us to execute SQL queries on the database.
#Creating the students Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
math INTEGER,
science INTEGER,
english INTEGER,
total INTEGER,
average REAL,
grade TEXT
)
''')
conn.commit()


conn.commit() #commits the changes to the database.
# Defining the Student Class
class Student:
def __init__(self, name, math, science, english):
self.name = name
self.math = math
self.science = science
self.english = english
self.total = math + science + english
self.average = self.total / 3
self.grade = self.calculate_grade()

def calculate_grade(self):
if self.average >= 90:
return 'A'
elif self.average >= 80:
return 'B'
elif self.average >= 70:
return 'C'
elif self.average >= 60:
return 'D'
else:
return 'F'

#This method calculates the student's grade based on their average score:

A for average ≥ 90

B for average ≥ 80

C for average ≥ 70

D for average ≥ 60

F for average < 60
#6. Saving Student Data to the Database
def save_to_db(self):
cursor.execute('''
INSERT INTO students (name, math, science, english, total, average, grade)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', (self.name, self.math, self.science, self.english, self.total, self.average, self.grade))
conn.commit()

def display_students():
cursor.execute("SELECT * FROM students")
records = cursor.fetchall()
print("\nStudent Performance Records:")
print("ID | Name | Math | Science | English | Total | Average | Grade")
print("-" * 70)
for row in records:
print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]:.2f} | {row[7]}")

def delete_student(student_id):
cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
conn.commit()
print(f"Student with ID {student_id} deleted successfully!")

#This function deletes a student record from the database by their id.

The SQL query DELETE FROM students WHERE id = ? is used, where ? is replaced by the student_id provided.

conn.commit() #ensures the deletion is saved in the database.
#Updating a Student Record
def update_student(student_id, math, science, english):
total = math + science + english
average = total / 3
grade = Student("", math, science, english).calculate_grade()
cursor.execute('''
UPDATE students SET math=?, science=?, english=?, total=?, average=?, grade=? WHERE id=?
''', (math, science, english, total, average, grade, student_id))
conn.commit()
print(f"Student with ID {student_id} updated successfully!")


conn.commit() saves the updates in the database.
Main Loop Breakdown
def main():
while True:
print("\nStudent Performance Tracking System")
print("1. Add Student")
print("2. View Students")
print("3. Update Student")
print("4. Delete Student")
print("5. Exit")
choice = input("Enter your choice: ")

while True: #This starts an infinite loop, meaning the program will keep asking the user for input until they decide to exit. The loop will continue until the user explicitly selects the exit option (option 5).

print("\nStudent Performance Tracking System"): This prints the main heading of the program each time the loop runs, ensuring that it appears clearly at the top of the user interface.

Options
print("1. Add Student")
print("2. View Students")
print("3. Update Student")
print("4. Delete Student")
print("5. Exit")

choice = input("Enter your choice: "): This prompts the user to input their choice. The input is captured as a string and stored in the choice variable. This input is what drives the next steps in the program.
Conditionals Based on User Choice
if choice == '1':
name = input("Enter student name: ")
math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))
student = Student(name, math, science, english)
student.save_to_db()
print("Student record added successfully!")

if choice == '1':: This checks if the user has selected option 1 (Add Student).

After saving, a confirmation message is printed to let the user know the student has been added successfully.
elif choice == '2':
display_students()

elif choice == '2':: This checks if the user has selected option 2 (View Students).

The display_students()# function is called, which fetches all student records from the database and prints them in a formatted way.
elif choice == '3':
student_id = int(input("Enter Student ID to update: "))
math = int(input("Enter new Math marks: "))
science = int(input("Enter new Science marks: "))
english = int(input("Enter new English marks: "))
update_student(student_id, math, science, english)

elif choice == '3':: #This checks if the user has selected option 3 (Update Student)
elif choice == '5':
print("Exiting Program...")
break
else:
print("Invalid choice! Try again.")