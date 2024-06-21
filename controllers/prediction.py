from flask import Blueprint, request, jsonify
from utils.cloud_storage import download_model
from utils.recommendation import load_model, recommend_destinations
from models.destination import get_destination_by_id

prediction_bp = Blueprint('prediction', __name__)

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    destination_id = request.args.get("destination_id")
    
    if not destination_id:
        return jsonify({'error': 'User ID and Destination ID are required'}), 400
    
    model_path = download_model()
    model = load_model(model_path)
    
    recommended_ids = recommend_destinations(model, destination_id)
    
    recommendations = [get_destination_by_id(dest_id) for dest_id in recommended_ids]
    
    return jsonify(recommendations), 200
