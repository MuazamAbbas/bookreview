# 📚 Django Book Review System

A simple yet modern Book Review System built with Django and Bootstrap 5.
Users can add, view, search, filter, update, delete books, and also leave reviews with ratings ⭐.

---

## 🚀 Features
- ✅ Add, Edit, Delete Books  
- ✅ Search & Filter Books  
- ✅ Responsive Bootstrap UI with cards  
- ✅ Dynamic Star Ratings ⭐  
- ✅ Reviews System (Users can add reviews with rating & comment)  
- ✅ Average Rating auto-updates per book  

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** Bootstrap 5, Bootstrap Icons
- **Database:** SQLite (default, can switch to PostgreSQL/MySQL)
- **Template Engine:** Django Templates

---

## ⚡ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/book-review-system.git
cd book-review-system

### 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run Migrations
python manage.py migrate

### 5. Create Superuser
python manage.py createsuperuser

### 6. Run the Server
python manage.py runserver

## 📂 Project Structure
bookreview/        # Main project folder
│
├── book/          # App folder
│   ├── migrations/
│   ├── templates/book/
│   │   ├── base.html
│   │   ├── book_list.html
│   │   ├── book_detail.html
│   │   ├── book_form.html
│   │   └── book_confirm_delete.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── bookreview/    # Project config folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md


