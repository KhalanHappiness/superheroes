# Superheroes Flask API

A RESTful Flask API that manages superheroes, their powers, and the relationships between them via HeroPowers. This API supports data retrieval, updates, and validation based on business rules.

---

##  Project Structure

Superheroes/
├── server/
│ ├── app.py
│ ├── models/
│ │ ├── init.py
| | ├── base.py 
│ │ ├── hero.py
│ │ ├── power.py
│ │ └── hero_power.py
│ ├── config.py
│ └── seed.py
├── migrations/
└── README.md

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KhalanHappiness/superheroes
   cd Superheroes

Create and activate a virtual environment:


- pipenv install
- pinenv shell

## Install dependencies:

- pip install flask_sqlalchemy flask_migrate flask


# Run migrations:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed the database:
python seed.py
Start the server:
flask run

### Data Models & Relationships
## Hero
id: Integer, Primary Key

name: String

super_name: String

Relationships: Has many Powers through HeroPowers

## Power
id: Integer, Primary Key

name: String

description: String (min 20 characters)

Relationships: Has many Heroes through HeroPowers

## HeroPower
id: Integer, Primary Key

strength: String (Strong, Weak, Average)

hero_id: Foreign Key → Hero

power_id: Foreign Key → Power

Relationships: Belongs to Hero, Belongs to Power

-- Deleting a Hero or Power cascades to delete related HeroPowers.

## Validations
Power.description must be present and at least 20 characters long.

HeroPower.strength must be one of: "Strong", "Weak", "Average".

## API Endpoints
GET /heroes
Returns a list of all heroes:


[
  { "id": 1, "name": "Kamala Khan", "super_name": "Ms. Marvel" },
  ...
]
GET /heroes/:id
Returns a specific hero with related powers:

 If found:


{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "id": 1,
      "strength": "Strong",
      "power_id": 2,
      "hero_id": 1,
      "power": {
        "id": 2,
        "name": "flight",
        "description": "gives the wielder the ability to fly through the skies at supersonic speed"
      }
    }
  ]
}
 If not found:


{ "error": "Hero not found" }
GET /powers
Returns a list of all powers:

[
  { "id": 1, "name": "super strength", "description": "..." },
  ...
]
GET /powers/:id
 If found:

{ "id": 1, "name": "super strength", "description": "..." }
If not found:


{ "error": "Power not found" }

PATCH /powers/:id
Updates a power's description.
 If updated:


{ "id": 1, "name": "super strength", "description": "Valid Updated Description" }
 If not found:


{ "error": "Power not found" }
 If validation fails:


{ "errors": ["validation errors"] }

POST /hero_powers
Creates a new HeroPower.

Request Body:

{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
 If successful:


{
  "id": 11,
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average",
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "id": 1,
    "name": "super strength",
    "description": "..."
  }
}
 If validation fails:


{ "errors": ["validation errors"] }
Testing
You can use  Postman to test all endpoints. Be sure your server is running on http://127.0.0.1:5000.

Technologies Used
Python 3 / Flask

SQLAlchemy

Flask-Migrate

PostgreSQL / SQLite

SQLAlchemy Serializer



 ## Notes
Make sure to set your FLASK_APP to app.py before running the server:

export FLASK_APP=app


 Author
Built by Happiness Khalan