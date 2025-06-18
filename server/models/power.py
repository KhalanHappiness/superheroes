from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from . import db

class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    serialize_rules = ("-power.hero_powers",)

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String, nullable =False)
    description = db.Column(db.String, nullable =False)

    hero_powers = db.relationship('HeroPower', back_populates = 'power', cascade= 'all, delete-orphan')

    # Validation for description
    @validates('description')
    def validate_description(self, key, description):
        if not description:
            raise ValueError("Description must be present")
        if len(description.strip()) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return description

    def __repr__(self):
        return f'<Power {self.id},{self.name}, {self.description}>'