import json
from framework.models import Employees
from app import app, api, db
from flask_restful import Resource
from flask import request, Response
from utils.helpers import convert_list


# class EmployeesResource(Resource):
#
#     def get(self):
#         employee = Employees.query.all()
#         return convert_list(employee)
#
#     def post(self):
#         data = request.json
#         employee = Employees(name=data['name'],
#                              email=data['email'],
#                              department_type=data['department_type'],
#                              department_id=int(data['department_id']))
#         db.session.add(employee)
#         db.session.commit()
#         return employee.serialize
#
# api.add_resource('/employees', EmployeesResource)

class EmployeeSingleResource(Resource):
    def get(self, id):
        employee = Employees.query.all(id)
        return employee.serialize

    def delete(self, id):
        employee = Employees.query.get(id)
        db.session.delete(employee)
        db.session.commit()
        return "", 204




