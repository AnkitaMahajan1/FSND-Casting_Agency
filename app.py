import os
from flask import Flask, request, abort, jsonify,render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import *
from flask_moment import Moment
from flask_migrate import Migrate
from flask_wtf import Form
from forms import *
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  moment = Moment(app)
  CORS(app)
  #----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                              'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                              'GET, POST, PATCH, DELETE, OPTIONS')
    return response
  @app.route('/')
  # @requires_auth('get:actors')
  def index():
    return render_template('pages/index.html')

  #  Actors
  #  ----------------------------------------------------------------
    
  @app.route('/actors')
  @requires_auth('get:actors')
  def get_actors(payload):
    try:
      # Get a list of all actors from the actors table
      all_actors = Actor.query.all()
      actor_list = [{'name': actor.name, 'age': actor.age, 'gender': actor.gender} for actor in all_actors]
      return jsonify(actor_list)
    except:
      abort(500)

  # Create a new actor
  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def create_actor(payload):
    try:
      data = request.get_json()
      name = data['name']
      age = data['age']
      gender = data['gender']
      actor = Actor(name=name, age=age, gender=gender)
      db.session.add(actor)
      db.session.commit()
      return jsonify({'success': True})
    except:
      abort(400)

  # Update an existing actor
  @app.route('/actors/<int:id>', methods=['PATCH'])
  @requires_auth("edit:actor")
  def update_actor(payload, id):
    try:
      data = request.get_json()
      actor = Actor.query.get(id)
      if 'name' in data:
        actor.name = data['name']
      if 'age' in data:
        actor.age = data['age']
      if 'gender' in data:
        actor.gender = data['gender']
      db.session.commit()
      return jsonify({'success': True})
    except:
            abort(404)

  # Delete an actor
  @app.route('/actors/<int:id>', methods=['DELETE'])
  @requires_auth("delete:actor")
  def delete_actor(payload, id):
    try:
      actor = Actor.query.get(id)
      db.session.delete(actor)
      db.session.commit()
      return jsonify({'success': True})
    except:
      abort(404)

    #  Movies
  #  ----------------------------------------------------------------

  # Get a list of all movies

  @app.route('/movies')
  @requires_auth('get:movies')
  def get_movies(payload):
    all_movies = Movie.query.all()
    if not all_movies:
      abort(404)
    movie_list = [{'title': movie.title, 'release_date': movie.release_date} for movie in all_movies]
    return jsonify({'success': True, 'movies': movie_list})

  # Create a new movie
  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def create_movie(payload):
    data = request.get_json()
    title = data.get('title')
    release_date = data.get('release_date')
    if not title or not release_date:
      abort(400)
    movie = Movie(title=title, release_date=release_date)
    db.session.add(movie)
    db.session.commit()
    return jsonify({'success': True, 'movie': {'title': movie.title, 'release_date': movie.release_date}})

  # Update an existing movie
  @app.route('/movies/<int:id>', methods=['PATCH'])
  @requires_auth('edit:movie')
  def update_movie(payload, id):
    data = request.get_json()
    movie = Movie.query.get(id)
    if not movie:
      abort(404)
    if 'title' in data:
      movie.title = data['title']
    if 'release_date' in data:
      movie.release_date = data['release_date']
    db.session.commit()
    return jsonify({'success': True, 'movie': {'title': movie.title, 'release_date': movie.release_date}})

  # Delete a movie
  @app.route('/movies/<int:id>', methods=['DELETE'])
  @requires_auth('delete:movie')
  def delete_movie(payload, id):
    movie = Movie.query.get(id)
    if not movie:
      abort(404)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({'success': True})

  # Error handling
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({'success': False, 'error': 400, 'message': 'Bad request'}), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({'success': False, 'error': 404, 'message': 'Resource not found'}), 404

  @app.errorhandler(422)
  def unprocessable_entity(error):
    return jsonify({'success': False, 'error': 422, 'message': 'Unprocessable entity'}), 422


  @app.errorhandler(500)
  def internal_server_error(error):
    return jsonify({'success': False, 'error': 500, 'message': 'Internal Server Error'}), 500



  return app

app = create_app()
migrate = Migrate(app= app, db= db)




if __name__ == '__main__':
  application.run()

# if __name__ == '__main__':
#   APP.run(host='0.0.0.0', port=8080, debug=True)

# FLASK_APP=app.py FLASK_DEBUG=true flask run