import sqlite3
import os

db_file = "person.db"

if os.path.exists(db_file):
    os.remove(db_file)


def setup_database():
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """
    )

    department_list = [(101, "HR"), (102, "IT"), (103, "Sales")]
    cursor.executemany(
        "INSERT INTO departments (id, name) VALUES (?, ?)", department_list
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first TEXT NOT NULL,
            last TEXT NOT NULL,
            dept_id INTEGER NOT NULL,
            FOREIGN KEY (dept_id) REFERENCES departments(id)
        )
    """
    )

    employees = [
        ("kamila", "azybekova", 101),
        ("marat", "arzymatov", 101),
        ("bayaman", "azybekov", 102),
        ("marjan", "aypova", 102),
        ("ayisha", "azybekova", 103),
        ("aibike", "jumabekova", 103),
    ]
    cursor.executemany(
        "INSERT INTO employees (first, last, dept_id) VALUES (?, ?, ?)", employees
    )

    connection.commit()
    connection.close()


def show_employees():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")

    for employee in cursor.fetchall():
        print(employee)

    conn.close()


if __name__ == "__main__":
    setup_database()
    show_employees()
