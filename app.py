from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database table
def init_db():
    conn = sqlite3.connect('workouts.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise TEXT,
            sets INTEGER,
            reps INTEGER,
            weight INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    conn = sqlite3.connect('workouts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM workouts")
    data = c.fetchall()
    conn.close()
    return render_template('index.html', workouts=data)

@app.route('/add', methods=['POST'])
def add():
    exercise = request.form['exercise']
    sets = request.form['sets']
    reps = request.form['reps']
    weight = request.form['weight']

    conn = sqlite3.connect('workouts.db')
    c = conn.cursor()
    c.execute("INSERT INTO workouts (exercise, sets, reps, weight) VALUES (?, ?, ?, ?)",
              (exercise, sets, reps, weight))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)