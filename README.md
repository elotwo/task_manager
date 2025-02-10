#TASK MANAGEMENT APPLICATION:

A simple and intuitive Task Management Application built with Flask (Python) for the backend, SQLite for the database, and HTML/CSS/JavaScript for the frontend. Manage your tasks efficiently with features like adding, updating, deleting, filtering, and sorting tasks.

#FEATURES:

1) Add Tasks: Add tasks with a title, description, due date, due time, priority, and category.

2) Update Tasks: Update the status of tasks (Pending, In Progress, Completed).

3) Delete Tasks: Remove tasks you no longer need.

4) Filter Tasks: Filter tasks by status, priority, or category.

5) Sort Tasks: Sort tasks by due date, priority, or category.

6) Responsive Design: Clean and modern user interface.


#TECHNOLOGIES USED

Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

Database: SQLite

Styling: Custom CSS

#FOLDER STRUCTURE: 

/task_manager
|
|--- /templates
|    |
|    |-- index.html          # Frontend HTML template
|--- /static
|    |
|    |-- style.css           # Custom CSS for styling
|--- app.py                  # Flask backend application
|
|--- README.md               # Project documentation

#DATABASE SCHEMA:

The application uses an SQLite database (tasks.db) with the following schema:

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'Pending',
    due_date TEXT,
    due_time TEXT,
    priority TEXT DEFAULT 'Medium',
    category TEXT DEFAULT 'General'
);

