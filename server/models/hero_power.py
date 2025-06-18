from sqlalchemy_serializer import SerializerMixin

from . import db

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'


    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column (db.String)
    hero_id =db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))


    def __repr__(self):
        return f'<HeroPower {self.id}, {self.strength}>'