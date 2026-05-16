# Wisdom Expense Tracker — Project Summary

**Client:** Wisdom The Global World School  
**Type:** Internal Web Application  
**Stack:** Python (Flask) + SQLite + HTML/Bootstrap + JavaScript (localStorage)  
**Repo:** https://github.com/Prince4061/expanse-tracker  
**Last Updated:** 15 May 2026

---

## 📌 Project Ka Maqsad

Wisdom The Global World School ke liye ek **internal expense management system** banaya ja raha hai jo school ke daily, monthly aur yearly kharche ko digitally track kare. Pehle yeh sab manually register mein hota tha — ab sab kuch ek web application mein manage hoga.

---

## 🏗️ Project Architecture

```
expanse-tracker/
├── app.py              # Flask backend — routes & Excel export
├── config.py           # App configuration (DB path, secret key)
├── models.py           # SQLAlchemy database models
├── requirements.txt    # Python dependencies
├── seed.py             # Development seed data script
├── prd.md              # Product Requirements Document
├── plan.md             # Development plan
├── instance/
│   └── expense_tracker.db   # SQLite database
├── static/
│   ├── css/style.css   # Custom dark theme styling
│   └── js/app.js       # Client-side logic (localStorage)
└── templates/
    ├── login.html
    ├── dashboard.html
    ├── expenses.html
    ├── categories.html
    ├── vendors.html
    ├── reports.html
    └── settings.html
```

---

## 🗄️ Database Models (`models.py`)

| Model | Fields | Purpose |
|-------|--------|---------|
| **User** | id, username, password_hash, full_name, role | Login & access control |
| **Category** | id, name | Expense categories (Salary, Electricity, etc.) |
| **Vendor** | id, vendor_name, phone, gst_number, address | Vendor/supplier records |
| **Expense** | id, title, amount, category_id, vendor_id, payment_method, expense_date, receipt, notes, created_by | Core expense records |

---

## 🧭 Flask Routes (`app.py`)

| Route | Method | Function |
|-------|--------|----------|
| `/` | GET | → Login redirect |
| `/login` | GET, POST | Login page |
| `/dashboard` | GET | Dashboard |
| `/expenses` | GET | Expense list |
| `/categories` | GET | Categories |
| `/vendors` | GET | Vendors |
| `/reports` | GET | Reports page |
| `/settings` | GET | Settings |
| `/reports/export/excel` | GET | Excel export (backend route) |

---

## 📄 Pages & Features

### 🔐 Login Page
- Username + Password authentication
- Users localStorage se validate hote hain
- Galat credentials par Hindi error message: *"Username ya password galat hai."*
- Default credentials: `admin` / `admin123`

### 📊 Dashboard
- **4 Summary Cards:** Total Expenses, This Month, Today, Total Vendors
- **Monthly Trend Chart** (Line) — real expense data se dynamically generate
- **Category-wise Chart** (Doughnut) — actual category breakdown

### 💰 Expenses Page
- Expenses table with: Date, Title, Category, Vendor, Amount, Payment Method
- **Add Expense Modal** — Title, Amount, Category, Vendor, Date, Payment Method
- **Delete Expense** functionality
- Data localStorage mein save hota hai
- Payment Methods: Cash, Bank Transfer, Card, UPI

### 🏷️ Categories Page
- Default categories: Salary, Electricity, Internet, Furniture, Stationery, Maintenance, Event Expense, Marketing, Miscellaneous
- **Add / Edit / Delete** category
- localStorage mein persist hoti hain

### 🏪 Vendors Page
- Vendor Name, Phone Number, GST Number columns
- **Add Vendor** — Name, Phone (optional), GST (optional)
- **Delete Vendor**

### 📈 Reports Page
- **Monthly Summary** — month-wise total + count
- **Yearly Summary** — year-wise total + count
- **Export Excel** ✅ — localStorage data se CSV generate karke download karta hai
  - Columns: ID, Title, Amount, Category, Vendor, Payment Method, Date, Notes
  - UTF-8 BOM se Excel mein Hindi characters sahi dikhte hain
- Export PDF — coming soon

### ⚙️ Settings Page
- **School Information** — School Name, Phone, Address (localStorage mein save)
- **Currency** — ₹ INR (fixed, Indian school ke liye)
- **Date Format** — DD-MM-YYYY (fixed, Indian standard)
- **Password Change** — Current + New + Confirm password validate karke update
- **Danger Zone** — Sabha data delete (Hindi warning + logout redirect)

---

## 🛠️ Tech Stack Details

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask |
| Database (server) | SQLite + SQLAlchemy |
| Data Storage (client) | Browser localStorage |
| Frontend | HTML5, Bootstrap 5.3, Font Awesome 6.4 |
| Charts | Chart.js |
| Excel Export | Client-side CSV (JavaScript) |
| Styling | Custom CSS — Dark theme |
| Authentication | localStorage-based (client-side) |

> **Note:** Abhi data localStorage mein store ho raha hai (browser-side). Flask backend aur SQLite DB ready hain lekin abhi full integration pending hai.

---

## ✅ Completed Features

- [x] Login / Logout system
- [x] Dashboard with real charts
- [x] Expense Add / Delete
- [x] Category CRUD (Add / Edit / Delete)
- [x] Vendor Add / Delete
- [x] Reports — Monthly & Yearly summary
- [x] **Export to Excel (CSV)** — fully working
- [x] Settings — School info save, Password change, Data wipe
- [x] Indian localization — ₹ INR, DD-MM-YYYY, Hindi messages
- [x] Dark theme UI

---

## 🔄 Pending / Future Work

- [ ] Backend authentication (Flask-Login + password hashing)
- [ ] Full SQLite integration (expenses ko DB mein save karna)
- [ ] Receipt upload feature
- [ ] Export to PDF
- [ ] Role-based access (Admin / Accountant / Viewer)
- [ ] Search & filter on expenses table
- [ ] Pagination
- [ ] Vendor expense history
- [ ] Monthly/Yearly report with filters

---

## 🔑 Default Login

```
Username: admin
Password: admin123
```

Settings page se password change kiya ja sakta hai.

---

## 📦 Git Commits History

| Commit | Description |
|--------|-------------|
| Initial | Project setup — Flask app, models, config |
| Frontend pages | Login, Dashboard, Expenses, Categories, Vendors, Reports, Settings templates |
| Flask routing | Routes connected to templates |
| `csv export fixed` | Excel export feature implement kiya (localStorage se CSV download) |
| `unneseary chije hata di` | USD/EUR removed, MM/DD/YYYY removed, fake chart data replaced with real data, Hindi messages added |

---

*Prepared by: Antigravity AI | Wisdom The Global World School — Internal Use Only*
