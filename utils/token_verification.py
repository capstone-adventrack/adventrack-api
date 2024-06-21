import firebase_admin
from firebase_admin import auth, credentials
from flask import request, jsonify

cred = credentials.Certificate("path/to/firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

def verify_firebase_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        return None

def require_auth(f):
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1]
            decoded_token = verify_firebase_token(token)
            if decoded_token:
                request.user = decoded_token
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    return decorated_function
