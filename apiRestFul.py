from flask import Flask
from flask_restful import Api
from resources.routes import initialize_routes
from database.db import initialize_db

app = Flask(__name__)
api = Api(app)  #créé une instance Api

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/API_REST_FLASK'
}

initialize_db(app)  #nous importons le formulaire initialize_db pour initialiser notre db

initialize_routes(api)

app.run()
 
 