from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    img = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String(), unique=True, nullable=False)

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    birth_year = db.Column(db.String(100), unique=True, nullable=False)
    gender = db.Column(db.String(100), unique=True, nullable=False)
    height = db.Column(db.String(100), unique=True, nullable=False)
    hair_color = db.Column(db.String(100), unique=True, nullable=False)
    eye_color = db.Column(db.String(100), unique=True, nullable=False)
     
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    climate = db.Column(db.String(100), unique=True, nullable=False)
    diameter = db.Column(db.String(100), unique=True, nullable=False)
    gravity = db.Column(db.String(100), unique=True, nullable=False)
    population = db.Column(db.String(100), unique=True, nullable=False)
    terrain = db.Column(db.String(100), unique=True, nullable=False)
     