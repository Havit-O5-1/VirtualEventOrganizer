from flask import Flask, render_template, request, redirect, flash
import sqlite3
import bcrypt

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Validate inputs
        if len(username) < 3:
            flash("Username must be at least 3 characters long.", 'error')
            return redirect('/register')
        if len(password) < 6:
            flash("Password must be at least 6 characters long.", 'error')
            return redirect('/register')
        if password != confirm_password:
            flash("Passwords do not match.", 'error')
            return redirect('/register')

        # Hash password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Store user in the database
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()
            flash("Registration successful!", 'success')
            return redirect('/register')
        except sqlite3.IntegrityError:
            flash("Username already exists. Please choose a different username.", 'error')
            return redirect('/register')

    return render_template('register.html')

@app.route('/')
def home():
    return '<h1>Welcome to the User Registration App</h1><a href="/register">Register Here</a>'

# Initialize the database
init_db()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
