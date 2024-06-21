import pickle
from flask import jsonify
from models.destination import Destination
class Recommendation:
    def load_model(model_path):
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        return model

    def recommend_destinations(model, destination_id):
        recommendations = model.predict(destination_id)
        recommended_destinations = Destination.query.filter(Destination.id.in_(recommendations)).all()
        return jsonify([dest.serialize() for dest in recommended_destinations]), 200
