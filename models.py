import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# database_path = os.environ['DATABASE_URL']
database_path = "postgresql://{}:{}@{}/{}".format(
    'postgres', 'root', 'localhost:5432', 'capstone')

db = SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    actors = db.relationship('Actor', secondary='castings', backref='movies')
    def __repr__(self):
        return f'<Movie {self.title}>'

class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    # movies = db.relationship('Movie', secondary='castings', backref='actors')
    def __repr__(self):
        return f'<Actor {self.name}>'

class Casting(db.Model):
    __tablename__ = 'castings'
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    def __repr__(self):
        return f'<Casting {self.id}>'

