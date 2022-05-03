from framework.models import Plant
from api import app, api, db
from flask_restful import Resource
from flask import request
from utils.helpers import convert_list

class PlantResource(Resource):

    def get(self):
        plants = Plant.query.all()
        return convert_list(plants)
