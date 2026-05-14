import os
from flask import Flask, render_template, redirect, url_for, request, flash
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# --- Routes ---

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authentication logic will go here
        # For now, just dummy redirect to dashboard
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/expenses')
def expenses():
    return render_template('expenses.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/vendors')
def vendors():
    return render_template('vendors.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')
if __name__ == '__main__':
    # Create database and tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
