from sqlalchemy_serializer import SerializerMixin

from . import db

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    seriliaze_rules = ("-hero_powers.hero", "-hero_powers.power",)


    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column (db.String)
    hero_id =db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    hero = db.relationship('Hero', back_populates = "hero_powers")
    power = db.relationship('Power', back_populates ="hero_powers")


    def __repr__(self):
        return f'<HeroPower {self.id}, {self.strength}>'