from flask import Flask, request
from controllers.auth_controller import AuthController
from controllers.users_controller import UsersController
from controllers.destinations_controller import DestinationsController
from utils.recommendation import Recommendation
from models.database import db
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

# Set up the configuration using environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)

# Initialize database
db.init_app(app)

# Routes for authentication
@app.route('/register', methods=['POST'])
def register():
    return AuthController.register(request)

@app.route('/login', methods=['POST'])
def login():
    return AuthController.login(request)

# Routes for user management
@app.route('/users', methods=['GET'])
def users():
    return UsersController.index()

@app.route('/users/<int:id>', methods=['GET'])
def user_by_id(id):
    return UsersController.get_user_by_id(id)

# Routes for destinations
@app.route('/destinations', methods=['GET'])
def destinations():
    return DestinationsController.index()

@app.route('/destinations/<int:id>', methods=['GET'])
def destinations_by_id(id):
    return DestinationsController.get_by_id(id)

@app.route('/destinations/search/name', methods=['GET'])
def search_name():
    name = request.args.get('name')
    return DestinationsController.search_by_name(name)

@app.route('/destinations/search/city', methods=['GET'])
def search_city():
    city = request.args.get('city')
    return DestinationsController.search_by_city(city)

@app.route('/destinations', methods=['POST'])
def create_destination():
    return DestinationsController.create(request)

# Route for travel recommendation
@app.route('/predict', methods=['POST'])
def predict():
    destination_id = request.json['destination_id']
    return Recommendation.predict(destination_id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
