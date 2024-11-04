import sqlite3 as sql
import os

db_name = "student_data.db"
if os.path.exists(db_name):
    os.remove(db_name)

with sql.connect(db_name) as conn:
    cur = conn.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS student_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            activity TEXT,
            homework_score INTEGER
        )"""
    )

    cur.execute(
        """INSERT INTO student_info(first_name, last_name, age, activity, homework_score)
           VALUES
               ('adil', 'bekmuratov', 16, 'chess', 10),
               ('dinara', 'nurgalieva', 16, 'shopping', 10),
               ('temirlan', 'zharasov', 18, 'coding', 10),
               ('bolotbek', 'jumaev', 19, 'sports', 10),
               ('samat', 'kozhaev', 16, 'music', 10),
               ('aidana', 'kadyrova', 17, 'painting', 10),
               ('nurbol', 'omurbekov', 15, 'gaming', 10),
               ('aigul', 'beketaeva', 18, 'dancing', 10),
               ('zhanna', 'kaipova', 16, 'cooking', 10),
               ('aidar', 'serikbayev', 17, 'traveling', 10)"""
    )

    cur.execute(
        """SELECT * FROM student_info WHERE LENGTH(last_name) = 10 AND homework_score = 10"""
    )
    long_name_students = cur.fetchall()

    for student in long_name_students:
        student_id = student[0]
        cur.execute(
            """UPDATE student_info SET first_name = 'genius' WHERE id = ?""",
            (student_id,),
        )

    for student in long_name_students:
        student_id = student[0]
        cur.execute("""SELECT * FROM student_info WHERE id = ?""", (student_id,))
        print(cur.fetchall())
