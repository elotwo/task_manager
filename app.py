from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'tasks.db'

# Initialize the database
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'Pending',
                due_date TEXT,
                due_time TEXT,
                priority TEXT DEFAULT 'Medium',
                category TEXT DEFAULT 'General'
            )
        ''')
        conn.commit()

# Homepage - List all tasks
@app.route('/')
def index():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

# Add a new task
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = request.form.get('due_date')
    due_time = request.form.get('due_time')
    priority = request.form.get('priority')
    category = request.form.get('category')
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (title, description, due_date, due_time, priority, category)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, description, due_date, due_time, priority, category))
        conn.commit()
    return redirect(url_for('index'))

# Update task status
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    new_status = request.form.get('status')
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (new_status, task_id))
        conn.commit()
    return redirect(url_for('index'))

# Delete a task
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
    return redirect(url_for('index'))

# Filter tasks
@app.route('/filter', methods=['POST'])
def filter_tasks():
    status = request.form.get('status')
    priority = request.form.get('priority')
    category = request.form.get('category')
    query = 'SELECT * FROM tasks WHERE 1=1'
    params = []
    if status:
        query += ' AND status = ?'
        params.append(status)
    if priority:
        query += ' AND priority = ?'
        params.append(priority)
    if category:
        query += ' AND category = ?'
        params.append(category)
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

# Sort tasks
@app.route('/sort', methods=['POST'])
def sort_tasks():
    sort_by = request.form.get('sort_by')
    query = f'SELECT * FROM tasks ORDER BY {sort_by}'
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
