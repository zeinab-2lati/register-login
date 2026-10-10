from flask import Flask, request, jsonify
from extensions import db
from models import User
from services import register_user, login_user

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/auth/register", methods=["POST"])
def register():
    data = request.json

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    user = register_user(username, email, password)

    return jsonify({
        "success": True,
        "message": "User registered successfully",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 201
    

@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = login_user(email, password)

    if user is None:
        return jsonify({
            "success": False,
            "message": "Invalid email or password"
        }), 401

    return jsonify({
        "success": True,
        "message": "Login successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 200



if __name__ == "__main__":
    app.run(debug=True)