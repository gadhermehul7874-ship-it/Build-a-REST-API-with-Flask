# Flask User API

A simple **RESTful API** built with **Flask** to manage users. It supports full CRUD operations (Create, Read, Update, Delete) with in-memory storage using a dictionary.

---

## Features

- **Create** a new user (`POST /users`)
- **Read** all users or a single user (`GET /users`, `GET /users/<id>`)
- **Update** an existing user (`PUT /users/<id>`)
- **Delete** a user (`DELETE /users/<id>`)
- Unique UUID-based user IDs
- Optional `age` field
- Health check endpoint

---

## Tech Stack

- **Python 3.6+**
- **Flask** (web framework)
- **UUID** (for generating unique IDs)

---

## API Endpoints

| Method | Endpoint          | Description                     | Required Fields       |
|--------|-------------------|----------------------------------|------------------------|
| `GET`  | `/`               | Health check                    | -                      |
| `GET`  | `/users`          | Get all users                   | -                      |
| `GET`  | `/users/<id>`     | Get user by ID                  | -                      |
| `POST` | `/users`          | Create a new user               | `name`, `email`        |
| `PUT`  | `/users/<id>`     | Update user (partial updates)   | At least one field     |
| `DELETE` | `/users/<id>`   | Delete a user                   | -                      |

---

## Request & Response Examples

### 1. Create a User (`POST /users`)

**Request:**
```json
{
  "name": "Alice Smith",
  "email": "alice@example.com",
  "age": 30
}
Response (201):
json{
  "id": "a1b2c3d4-...", 
  "name": "Alice Smith",
  "email": "alice@example.com",
  "age": 30
}

2. Get All Users (GET /users)
Response (200):
json[
  {
    "id": "a1b2c3d4-...",
    "name": "Alice Smith",
    "email": "alice@example.com",
    "age": 30
  }
]

3. Update User (PUT /users/<id>)
Request:
json{
  "age": 31
}
Response (200):
json{
  "id": "a1b2c3d4-...",
  "name": "Alice Smith",
  "email": "alice@example.com",
  "age": 31
}

4. Delete User (DELETE /users/<id>)
Response (200):
json{
  "message": "User deleted",
  "user": {
    "id": "a1b2c3d4-...",
    "name": "Alice Smith",
    "email": "alice@example.com",
    "age": 31
  }
}

How to Run
1. Clone the repository (or save the code)
bashgit clone <your-repo-url>
cd flask-user-api
2. Create a virtual environment (recommended)
bashpython -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
3. Install dependencies
bashpip install flask
4. Run the app
bashpython app.py

The server will start at: http://127.0.0.1:5000

Testing with curl
bash# Create user
curl -X POST http://127.0.0.1:5000/users \
     -H "Content-Type: application/json" \
     -d '{"name":"Bob", "email":"bob@example.com"}'

# Get all users
curl http://127.0.0.1:5000/users

# Update user
curl -X PUT http://127.0.0.1:5000/users/<user_id> \
     -H "Content-Type: application/json" \
     -d '{"age": 25}'
