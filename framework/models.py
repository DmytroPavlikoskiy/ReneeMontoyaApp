from Zalypa.app import db


class Employees(db.Model):
    def __init__(self, name, email, department_type, department_id):
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id

    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    department_type = db.Column(db.String(255), nullable=False)
    department_id = db.Column(db.Integer, nullable=False)

class Plant(db.Model):
    __tablename__ = "plants"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    direction_id = db.Column(db.Integer, nullable=False)


class Salon(db.Model):
    __tablename__ = 'salons'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    name_salon = db.Column(db.String(255), nullable=False)

