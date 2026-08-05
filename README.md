# 🔐 Flask Auth & OTP Verification REST API

A clean, production-ready, and modular RESTful API built with Python and Flask. This project features complete User Management, Authentication logic, JWT Authorization, and OTP (One-Time Password) Verification using Flask Blueprints and the Application Factory pattern.

---

## ✨ Features

- 👤 **User Management:** Complete user registration, login, and protected profile retrieval.
- 🔑 **OTP Verification:** Secure One-Time Password logic for verification workflows.
- 🛡️ **JWT Authentication:** Protected endpoints requiring Bearer Token authorization.
- 🏗️ **Modular Architecture:** Utilizes Flask Blueprints and the Application Factory pattern for scalability and maintainability.
- 🔐 **Environment Configuration:** Sensitive credentials and secrets managed securely via `.env`.
- 🧪 **Automated Testing:** Unit and integration testing setup configured with `pytest`.

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.x
- **Framework:** Flask
- **ORM & Database:** Flask-SQLAlchemy (or ORM of choice)
- **Testing:** Pytest
- **Configuration:** python-dotenv

---

## 📁 Project Structure

```text
py/
├── app/
│   ├── models/
│   │   ├── user.py          # User Database Model
│   │   └── otp.py           # OTP Database Model
│   ├── routes/
│   │   ├── user_routes.py   # User Auth & Management Endpoints
│   │   └── otp_routes.py    # OTP Endpoints
│   ├── config.py            # App Configurations
│   ├── extensions.py        # Extensions Initializer (DB, JWT, etc.)
│   └── __init__.py          # Application Factory Setup
├── app.py                   # Main Entry Point
├── .env                     # Environment Variables (Keep Private!)
├── .gitignore
├── requirements.txt         # Project Dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have Python 3.10+ installed on your system.

### 2. Clone the Repository

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/Python_Flask_Backend_Project.git

cd Python_Flask_Backend_Project
```

### 3. Setup Virtual Environment & Install Dependencies

```bash
# Create Virtual Environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux / Mac)
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the root directory and define your secrets:

```env
FLASK_ENV=development
SECRET_KEY=your_super_secret_key
DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=your_jwt_secret_key
```

### 5. Run the Application

```bash
python app.py
```

The server will start running at:

```
http://127.0.0.1:5000/
```

---

## 🔌 API Endpoints Summary

| Module | Route | Method | Authorization | Description |
|---------|-------|--------|---------------|-------------|
| User | `/api/user/register` | POST | None | Register a new user |
| User | `/api/user/login` | POST | None | User login and token generation |
| User | `/api/user` | GET | Bearer `<TOKEN>` | Get all users (Protected) |
| OTP | `/api/otp/send` | POST | None | Request OTP generation |
| OTP | `/api/otp/verify` | POST | None | Verify submitted OTP |

---

## 🧪 Running Tests

To execute the automated test suite using `pytest`, run:

```bash
pytest
```

---

## 📝 License

This project is open-source and available under the MIT License.
