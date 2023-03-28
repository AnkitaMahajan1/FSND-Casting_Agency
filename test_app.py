import os
import json
import unittest
from app import create_app
from models import db, Actor, Movie, setup_db
from flask_sqlalchemy import SQLAlchemy


class ActorTestCase(unittest.TestCase):
    def setUp(self):
        self.director_token = os.environ['director_token']
        self.assistant_token = os.environ['assistant_token']
        self.executive_token = os.environ['executive_producer_token']
        self.app = create_app()
        self.client = self.app.test_client
        # setup_db(self.app)

        self.new_actor = {'name': 'Jane Doe', 'age': 30, 'gender': 'Female'}
        self.invalid_actor = {'name': '', 'age': 25, 'gender': 'Female'}     

    def tearDown(self):
        pass
    #get request test using director token
    def test_get_actors(self):
        response = self.client().get('/actors', headers={
            'Authorization': "Bearer {}".format(self.director_token)
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data) > 0)
    #get request test using assistant token
    def test_get_actors(self):
        response = self.client().get('/actors', headers={
            'Authorization': "Bearer {}".format(self.assistant_token)
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data) > 0)
    #post request test using director token
    def test_create_actor(self):
        response = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(self.director_token)
        }, json=self.new_actor)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
    #post request test using assistant token
    def test_create_actor_failure(self):
        data = {}
        response = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(self.assistant_token)
        }, json=self.new_actor)
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.json['success'])

    def test_update_actor(self):
        actor = Actor(name='Jane Doe', age=25, gender='Female')
        db.session.add(actor)
        db.session.commit()
        response = self.client.patch(f'/actors/{actor.id}', json={'name': 'Janet Doe'}, headers={
            'Authorization': "Bearer {}".format(self.executive_token)
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_update_actor_not_found(self):
        response = self.client.patch('/actors/999', json={'name': 'Janet Doe'}, headers={
            'Authorization': "Bearer {}".format(self.assistant_token)
        },)
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertFalse(data['success'])

    def test_delete_actor(self):
        actor = Actor(name='John Smith', age=40, gender='Male')
        db.session.add(actor)
        db.session.commit()
        response = self.client.delete(f'/actors/{actor.id}', headers={
            'Authorization': "Bearer {}".format(self.executive_token)
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_delete_actor_not_found(self):
        response = self.client.delete('/actors/999', headers={
            'Authorization': "Bearer {}".format(self.director_token)
        },)
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertFalse(data['success'])

class TestMoviesEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db
        self.db.create_all()
        self.movie = Movie(title="Test Movie", release_date="2022-01-01")
        self.db.session.add(self.movie)
        self.db.session.commit()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_get_movies_success(self):
        response = self.app.get('/movies')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])
        self.assertGreater(len(response.json['movies']), 0)

    def test_get_movies_failure(self):
        self.db.session.delete(self.movie)
        self.db.session.commit()
        response = self.app.get('/movies')
        self.assertEqual(response.status_code, 404)
        self.assertFalse(response.json['success'])

    def test_create_movie_success(self):
        data = {"title": "New Movie", "release_date": "2023-04-01"}
        response = self.app.post('/movies', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])
        self.assertIsNotNone(response.json['movie']['title'])
        self.assertIsNotNone(response.json['movie']['release_date'])

    def test_create_movie_failure(self):
        data = {"title": "New Movie"}
        response = self.app.post('/movies', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.json['success'])

    def test_update_movie_success(self):
        data = {"title": "Updated Movie"}
        response = self.app.patch(f'/movies/{self.movie.id}', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])
        self.assertEqual(response.json['movie']['title'], "Updated Movie")

    def test_update_movie_failure(self):
        response = self.app.patch('/movies/1000')
        self.assertEqual(response.status_code, 404)
        self.assertFalse(response.json['success'])

    def test_delete_movie_success(self):
        response = self.app.delete(f'/movies/{self.movie.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_delete_movie_failure(self):
        response = self.app.delete('/movies/1000')
        self.assertEqual(response.status_code, 404)
        self.assertFalse(response.json['success'])


if __name__ == '__main__':
    unittest.main()