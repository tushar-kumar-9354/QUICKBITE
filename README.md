# 🍔 QuickBite - Restaurant Ordering System API

## 📋 Overview
**QuickBite** is a full-featured restaurant ordering system built with Flask that demonstrates real-world API development, authentication, database management, and frontend integration.

## 🚀 Features

### 🔐 **Authentication & Security**
- JWT-based authentication system
- Secure user registration and login
- Token-protected API endpoints
- Password validation and error handling

### 🛒 **Order Management**
- Create new food orders
- View personal order history
- Real-time order tracking
- Quantity validation and item management

### 🏗️ **Technical Stack**
- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: JWT (JSON Web Tokens)
- **CORS**: Cross-Origin Resource Sharing enabled
- **Frontend**: HTML5, CSS3, JavaScript
- **Database Migrations**: Flask-Migrate

## 📁 Project Structure

```
quickbite/
├── app/
│   ├── __init__.py              # Flask application factory
│   ├── models.py               # Database models (User, Order)
│   ├── extensions.py           # Flask extensions (DB, CORS, Migrate)
│   ├── errors.py              # Custom error handlers
│   ├── utils/
│   │   └── auth.py            # JWT authentication decorator
│   ├── routes/
│   │   ├── auth.py            # Authentication endpoints
│   │   ├── orders.py          # Order management endpoints
│   │   └── health.py          # Health check and home page
│   └── templates/
│       └── index.html         # Frontend web interface
├── migrations/                 # Database migration files
├── instance/                  # Database instance
├── run.py                     # Application entry point
├── wsgi.py                    # Production WSGI entry
├── reset_db.py               # Database reset utility
└── README.md                 # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step 1: Clone and Setup
```bash
# Clone the repository
git clone <repository-url>
cd quickbite

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure Environment
Create a `.env` file (optional):
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
```

### Step 3: Initialize Database
```bash
# Reset database (clears existing data)
python reset_db.py

# Or use Flask-Migrate
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Step 4: Run the Application
```bash
# Development mode
python run.py

# The application will be available at:
# http://localhost:5000
```

## 📚 API Documentation

### Base URL
```
http://localhost:5000
```

### Authentication Endpoints

#### 1. Register New User
```http
POST /auth/register
Content-Type: application/json

{
    "username": "john_doe",
    "password": "securepassword123"
}
```
**Response:**
```json
{
    "message": "User registered successfully"
}
```

#### 2. Login
```http
POST /auth/login
Content-Type: application/json

{
    "username": "john_doe",
    "password": "securepassword123"
}
```
**Response:**
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Order Endpoints (Protected)

#### 3. Create New Order
```http
POST /orders/
Authorization: Bearer <your_jwt_token>
Content-Type: application/json

{
    "item": "Cheese Pizza",
    "quantity": 2
}
```
**Response:**
```json
{
    "message": "Order created successfully",
    "order": {
        "id": 1,
        "item": "Cheese Pizza",
        "quantity": 2,
        "user": "john_doe"
    }
}
```

#### 4. Get User Orders
```http
GET /orders/
Authorization: Bearer <your_jwt_token>
```
**Response:**
```json
[
    {
        "id": 1,
        "item": "Cheese Pizza",
        "quantity": 2,
        "user": "john_doe"
    },
    {
        "id": 2,
        "item": "Burger",
        "quantity": 1,
        "user": "john_doe"
    }
]
```

### Health Check
```http
GET /
```
**Response:** HTML interface or JSON health status

## 🌐 Web Interface

QuickBite includes a complete web interface accessible at `http://localhost:5000`:

### Features:
- **User Registration & Login** - Complete authentication flow
- **Order Creation** - Intuitive order form with validation
- **Order History** - View all past orders in JSON format
- **Responsive Design** - Clean, mobile-friendly interface
- **Real-time Feedback** - Instant status updates

### Interface Components:
1. **Registration Card** - Create new account
2. **Login Card** - Access existing account
3. **Order Creation Card** - Place new orders
4. **Order History Card** - View all previous orders

## 🔧 Database Models

### User Model
```python
class User:
    id: Integer (Primary Key)
    username: String (Unique, Required)
    password: String (Required)
    orders: Relationship to Order
```

### Order Model
```python
class Order:
    id: Integer (Primary Key)
    user_id: Integer (Foreign Key to User)
    item: String (Food item name)
    quantity: Integer
```

## 🛡️ Security Features

1. **JWT Authentication**
   - Token-based stateless authentication
   - Token expiration handling
   - Secure token validation

2. **Input Validation**
   - Required field checks
   - Quantity validation (positive integers)
   - Type checking

3. **Error Handling**
   - Custom HTTP error responses
   - Detailed error messages
   - Safe exception handling

## 🧪 Testing the API

### Using cURL
```bash
# Register a user
curl -X POST http://localhost:5000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass"}'

# Login and get token
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass"}'

# Create order (replace TOKEN with actual JWT)
curl -X POST http://localhost:5000/orders/ \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"item":"Pizza","quantity":2}'

# Get orders
curl -X GET http://localhost:5000/orders/ \
  -H "Authorization: Bearer TOKEN"
```

### Using Python Requests
```python
import requests

# Register
response = requests.post('http://localhost:5000/auth/register', 
    json={'username': 'newuser', 'password': 'password123'})

# Login
response = requests.post('http://localhost:5000/auth/login',
    json={'username': 'newuser', 'password': 'password123'})
token = response.json()['token']

# Create order
headers = {'Authorization': f'Bearer {token}'}
response = requests.post('http://localhost:5000/orders/',
    headers=headers,
    json={'item': 'Burger', 'quantity': 1})

# Get orders
response = requests.get('http://localhost:5000/orders/', headers=headers)
```

## 🔄 Database Management

### Resetting Database
```bash
python reset_db.py
```

### Using Flask-Migrate
```bash
# Initialize migrations
flask db init

# Create migration
flask db migrate -m "Description of changes"

# Apply migration
flask db upgrade

# Rollback migration
flask db downgrade
```

## 🚨 Common Issues & Solutions

### Issue 1: "Table order has no column named user_id"
**Solution:** Run database reset or migrations
```bash
python reset_db.py
```

### Issue 2: "404 Not Found" for endpoints
**Solution:** Check URL prefixes
- Authentication: `/auth/login`, `/auth/register`
- Orders: `/orders/` (not `/orders/orders`)

### Issue 3: "Invalid token" error
**Solution:** 
1. Ensure you're logged in first
2. Check if token is being sent in Authorization header
3. Verify token hasn't expired

### Issue 4: Database connection issues
**Solution:**
```bash
# Delete old database
rm instance/db.sqlite3

# Recreate tables
python reset_db.py
```

## 📝 Code Quality Features

1. **Modular Structure** - Clean separation of concerns
2. **Blueprints** - Organized route management
3. **Error Handling** - Comprehensive error responses
4. **Logging** - Debug information for development
5. **Configuration Management** - Environment-based settings

## 🎯 Learning Objectives Covered

This project demonstrates:
- ✅ RESTful API design principles
- ✅ JWT authentication implementation
- ✅ Database modeling with SQLAlchemy
- ✅ Flask application structure
- ✅ Frontend-Backend integration
- ✅ Error handling and validation
- ✅ CORS implementation
- ✅ Database migrations

## 🔮 Future Enhancements

1. **Password Hashing** - Add bcrypt for secure password storage
2. **Admin Panel** - Restaurant management interface
3. **Order Status** - Cooking, ready, delivered statuses
4. **Payment Integration** - Stripe or PayPal integration
5. **Email Notifications** - Order confirmation emails
6. **API Documentation** - Swagger/OpenAPI documentation
7. **Testing Suite** - Unit and integration tests
8. **Docker Support** - Containerized deployment

## 👥 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is for educational purposes. Feel free to modify and use as needed.

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Database management with [SQLAlchemy](https://www.sqlalchemy.org/)
- Authentication with [PyJWT](https://pyjwt.readthedocs.io/)
- CORS support with [Flask-CORS](https://flask-cors.readthedocs.io/)

## 📧 Contact & Support

For questions, issues, or feedback:
- Create an issue in the GitHub repository
- Check the troubleshooting section above

---

**Happy Ordering!** 🍕🍔🥗

*QuickBite - Your digital restaurant experience*