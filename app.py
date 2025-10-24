from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage: {user_id: user_data}
users = {}

# Helper: Generate unique ID
def generate_id():
    return str(uuid.uuid4())

# GET /users - Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

# GET /users/<id> - Get user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

# POST /users - Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Name and email are required"}), 400

    user_id = generate_id()
    new_user = {
        "id": user_id,
        "name": data['name'],
        "email": data['email'],
        "age": data.get('age')  # optional field
    }
    
    users[user_id] = new_user
    return jsonify(new_user), 201

# PUT /users/<id> - Update an existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Update only provided fields
    if 'name' in data:
        users[user_id]['name'] = data['name']
    if 'email' in data:
        users[user_id]['email'] = data['email']
    if 'age' in data:
        users[user_id]['age'] = data['age']

    return jsonify(users[user_id]), 200

# DELETE /users/<id> - Delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user}), 200

# Health check
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "User API is running! Use /users"}), 200

if __name__ == '__main__':
    app.run(debug=True)
