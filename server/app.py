from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

from models import db
from models.hero import Hero
from models.power import Power
from models.hero_power import HeroPower

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'app.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False


db.init_app(app)
migrate = Migrate(app, db)



@app.route('/')
def index():
    return "Index for Hero API"

@app.route('/heroes')
def get_heroes():

    heroes = Hero.query.all()
    heroes_list = []

    for hero in heroes:

        hero_dict = hero.to_dict(rules=('-hero_powers', '-powers'))

        heroes_list.append(hero_dict)

    response = make_response(
        heroes_list,
        200
    )
    return response

