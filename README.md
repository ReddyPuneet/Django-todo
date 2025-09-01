# 📝 Django To-Do App

A simple To-Do application built with **Django**.  
Users can add, view, and manage their tasks.

---

## 🚀 Features
- Add new tasks
- Mark tasks as completed
- Delete tasks
- Simple and clean UI

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/django-todo.git
   cd django-todo
   
python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows

Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py migrate


Start the development server:

python manage.py runserver


Open in your browser:

http://127.0.0.1:8000/

📂 Project Structure
todo/                # Django project folder (settings, urls)
mytodo/              # Django app (models, views, templates)
manage.py            # Django management script
db.sqlite3           # SQLite database (ignored in .gitignore)

🛠️ Technologies Used

Python 3.x

Django

SQLite
