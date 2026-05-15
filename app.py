import os
from flask import Flask, render_template, redirect, url_for, request, flash, send_file
from config import Config
from models import db, User, Expense, Category, Vendor
import pandas as pd
import io

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

@app.route('/reports/export/excel')
def export_excel():
    # Query all expenses and join with Category and Vendor
    expenses = db.session.query(
        Expense.id,
        Expense.title,
        Expense.amount,
        Category.name.label('category'),
        Vendor.vendor_name.label('vendor'),
        Expense.payment_method,
        Expense.expense_date,
        Expense.notes
    ).join(Category, Expense.category_id == Category.id)\
     .outerjoin(Vendor, Expense.vendor_id == Vendor.id).all()

    if not expenses:
        flash("No expenses found to export.", "warning")
        return redirect(url_for('reports'))

    # Convert to DataFrame
    df = pd.DataFrame(expenses, columns=[
        'ID', 'Title', 'Amount', 'Category', 'Vendor', 'Payment Method', 'Date', 'Notes'
    ])

    # Create Excel file in memory
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Expenses')
    
    output.seek(0)

    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name='expenses_report.xlsx'
    )
if __name__ == '__main__':
    # Create database and tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
