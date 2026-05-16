from app import app
from models import db, Category, Expense, Vendor, User, Setting
from datetime import datetime
from werkzeug.security import generate_password_hash

with app.app_context():
    # 1. Seed Categories
    if Category.query.count() == 0:
        default_categories = [
            'Salary', 'Electricity', 'Internet', 'Furniture', 'Stationery', 
            'Maintenance', 'Event Expense', 'Marketing', 'Miscellaneous'
        ]
        for c_name in default_categories:
            db.session.add(Category(name=c_name))
        db.session.commit()
        print("Added default categories.")

    # 2. Seed Default Admin User
    if User.query.count() == 0:
        hashed_pw = generate_password_hash('admin123')
        admin = User(username='admin', password_hash=hashed_pw, full_name='System Admin', role='Admin')
        db.session.add(admin)
        db.session.commit()
        print("Added default admin user (admin/admin123).")

    # 3. Seed Default School Settings
    if Setting.query.count() == 0:
        s1 = Setting(key_name='school_name', value='Wisdom The Global World School')
        s2 = Setting(key_name='school_phone', value='+91 9876543210')
        s3 = Setting(key_name='school_address', value='123 Education Lane, Knowledge City')
        db.session.add_all([s1, s2, s3])
        db.session.commit()
        print("Added default school settings.")

    print(f"Current DB Status - Users: {User.query.count()}, Categories: {Category.query.count()}, Settings: {Setting.query.count()}")
