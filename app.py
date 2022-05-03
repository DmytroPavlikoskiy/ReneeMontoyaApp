from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from routs.add_routs import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Dominikpavlikovskiy375@localhost/dbEPS'
db = SQLAlchemy(app)
db.init_app(app)
api = Api(app)

with app.app_context():
    from routs.add_routs import *
    from framework.models import *
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
