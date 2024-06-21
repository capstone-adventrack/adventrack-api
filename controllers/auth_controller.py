from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from models.database import db
from models.user import User

class AuthController:
    @staticmethod
    def register(request):
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')

        if not username or not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'error': 'User already exists'}), 400

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201

    @staticmethod
    def login(request):
        email = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
            return jsonify({'error': 'Missing email or password'}), 400

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Invalid email or password'}), 401

        return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
