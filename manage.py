# import os
# SECRET_KEY = os.urandom(32)
# # Grabs the folder where the script runs.
# basedir = os.path.abspath(os.path.dirname(__file__))

# # Enable debug mode.
# DEBUG = True

# # Connect to the database
# DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
# DB_USER = os.getenv('DB_USER', 'postgres')
# DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
# DB_NAME = os.getenv('DB_NAME', 'capstone')

# # TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD, DB_HOST, DB_NAME)

# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand

# from app import app
# from models import db

# migrate = Migrate(app, db)
# manager = Manager(app)

# manager.add_command('db', MigrateCommand)

# if __name__ == '__main__':
#     app.run()