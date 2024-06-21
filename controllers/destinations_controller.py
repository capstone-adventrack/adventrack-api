from flask import jsonify, request
from models.database import db
from models.destination import Destination

class DestinationsController:
    @staticmethod
    def index():
        destinations = Destination.query.all()
        return jsonify([dest.serialize() for dest in destinations]), 200

    @staticmethod
    def get_by_id(destination_id):
        destination = Destination.query.get(destination_id)
        if not destination:
            return jsonify({'error': 'Destination not found'}), 404
        return jsonify(destination.serialize()), 200

    @staticmethod
    def search_by_name(name):
        destinations = Destination.query.filter(Destination.place_name.ilike(f'%{name}%')).all()
        return jsonify([dest.serialize() for dest in destinations]), 200

    @staticmethod
    def search_by_city(city):
        destinations = Destination.query.filter(Destination.city.ilike(f'%{city}%')).all()
        return jsonify([dest.serialize() for dest in destinations]), 200
