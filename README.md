Casting Agency Specifications

The Casting Agency is a company that creates movies and manages actors by assigning them to these movies. As an Executive Producer within the company, you are developing a system to simplify and streamline the process.

Motivation for the Project

The goal of this project is to demonstrate proficiency in using Flask, SQLAlchemy, Auth0, gunicorn, and Heroku to develop and deploy a RESTful API. This project serves as the capstone project for the Udacity Full Stack Nanodegree program.

Getting Started

Installing Dependencies

To get started, you'll need to install Python 3.7. Follow the instructions in the Python documentation to install the latest version of Python for your platform.

Virtual Environment

We recommend using a virtual environment when working with Python projects. This keeps your dependencies separate and organized for each project. Instructions for setting up a virtual environment for your platform can be found in the Python documentation.

PIP Dependencies

Once you have set up your virtual environment, then run the following command:

pip install -r requirements.txt

This command installs all the required packages listed in the requirements.txt file.

Key Dependencies

Flask is a lightweight backend microservices framework used to handle requests and responses.

SQLAlchemy is the Python SQL toolkit and ORM used to manage the lightweight SQLite database. You'll mainly work in app.py and reference models.py.

Flask-CORS is an extension used to handle cross-origin requests from the frontend server.

Running the server
To run the server, execute:

flask run

Project deployed at

--url
To test live APIs the only way right now to do this is curl requests. Add Auth token headers from logins below to test.
OATH login url. There are three logins, JWTs for these appear in the url after successfull login. Those tokens are needed to test the different APIs.

https://dev-8w8jzycn5qmrkfp0.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=PBtNJiAXuBp5pW7sPAIVTTIBwiGNq7QE&redirect_uri=https://127.0.0.1:5000/actors

casting Assistant token 

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilg1eGtTYnNqSkJxVnZkd3ZwSHU1MSJ9.eyJpc3MiOiJodHRwczovL2Rldi04dzhqenljbjVxbXJrZnAwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDA0NjQ4ZWYzNGQyYzJhMmM2NzdlMDMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY3OTkyODg2NCwiZXhwIjoxNjc5OTM2MDY0LCJhenAiOiJQQnROSmlBWHVCcDVwVzdzUEFJVlRUSUJ3aUdOcTdRRSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.C017jABMYXX1pZr7SNcI_o1umh6sPMaFPlI320szNP-132He_eU9Mzy82Yg6qjwHLgUAgpv1tCGq563zwaFpMeZ4T00RaxvrQWKtfKyZ8txdUpnmYCOMBIju6MsSFEeC-ziVB_s-NC50oOwc8kgtOscthprz4IE9yE72T5JmxwreJj5St09NRaMwU9K2h41Jw3a1BUEwUFyPzvB_t__UyXYxAX-_SoM-f7AYTHX_tsZIpkiVybd5f4W6S2uEPKxadW2SeTMnoP2WFhz5JhA3K2SMlcmn7z8Sc2d19N9f5lFLiQMYM1aHkRIt70hCgF48n4z5ctpOp_dYmi2j6nxZ9g

Casting director token 

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilg1eGtTYnNqSkJxVnZkd3ZwSHU1MSJ9.eyJpc3MiOiJodHRwczovL2Rldi04dzhqenljbjVxbXJrZnAwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDA0NjQ4ZWYzNGQyYzJhMmM2NzdlMDMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY3OTkyOTAyNywiZXhwIjoxNjc5OTM2MjI3LCJhenAiOiJQQnROSmlBWHVCcDVwVzdzUEFJVlRUSUJ3aUdOcTdRRSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZWRpdDphY3RvciIsImVkaXQ6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIl19.WVd9_JX5wErq2AXf34l24FWz4BLUcvk1MpIkSpH-Qq_T5y4CAuW8vXF5nc8qL7Pfqe5B8QufGoVyboQhQelIGIpCwngPinxqffci9tC5mGl8lbhtnmWfvBk0htlsPHEzOE2StVpOcDXDTVagqquX9pGSRLMMbMmN8ByRwnxmMF34TM80AWMzX4e3N3l9VZFaB-XLXvG0ReUn9HahqHBNvzBjgjWE07aVOHxTwsy4r2IkH5BHo0LF3K36v4LBPxacrePOeaqDr6Iez72cCVtvbdWJoGV-pfrgHeYqO_U_UgQUrxsYQNDUICa__dM5IEmFOookCHn0diq0Wi7GOptVNA

Executive Producer 

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilg1eGtTYnNqSkJxVnZkd3ZwSHU1MSJ9.eyJpc3MiOiJodHRwczovL2Rldi04dzhqenljbjVxbXJrZnAwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDA0NjQ4ZWYzNGQyYzJhMmM2NzdlMDMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY3OTkyNDcxNiwiZXhwIjoxNjc5OTMxOTE2LCJhenAiOiJQQnROSmlBWHVCcDVwVzdzUEFJVlRUSUJ3aUdOcTdRRSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZWRpdDphY3RvciIsImVkaXQ6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.u88oYcw0N6E_yZXKdCAEbuDPb5aqOMW57ZlSIiBr-iela7FRKqvmr1u5-3QbTTEd6wazLDff0TeUp_8mPCPN5Or2aeUwVr-Gn-s4TsgD8v3Q0zKMhCZRJN6-qlMeGLgG2g_PM4UZaOzb1YXGWzEK0pZAecbAUla4kzSxA5U7e0w7DCT3n7G2_D9b4ob24t_IuWxMq0CtGPLa9az3jb34ZpzHWytVgrisjrNAbRlDtiUOWdHyPSyDdYae2tQxLc7Y5qLdZcwnMwMdbgofvZhstgdGH6u9-3jAboT2omN24IGQaKN3qI9IZ2QT7yC1pTGOys3YSUPUqe8U2Q6efFQNBA

Testing
To run the tests, run


python test_app.py
The tests print data returned from the APIs.

The rests also use the Auth token set in env variables and will give an error if the tokens are expired.

API Reference
Error Handling
Errors are returned as JSON objects in the following format:

{
    'success': False,
    'error': 500, 
    'message': 'Internal Server Error'
}

Endpoints
GET '/actors' POST '/actors' PATCH '/actors/<actor_id>' DELETE '/actors/<actor_id>' GET '/movies' POST '/movies' PATCH '/movies/<movie_id>' DELETE '/movies/<movie_id>'

GET '/movies' Fetches list of movies 
Required URL Arguments: None 
Required Data Arguments: None 
Returns: Returns Json data about movies Success Response:

{
   "movies":[
      {
         "release_date":"2020-08-09",
         "title":"Inception"
      },
      {
         "release_date":"2020-01-09",
         "title":"Endgame"
      }
   ]
}
GET '/actors' Fetches list of actors 
Required Data Arguments: None 
Returns: Json data about actors
Success Response:

  {
   "actors":[
      {
        "name":"John Deo",
         "age":32,
         "gender":"Male"
         
      }
   ]
}
DELETE '/movies/int:movie_id' Deletes the movie 
Required URL Arguments: movie_id: movie_id_integer 
Required Data Arguments: None 
Returns: deleted movie's ID Success Response:{'success': True}

DELETE '/actors/int:id' Deletes the actor 
Required URL Arguments: id: actor_id 
Required Data Arguments: None 
Returns:the deleted actor's ID Success Response:{'success': True}

POST '/movies' Post a new movie in a database. 
Required URL Arguments: None Required 
Data Arguments: Json data 
Success Response:{'success': True}

POST '/actors' Post a new actor in a database.
Required URL Arguments: None
Required Data Arguments: Json data
Success Response:{'success': True}

PATCH '/movies/int:movie_id' Updates the movie
Required URL Arguments: movie_id: movie_id 
Required Data Arguments: Json data in body to patch
Returns: Json data about the updated movie Success Response:

{
   "movie":{
      "release_date":"2020-09-08",
      "title":"Endgame"
   },
   "success":True
}
PATCH '/actors/int:actor_id' Updates the actor_id of actor 
Required URL Arguments: actor_id: actor_id_integer 
Required Data Arguments: In JSON body add the values to update 
Returns: Json data about the modified actor's ID Success Response:

{
   "actor":{
      "age":29,
      "gender":"M",
      "name":"howard"
   },
   "success":True
}
Authors: Ankita Mahajan and the Udacity team responsible for developing the starter code and project tasks.