# Practice DATABASE  
# 1) Create Database
# 2) Create 2-3 tables
# 3) Insert some records
# 4) Perform diffrent select operations
# 5) Update some data
# 6) Delete some data
import sqlite3
import os
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create the database file path
db_path = os.path.join(script_dir, 'student.db')
# Connect to the SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect(db_path)
# Create a cursor object to execute SQL commands
cursor = conn.cursor()
# Create a table named 'students' with columns id, name, age, and city
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    age INTEGER,
    city TEXT
)
''')

# Create two more tables: 'courses' and 'enrollments'
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    credits INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    grade TEXT,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
)
''')

# Insert initial records only if tables are empty (helps avoid duplicates on multiple runs)
cursor.execute('SELECT COUNT(*) FROM students')
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        'INSERT INTO students (name, age, city) VALUES (?, ?, ?)',
        [
            ('Alice', 20, 'New York'),
            ('Bob', 22, 'Los Angeles'),
            ('Charlie', 19, 'Chicago')
        ]
    )

cursor.execute('SELECT COUNT(*) FROM courses')
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        'INSERT INTO courses (code, name, credits) VALUES (?, ?, ?)',
        [
            ('CS101', 'Intro to CS', 4),
            ('MATH201', 'Calculus I', 3),
            ('ENG150', 'English Lit', 2)
        ]
    )

# Commit after initial inserts
conn.commit()

# Create sample enrollments if none exist
cursor.execute('SELECT COUNT(*) FROM enrollments')
if cursor.fetchone()[0] == 0:
    # Map names/codes to ids
    cursor.execute("SELECT id, name FROM students")
    students = {name: sid for (sid, name) in cursor.fetchall()}
    cursor.execute("SELECT id, code FROM courses")
    courses = {code: cid for (cid, code) in cursor.fetchall()}

    enroll_data = [
        (students['Alice'], courses['CS101'], 'A'),
        (students['Alice'], courses['MATH201'], 'B+'),
        (students['Charlie'], courses['ENG150'], 'A-')
    ]
    cursor.executemany(
        'INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)',
        enroll_data
    )
    conn.commit()

# Perform different select operations and joins
print('Students:')
cursor.execute('SELECT * FROM students')
for row in cursor.fetchall():
    print(row)

print('\nCourses:')
cursor.execute('SELECT * FROM courses')
for row in cursor.fetchall():
    print(row)

print('\nEnrollments:')
cursor.execute('SELECT * FROM enrollments')
for row in cursor.fetchall():
    print(row)

print('\nEnrollments (joined view):')
cursor.execute('''
SELECT s.name AS student, c.code AS course_code, c.name AS course_name, e.grade
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id
''')
for row in cursor.fetchall():
    print(row)

# Update some data
print('\nUpdating data...')
cursor.execute("UPDATE students SET city = 'San Francisco' WHERE name = 'Alice'")
cursor.execute("UPDATE courses SET credits = 5 WHERE code = 'CS101'")
cursor.execute("UPDATE enrollments SET grade = 'A+' WHERE grade = 'A' AND student_id = (SELECT id FROM students WHERE name = 'Alice')")
conn.commit()

print('After updates:')
cursor.execute('SELECT * FROM students')
for row in cursor.fetchall():
    print(row)
cursor.execute('SELECT * FROM courses')
for row in cursor.fetchall():
    print(row)
cursor.execute('SELECT * FROM enrollments')
for row in cursor.fetchall():
    print(row)

# Delete some data
print('\nDeleting some data...')
cursor.execute("DELETE FROM students WHERE name = 'Bob'")
cursor.execute("DELETE FROM enrollments WHERE student_id = (SELECT id FROM students WHERE name = 'Charlie') AND course_id = (SELECT id FROM courses WHERE code = 'ENG150')")
conn.commit()

print('After deletes:')
cursor.execute('SELECT * FROM students')
for row in cursor.fetchall():
    print(row)
cursor.execute('SELECT * FROM enrollments')
for row in cursor.fetchall():
    print(row)

# Close the database connection
conn.close()