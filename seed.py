from app import app
from models import db, Category, Expense, Vendor, User
from datetime import datetime

with app.app_context():
    # Check if category exists
    if Category.query.count() == 0:
        c1 = Category(name='Salary')
        c2 = Category(name='Electricity')
        c3 = Category(name='Internet')
        db.session.add_all([c1, c2, c3])
        db.session.commit()
        print("Added sample categories.")

    # Check if vendor exists
    if Vendor.query.count() == 0:
        v1 = Vendor(vendor_name='Modern Electronics', phone='9876543210')
        db.session.add(v1)
        db.session.commit()
        print("Added sample vendor.")

    # Check if user exists (needed for created_by)
    if User.query.count() == 0:
        u1 = User(username='admin', password_hash='pbkdf2:sha256:260000$...', full_name='Admin User', role='Admin')
        db.session.add(u1)
        db.session.commit()
        print("Added sample user.")

    # Check if expense exists
    if Expense.query.count() == 0:
        admin = User.query.first()
        cat = Category.query.first()
        v = Vendor.query.first()
        
        e1 = Expense(
            title='Office Internet Bill',
            amount=1500.00,
            category_id=cat.id,
            vendor_id=v.id,
            payment_method='UPI',
            expense_date=datetime.utcnow(),
            created_by=admin.id
        )
        db.session.add(e1)
        db.session.commit()
        print("Added sample expense.")

    print(f"Current Counts - Categories: {Category.query.count()}, Expenses: {Expense.query.count()}")
