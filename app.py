import os
from flask import Flask, render_template, redirect, url_for, request, flash, send_file, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from config import Config
from models import db, User, Expense, Category, Vendor, Setting
import pandas as pd
import io
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# --- Flask Login Setup ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- HTML Routes ---

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        username = data.get('username')
        password = data.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            if not user.is_active:
                return jsonify({'success': False, 'message': 'Account is disabled.'}), 403
            login_user(user)
            return jsonify({'success': True}) if request.is_json else redirect(url_for('dashboard'))
        return jsonify({'success': False, 'message': 'Invalid credentials'}) if request.is_json else render_template('login.html', error="Invalid username or password")
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

import json

def get_categories_json():
    cats = Category.query.all()
    return json.dumps([{'id': c.id, 'name': c.name} for c in cats])

def get_vendors_json():
    vens = Vendor.query.filter_by(is_active=True).all()
    return json.dumps([{'id': v.id, 'name': v.vendor_name, 'phone': v.phone, 'gst': v.gst_number} for v in vens])

def get_expenses_json():
    exps = Expense.query.order_by(Expense.expense_date.desc()).all()
    return json.dumps([{
        'id': e.id,
        'title': e.title,
        'amount': float(e.amount),
        'categoryId': e.category_id,
        'vendorId': e.vendor_id,
        'method': e.payment_method,
        'date': e.expense_date.strftime('%Y-%m-%d')
    } for e in exps])

def get_settings_json():
    settings = Setting.query.all()
    return json.dumps({s.key_name: s.value for s in settings})

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', expenses_json=get_expenses_json(), categories_json=get_categories_json(), vendors_json=get_vendors_json(), settings_json=get_settings_json())

@app.route('/expenses')
@login_required
def expenses():
    return render_template('expenses.html', expenses_json=get_expenses_json(), categories_json=get_categories_json(), vendors_json=get_vendors_json())

@app.route('/categories')
@login_required
def categories():
    return render_template('categories.html', categories_json=get_categories_json())

@app.route('/vendors')
@login_required
def vendors():
    return render_template('vendors.html', vendors_json=get_vendors_json())

@app.route('/reports')
@login_required
def reports():
    return render_template('reports.html', expenses_json=get_expenses_json(), categories_json=get_categories_json(), vendors_json=get_vendors_json())

@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html', settings_json=get_settings_json())

# --- API Routes ---

@app.route('/api/categories', methods=['GET', 'POST'])
@login_required
def api_categories():
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        if Category.query.filter_by(name=name).first():
            return jsonify({'success': False, 'message': 'Category already exists.'}), 400
        new_cat = Category(name=name)
        db.session.add(new_cat)
        db.session.commit()
        return jsonify({'success': True, 'id': new_cat.id, 'name': new_cat.name})
    
    cats = Category.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in cats])

@app.route('/api/categories/<int:id>', methods=['DELETE'])
@login_required
def api_delete_category(id):
    cat = Category.query.get_or_404(id)
    if cat.expenses.count() > 0:
        return jsonify({'success': False, 'message': 'Cannot delete category with associated expenses.'}), 400
    db.session.delete(cat)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/api/vendors', methods=['GET', 'POST'])
@login_required
def api_vendors():
    if request.method == 'POST':
        data = request.json
        new_ven = Vendor(
            vendor_name=data.get('name'),
            phone=data.get('phone', ''),
            gst_number=data.get('gst', '')
        )
        db.session.add(new_ven)
        db.session.commit()
        return jsonify({'success': True, 'id': new_ven.id, 'name': new_ven.vendor_name})
    
    vens = Vendor.query.filter_by(is_active=True).all()
    return jsonify([{'id': v.id, 'name': v.vendor_name, 'phone': v.phone, 'gst': v.gst_number} for v in vens])

@app.route('/api/vendors/<int:id>', methods=['DELETE'])
@login_required
def api_delete_vendor(id):
    ven = Vendor.query.get_or_404(id)
    ven.is_active = False # Soft delete
    db.session.commit()
    return jsonify({'success': True})

@app.route('/api/expenses', methods=['GET', 'POST'])
@login_required
def api_expenses():
    if request.method == 'POST':
        data = request.json
        try:
            new_exp = Expense(
                title=data.get('title'),
                amount=float(data.get('amount')),
                category_id=int(data.get('categoryId')),
                vendor_id=int(data.get('vendorId')) if data.get('vendorId') else None,
                payment_method=data.get('method'),
                expense_date=datetime.strptime(data.get('date'), '%Y-%m-%d').date() if data.get('date') else datetime.utcnow().date(),
                created_by=current_user.id
            )
            db.session.add(new_exp)
            db.session.commit()
            return jsonify({'success': True, 'id': new_exp.id})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

    exps = Expense.query.order_by(Expense.expense_date.desc()).all()
    return jsonify([{
        'id': e.id,
        'title': e.title,
        'amount': float(e.amount),
        'categoryId': e.category_id,
        'vendorId': e.vendor_id,
        'method': e.payment_method,
        'date': e.expense_date.strftime('%Y-%m-%d')
    } for e in exps])

@app.route('/api/expenses/<int:id>', methods=['DELETE'])
@login_required
def api_delete_expense(id):
    exp = Expense.query.get_or_404(id)
    db.session.delete(exp)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/api/settings', methods=['GET', 'POST'])
@login_required
def api_settings():
    if request.method == 'POST':
        data = request.json
        for k, v in data.items():
            setting = Setting.query.filter_by(key_name=k).first()
            if not setting:
                setting = Setting(key_name=k)
                db.session.add(setting)
            setting.value = v
        db.session.commit()
        return jsonify({'success': True})
        
    settings = Setting.query.all()
    return jsonify({s.key_name: s.value for s in settings})

@app.route('/api/user/account', methods=['POST'])
@login_required
def api_account():
    from werkzeug.security import generate_password_hash
    data = request.json
    cur = data.get('current')
    nw = data.get('new')
    new_username = data.get('username')
    
    if not check_password_hash(current_user.password_hash, cur):
        return jsonify({'success': False, 'message': 'Current password incorrect'})
        
    if new_username and new_username != current_user.username:
        existing = User.query.filter_by(username=new_username).first()
        if existing:
            return jsonify({'success': False, 'message': 'Username already taken'})
        current_user.username = new_username
        
    if nw:
        current_user.password_hash = generate_password_hash(nw)
        
    db.session.commit()
    return jsonify({'success': True})

@app.route('/reports/export/excel')
@login_required
def export_excel():
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

    df = pd.DataFrame(expenses, columns=[
        'ID', 'Title', 'Amount', 'Category', 'Vendor', 'Payment Method', 'Date', 'Notes'
    ])
    df['Amount'] = pd.to_numeric(df['Amount'])

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
    with app.app_context():
        db.create_all()
    app.run(debug=True)
