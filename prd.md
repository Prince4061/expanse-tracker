# Wisdom The Global World School – Expense Tracker System

---

# 1. Product Information

| Item | Details |
| --- | --- |
| Product Name | Wisdom Expense Tracker |
| Product Type | Web Application |
| Client | Wisdom The Global World School |
| Platform | Web-Based Internal System |
| Target Users | School Admin & Accounts Staff |
| Technology | Flask + SQLite |

---

# 2. Product Overview

Wisdom Expense Tracker एक internal web application होगी जिसका उपयोग स्कूल अपने daily, monthly और yearly expenses को manage करने के लिए करेगा।

यह system manual accounting process को simplify करेगा और सभी financial expenses को digital format में store करेगा।

---

# 3. Product Goals

## Primary Goals

- School expenses digitally manage करना
- Expense records maintain करना
- Reports generate करना
- Vendor tracking करना
- Accounting process simplify करना
- Fast data retrieval देना

---

# 4. Business Objectives

| Objective | Description |
| --- | --- |
| Reduce Manual Work | Register-based tracking हटाना |
| Improve Accuracy | Human errors कम करना |
| Faster Reporting | Instant monthly/yearly reports |
| Better Record Keeping | Expense history maintain करना |
| Centralized Data | All records in one system |

---

# 5. Target Users

---

# User Type 1 — Admin

## Responsibilities

- Full system management
- User management
- Expense approval
- Reports access
- Settings management

---

# User Type 2 — Accountant

## Responsibilities

- Add expenses
- Edit expenses
- Upload receipts
- View reports

---

# User Type 3 — Viewer

## Responsibilities

- View dashboard
- View reports only

---

# 6. Scope of the Project

---

# In Scope

✅ Authentication System

✅ Dashboard

✅ Expense Management

✅ Categories Management

✅ Vendor Management

✅ Reports System

✅ Excel/PDF Export

✅ Receipt Upload

✅ Role-Based Access

---

# Out of Scope (Phase 1)

❌ Fee Management

❌ Payroll Management

❌ SMS Integration

❌ Mobile App

❌ Online Payments

❌ Multi-Branch Support

---

# 7. Functional Requirements

---

# MODULE 1 — Authentication

## Description

System users secure login के माध्यम से application access करेंगे।

---

## Functional Requirements

### Login

- User username/password से login करेगा।
- Invalid credentials पर error message दिखेगा।

---

## Logout

- User session safely terminate होगा।

---

## Access Control

- Role-based permissions लागू होंगे।

---

# MODULE 2 — Dashboard

## Description

Dashboard expense overview और analytics दिखाएगा।

---

## Features

### Summary Cards

- Total Expenses
- Monthly Expenses
- Today Expenses
- Total Vendors

---

## Charts

- Monthly Expense Trend
- Category-wise Expense Chart

---

## Recent Activity

- Latest expenses list

---

# MODULE 3 — Expense Management

## Description

School expenses add, update, view और delete किए जाएंगे।

---

## Add Expense

### Fields

| Field | Required |
| --- | --- |
| Expense Title | Yes |
| Amount | Yes |
| Category | Yes |
| Vendor | Optional |
| Payment Method | Yes |
| Expense Date | Yes |
| Notes | Optional |
| Receipt Upload | Optional |

---

## Expense Features

✅ Add Expense

✅ Edit Expense

✅ Delete Expense

✅ Search Expenses

✅ Filter Expenses

✅ Pagination

---

## Filters

- Date Range
- Category
- Vendor
- Payment Method

---

# MODULE 4 — Categories Management

## Description

Expense categories manage करने के लिए module।

---

## Features

✅ Add Category

✅ Edit Category

✅ Delete Category

---

## Default Categories

- Salary
- Electricity
- Internet
- Furniture
- Stationery
- Maintenance
- Event Expense
- Marketing
- Miscellaneous

---

# MODULE 5 — Vendor Management

## Description

Expense vendors की details maintain की जाएंगी।

---

## Vendor Fields

| Field | Required |
| --- | --- |
| Vendor Name | Yes |
| Phone | No |
| GST Number | No |
| Address | No |

---

## Features

✅ Add Vendor

✅ Edit Vendor

✅ Delete Vendor

✅ Vendor Expense History

---

# MODULE 6 — Reports System

## Description

System विभिन्न expense reports generate करेगा।

---

## Reports

### Monthly Report

- Month-wise expense summary

---

### Yearly Report

- Annual expense overview

---

### Vendor Report

- Vendor-wise expenses

---

### Category Report

- Category-wise spending

---

## Export Features

✅ Export to Excel

✅ Export to CSV

✅ Export to PDF

---

# MODULE 7 — Settings

## Description

School-related settings manage करना।

---

## Features

### School Information

- School Name
- Logo
- Address
- Contact Number

---

### System Settings

- Currency
- Date Format

---

# 8. Non-Functional Requirements

---

# Performance

- Page load under 3 seconds
- Fast dashboard loading

---

# Security

✅ Password hashing

✅ CSRF protection

✅ Secure sessions

✅ Role-based access

---

# Reliability

- Daily database backup
- Data consistency
- Safe transactions

---

# Scalability

- Future PostgreSQL migration support
- Modular architecture

---

# Usability

- Simple UI
- Non-technical users friendly
- Responsive design

---

# 9. Technical Requirements

| Component | Technology |
| --- | --- |
| Backend | Flask |
| Database | SQLite |
| ORM | SQLAlchemy |
| Frontend | HTML + Bootstrap |
| Charts | Chart.js |
| Export | Pandas/OpenPyXL |
| PDF | WeasyPrint |

---

# 10. Database Requirements

---

# users Table

| Column | Type |
| --- | --- |
| id | Integer |
| username | String |
| password_hash | String |
| full_name | String |
| role | String |

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

---

# 11. API Requirements

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
POST /expenses/add
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

# 12. Security Requirements

---

# Authentication Security

- Password hashing mandatory
- Session timeout support

---

# File Upload Security

- Allowed file types only
- File size limit
- Safe filename handling

---

# Database Security

- ORM-only database operations
- Input validation mandatory

---

# Access Control

- Admin-only sensitive actions

---

# 13. UI/UX Requirements

---

# Design Style

- Clean admin dashboard
- Responsive layout
- Easy navigation

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

# Color Theme

- White content area
- Dark sidebar
- Blue primary buttons

---

# 14. Deployment Requirements

| Item | Details |
| --- | --- |
| Server | Ubuntu VPS |
| Web Server | Nginx |
| WSGI | Gunicorn |
| SSL | Let's Encrypt |

---

# 15. Backup Requirements

## Daily Backup

- SQLite database backup
- Uploads folder backup

---

# Backup Retention

- Minimum 30 days

---

# 16. Risks & Mitigation

| Risk | Solution |
| --- | --- |
| Data loss | Daily backup |
| Unauthorized access | Role-based access |
| File upload abuse | File validation |
| Wrong entries | Edit history/future logs |

---

# 17. Development Timeline

| Phase | Estimated Time |
| --- | --- |
| Planning | 1 Day |
| Backend Development | 3 Days |
| Frontend Development | 2 Days |
| Reports & Export | 1 Day |
| Testing | 1 Day |
| Deployment | 1 Day |

---

# Total Estimated Timeline

## MVP

### 4–5 Days

---

## Full Stable Version

### 7–10 Days

---

# 18. MVP Definition

## Phase 1 Deliverables

✅ Login System

✅ Dashboard

✅ Expense Management

✅ Categories

✅ Vendors

✅ Reports

✅ Excel Export

✅ Receipt Upload

---

# 19. Future Enhancements

- Fee Management
- Salary Module
- Budget Planning
- Audit Logs
- Notifications
- WhatsApp Reports
- Multi-School Support
- Mobile Application

---

# 20. Final Recommendation

यह system:

✅ Fast develop होगा

✅ Easy maintain रहेगा

✅ School accounting process simplify करेगा

✅ Small/medium scale usage के लिए perfect रहेगा

✅ SQLite के साथ efficiently run करेगा

✅ Future scalable रहेगा