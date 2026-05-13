# Wisdom The Global World School

# Final Expense Tracker Application Plan

---

# 1. Project Overview

यह एक web-based **School Expense Tracker Application** होगी जिसमें स्कूल अपने सभी expenses को manage कर सकेगा।

Application का मुख्य उद्देश्य:

- Daily expenses track करना
- Financial records maintain करना
- Reports generate करना
- Expense history रखना
- Accounting process आसान बनाना

---

# 2. Main Objectives

## System Goals

✅ Fast & Simple

✅ Low Maintenance

✅ Easy UI

✅ Fast Delivery

✅ Accurate Reports

✅ Secure Authentication

✅ Easy Backup

---

# 3. Recommended Technology Stack

| Layer | Technology |
| --- | --- |
| Backend | Python + Flask |
| Database | SQLite |
| ORM | SQLAlchemy |
| Frontend | HTML + Bootstrap 5 |
| JavaScript | Vanilla JS |
| Charts | Chart.js |
| Authentication | Flask-Login |
| Forms | Flask-WTF |
| Export | Pandas + OpenPyXL |
| PDF Reports | WeasyPrint |

---

# 4. Authentication System

## Login Type

### Normal Username/Password Authentication

Email authentication नहीं होगा।

---

## Login Fields

| Field | Type |
| --- | --- |
| Username | Text |
| Password | Password |

---

## User Roles

| Role | Access |
| --- | --- |
| Admin | Full access |
| Accountant | Manage expenses |
| Viewer | View only |

---

# 5. Main Modules

---

# MODULE 1 — Dashboard

## Features

### Summary Cards

- Total Expenses
- This Month Expense
- Today Expense
- Total Vendors

---

## Charts

- Monthly Expense Chart
- Category-wise Pie Chart

---

## Activity Section

- Recent Expenses

---

# MODULE 2 — Expense Management

## Add Expense

### Fields

| Field | Type |
| --- | --- |
| Expense Title | Text |
| Amount | Decimal |
| Category | Dropdown |
| Vendor | Dropdown |
| Payment Method | Dropdown |
| Expense Date | Date |
| Receipt Upload | File |
| Notes | Textarea |

---

## Payment Methods

- Cash
- UPI
- Bank Transfer
- Card
- Cheque

---

## Expense Features

✅ Add Expense

✅ Edit Expense

✅ Delete Expense

✅ Search Expense

✅ Filter Expense

✅ Pagination

---

# MODULE 3 — Categories

## Features

✅ Add Category

✅ Edit Category

✅ Delete Category

---

## Default Categories

- Salary
- Electricity
- Internet
- Stationery
- Maintenance
- Furniture
- Transport
- Event Expense
- Marketing
- Miscellaneous

---

# MODULE 4 — Vendor Management

## Vendor Fields

| Field | Type |
| --- | --- |
| Vendor Name | Text |
| Phone | Text |
| GST Number | Text |
| Address | Textarea |

---

## Features

✅ Add Vendor

✅ Edit Vendor

✅ Vendor Expense History

---

# MODULE 5 — Reports System

## Reports

### Monthly Report

- Total monthly expense
- Category summary

---

### Yearly Report

- Month-wise report

---

### Vendor Report

- Vendor-wise expenses

---

### Category Report

- Category-wise expense report

---

## Export Features

✅ Excel Export

✅ CSV Export

✅ PDF Export

---

# MODULE 6 — Settings

## Features

### School Details

- School Name
- Logo
- Address
- Phone Number

---

### System Settings

- Currency
- Date Format

---

# 6. Complete Frontend Pages

---

# Authentication Pages

| Page | Purpose |
| --- | --- |
| Login Page | User login |

---

# Dashboard Pages

| Page | Purpose |
| --- | --- |
| Dashboard | Expense overview |

---

# Expense Pages

| Page | Purpose |
| --- | --- |
| Expense List | View expenses |
| Add Expense | Create expense |
| Edit Expense | Update expense |
| Expense Details | Full expense view |

---

# Category Pages

| Page | Purpose |
| --- | --- |
| Category List | View categories |
| Add Category | Add category |

---

# Vendor Pages

| Page | Purpose |
| --- | --- |
| Vendor List | View vendors |
| Add Vendor | Create vendor |

---

# Reports Pages

| Page | Purpose |
| --- | --- |
| Monthly Reports | Monthly analytics |
| Yearly Reports | Annual analytics |
| Export Reports | Download reports |

---

# Settings Pages

| Page | Purpose |
| --- | --- |
| Settings | Application settings |

---

# 7. UI Layout Plan

---

# Top Navbar

## Contains

- School Name
- Logged-in User
- Logout Button

---

# Sidebar Menu

```
Dashboard
Expenses
Categories
Vendors
Reports
Settings
Logout
```

---

# Recommended Design

## Use

- Bootstrap Admin Template
- Responsive Layout
- Clean White UI
- Dark Sidebar

---

# 8. Final Flask Project Structure

```
wisdom_expense_tracker/
│
├── app/
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   └── uploads/
│   │       └── receipts/
│   │
│   ├── templates/
│   │   │
│   │   ├── auth/
│   │   │   └── login.html
│   │   │
│   │   ├── dashboard/
│   │   │   └── dashboard.html
│   │   │
│   │   ├── expenses/
│   │   │   ├── list.html
│   │   │   ├── add.html
│   │   │   ├── edit.html
│   │   │   └── details.html
│   │   │
│   │   ├── categories/
│   │   ├── vendors/
│   │   ├── reports/
│   │   ├── settings/
│   │   │
│   │   └── includes/
│   │       ├── navbar.html
│   │       ├── sidebar.html
│   │       └── footer.html
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── expense.py
│   │   ├── category.py
│   │   └── vendor.py
│   │
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── dashboard_routes.py
│   │   ├── expense_routes.py
│   │   ├── category_routes.py
│   │   ├── vendor_routes.py
│   │   ├── report_routes.py
│   │   └── settings_routes.py
│   │
│   ├── forms/
│   │   ├── login_form.py
│   │   ├── expense_form.py
│   │   └── vendor_form.py
│   │
│   ├── services/
│   │   ├── report_service.py
│   │   ├── export_service.py
│   │   └── dashboard_service.py
│   │
│   ├── utils/
│   │   ├── decorators.py
│   │   ├── helpers.py
│   │   └── validators.py
│   │
│   ├── __init__.py
│
├── instance/
│   └── school.db
│
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

---

# 9. Final Database Design

---

# users Table

| Column | Type |
| --- | --- |
| id | Integer |
| username | String |
| password_hash | String |
| full_name | String |
| role | String |
| created_at | DateTime |

---

# categories Table

| Column | Type |
| --- | --- |
| id | Integer |
| name | String |

---

# vendors Table

| Column | Type |
| --- | --- |
| id | Integer |
| vendor_name | String |
| phone | String |
| gst_number | String |
| address | Text |

---

# expenses Table

| Column | Type |
| --- | --- |
| id | Integer |
| title | String |
| amount | Numeric(10,2) |
| category_id | FK |
| vendor_id | FK |
| payment_method | String |
| expense_date | Date |
| receipt | String |
| notes | Text |
| created_by | FK |
| created_at | DateTime |

---

# 10. Recommended APIs

---

# Authentication APIs

```
POST /login
GET /logout
```

---

# Expense APIs

```
GET /expenses
GET /expenses/add
POST /expenses/add
GET /expenses/edit/<id>
POST /expenses/update/<id>
POST /expenses/delete/<id>
```

---

# Category APIs

```
GET /categories
POST /categories/add
POST /categories/update/<id>
POST /categories/delete/<id>
```

---

# Vendor APIs

```
GET /vendors
POST /vendors/add
POST /vendors/update/<id>
POST /vendors/delete/<id>
```

---

# Reports APIs

```
GET /reports/monthly
GET /reports/yearly
GET /reports/category
GET /reports/vendor
GET /reports/export/excel
GET /reports/export/pdf
```

---

# 11. Receipt Upload System

## Upload Folder

```
static/uploads/receipts/
```

---

## Allowed File Types

- JPG
- PNG
- PDF

---

## Security

- Unique filename
- File size limit
- Safe upload validation

---

# 12. Security Plan

## Authentication Security

✅ Password hashing

✅ Session management

---

## Form Security

✅ CSRF protection

✅ Input validation

---

## Database Security

✅ SQLAlchemy ORM only

✅ No raw SQL queries

---

## Access Security

✅ Role-based access control

---

# 13. Bug Prevention Strategy

## Important Rules

### Expense Amount

Use:

```python
db.Numeric(10,2)
```

---

### Validation

- Required fields check
- Positive amount only
- Date validation

---

### Safe Delete

Delete confirmation popup mandatory।

---

### Transactions

Critical operations transactional होंगे।

---

# 14. Reports & Analytics

## Dashboard Analytics

### Charts

- Monthly Expense Trend
- Category Expense Pie Chart

---

## Reports

✅ Monthly Report

✅ Yearly Report

✅ Vendor Report

✅ Category Report

---

# 15. Export System

## Excel Export

Use:

```
Pandas + OpenPyXL
```

---

## PDF Export

Use:

```
WeasyPrint
```

---

# 16. Deployment Plan

## Recommended Server Stack

```
Ubuntu VPS
Nginx
Gunicorn
Flask
SQLite
```

---

# Domain Example

```
expense.wisdomschool.in
```

---

# SSL Certificate

Use:

```
Let's Encrypt
```

---

# 17. Backup Strategy

## Daily SQLite Backup

```bash
cp school.db backup/school_$(date +%F).db
```

---

## Uploads Backup

Receipts folder backup भी daily लेना।

---

# 18. Final Development Timeline

| Task | Time |
| --- | --- |
| Project Setup | 4 Hours |
| Database Models | 4 Hours |
| Authentication | 5 Hours |
| Dashboard | 6 Hours |
| Expense Module | 1 Day |
| Categories Module | 3 Hours |
| Vendor Module | 4 Hours |
| Reports System | 1 Day |
| Export System | 5 Hours |
| Testing | 1 Day |
| Deployment | 4 Hours |

---

# Total Estimated Time

## MVP Version

### 4–5 Days

---

## Full Stable Version

### 7–10 Days

---

# 19. Final MVP Features

## First Version में ये modules जरूर होने चाहिए:

✅ Login System

✅ Dashboard

✅ Expense Management

✅ Categories

✅ Vendor Management

✅ Reports

✅ Excel Export

✅ Receipt Upload

---

# 20. Future Upgrade Options

## Future Features

- Income Tracking
- Fee Management
- Salary Management
- SMS Alerts
- WhatsApp Reports
- Multi-Branch Support
- Cloud Backup
- Audit Logs
- Budget Planning
- Mobile App

---

# 21. Final Recommended Architecture

```
Frontend (Bootstrap + HTML)
            ↓
Flask Backend
            ↓
SQLAlchemy ORM
            ↓
SQLite Database
            ↓
Reports + Export System
```

---

# 22. Final Practical Recommendation

## Best Development Approach

### Phase 1

MVP जल्दी complete करो

### Phase 2

Reports improve करो

### Phase 3

Automation features add करो

---

# Final Conclusion

यह architecture:

✅ Fast develop होगा

✅ Easy maintain होगा

✅ School staff आसानी से use कर पाएंगे

✅ Low-cost hosting पर चलेगा

✅ Future scalable रहेगा

✅ SQLite के साथ stable रहेगा

✅ Small/medium school use case के लिए perfect रहेगा