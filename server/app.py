from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

from .models import db
from .models.hero import Hero
from .models.power import Power
from .models.hero_power import HeroPower

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
        200,
        {"Content-Type": "application/json"}
    )
    return response

@app.route('/heroes/<int:id>')
def get_hero_by_id(id):
    hero = Hero.query.filter(Hero.id == id).first()

    if hero:
        hero_dict = hero.to_dict()

        return make_response(hero_dict, 200)

    return make_response(jsonify({"error": "Hero not found"}), 404)

@app.route('/powers')
def get_powers():

    powers = Power.query.all()

    powers_dict = [power.to_dict(rules=('-hero_powers', '-heroes')) for power in powers]

    response = make_response(
        powers_dict,
        200,
        {"Content-Type": "application/json"}
        )
    return response

@app.route('/powers/<int:id>')
def get_power_by_id(id):
    power = Power.query.filter(Power.id == id).first()

    if power:
        power_dict = power.to_dict(rules=('-hero_powers', '-heroes'))

        return make_response(power_dict, 200)

    return make_response(jsonify({"error": "power not found"}), 404)

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)

    if not power:
        return make_response(jsonify({"error": "Power not found"}), 404)

    data = request.get_json()

    # Validation: Check if description is present and valid
    description = data.get('description')
    if not description or len(description.strip()) < 20:
        return make_response(jsonify({"errors": ["validation errors"]}), 400)

    # Update and commit
    power.description = description
    try:
        db.session.commit()
        return make_response(jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        }), 200)
    except:
        db.session.rollback()
        return make_response(jsonify({"errors": ["Something went wrong."]}), 500)