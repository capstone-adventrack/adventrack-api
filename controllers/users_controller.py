from flask import jsonify
from models.user import User

class UsersController:
    @staticmethod
    def index():
        users = User.query.all()
        return jsonify([user.serialize() for user in users]), 200

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(user.serialize()), 200
