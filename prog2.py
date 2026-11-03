from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check that name and email are provided
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({
            "message": "Name and email are required",
            "success": False
        }), 400

    name = data['name']
    email = data['email']

    # Validate email format
    email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if not re.match(email_pattern, email):
        return jsonify({
            "message": "Invalid email format",
            "success": False
        }), 400

    # Successful registration
    return jsonify({
        "message": f"User {name} registered successfully with {email}",
        "success": True
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
