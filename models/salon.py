from framework.models import Salon
from api import app, api, db
from flask_restful import Resource
from flask import request
from utils.helpers import convert_list

class PlantResource(Resource):

    def get(self):
        salons = Salon.query.all()
        return convert_list(salons)