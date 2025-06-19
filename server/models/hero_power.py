from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from . import db

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    serialize_rules = ('-hero.hero_powers', '-power.hero_powers')


    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column (db.String, nullable =False)
    hero_id =db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable =False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable =False)

    hero = db.relationship('Hero', back_populates = "hero_powers")
    power = db.relationship('Power', back_populates ="hero_powers")

    # Validation for strength
    @validates('strength')
    def validate_strength(self, strength):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if strength not in valid_strengths:
            raise ValueError(f"Strength must be one of: {', '.join(valid_strengths)}")
        return strength


    def __repr__(self):
        return f'<HeroPower {self.id}, {self.strength}>'