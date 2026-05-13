from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    full_name = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False) # Admin, Accountant, Viewer

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    expenses = db.relationship('Expense', backref='category', lazy='dynamic')

class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True)
    vendor_name = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(20))
    gst_number = db.Column(db.String(20))
    address = db.Column(db.Text)
    expenses = db.relationship('Expense', backref='vendor', lazy='dynamic')

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'))
    payment_method = db.Column(db.String(50), nullable=False)
    expense_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    receipt = db.Column(db.String(256))
    notes = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
