from flask import Flask, render_template, flash, render_template, request, url_for, redirect
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_db_connection():
    conn = sql.connect('database.db')
    conn.row_factory = sql.Row
    return conn

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/abb')
def abb():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('abb.html', posts=posts)

@app.route('/stud')
def stud():
    return render_template('stud.html')

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/classes')
def classes():
    return render_template('classes.html')

@app.route('/educ')
def educ():
    return render_template('educ.html')

@app.route('/science')
def science():
    return render_template('science.html')

@app.route('/global')
def global_1():
    return render_template('global.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

if __name__ == "__main__":
    app.run(debug=True)
