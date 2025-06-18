from sqlalchemy_serializer import SerializerMixin

from . import db

class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    serialize_rules = ("-power.hero_powers",)

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates = 'power', cascade= 'all, delete-orphan')

    def __repr__(self):
        return f'<Power {self.id},{self.name}, {self.description}>'