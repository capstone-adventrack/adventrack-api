from .database import db

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    time_minutes = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    pictures = db.Column(db.String(500), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'place_name': self.place_name,
            'description': self.description,
            'category': self.category,
            'city': self.city,
            'price': self.price,
            'rating': self.rating,
            'time_minutes': self.time_minutes,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'pictures': self.pictures
        }
