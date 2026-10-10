from models import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


def register_user(username, email, password):
    password_hash = generate_password_hash(password)

    user = User(
        username=username,
        email=email,
        password_hash=password_hash
    )

    db.session.add(user)
    db.session.commit()

    return user


def login_user(email, password):
    user = User.query.filter_by(email=email).first()

    if user is None:
        return None

    if check_password_hash(user.password_hash, password):
        return user

    return None
