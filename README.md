# 🧰 Django REST API – User Registration System

A simple Django REST Framework project for registering users with validations. Useful as a starter template for any backend.

---

## 🚀 Features

✅ RESTful API using Django REST Framework  
✅ Custom validators (age limit, no space in username, password match)  
✅ SQLite for database  
✅ Unique checks for username and email  
✅ Ready to connect with React, Postman, or mobile apps  
✅ Easily deployable on Heroku or Render

---

## 📦 Requirements

- Python 3.8+
- Django 4.x
- djangorestframework

---

## 🔧 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/userapi.git
cd userapi

# Create a virtual environment
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate DB
python manage.py migrate

# Run the server
python manage.py runserver
```

## 🧪 API Endpoints

| Method | Endpoint           | Description    |
| ------ | ------------------ | -------------- |
| GET    | `/api/users/`      | List all users |
| POST   | `/api/users/`      | Create user    |
| GET    | `/api/users/<id>/` | Get user by ID |
| PUT    | `/api/users/<id>/` | Update user    |
| DELETE | `/api/users/<id>/` | Delete user    |

## 🧾 Sample POST Request

POST /api/users/
{
  "username": "nitesh_s",
  "email": "nitesh@example.com",
  "age": 21,
  "password": "mypassword",
  "confirm_password": "mypassword"
}


## 📂 Project Structure

userapi/
├── accounts/          # App with model, views, serializers
├── userapi/           # Project settings
├── manage.py
├── requirements.txt
└── README.md
