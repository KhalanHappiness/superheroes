from sqlalchemy_serializer import SerializerMixin

from . import db

class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"

    serialize_rules = ('-hero_powers.hero','-powers.hero')


    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates = 'hero', cascade = 'all, delete-orphan')

    def __repr__ (self):
        return f"<Hero {self.name}, {self.super_name}>"