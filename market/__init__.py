from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# create db config, a dictionary which access some new key, values from us
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '8e566b1b7c90395f376fd5f8'

# create an instance from sql Alchemy
db = SQLAlchemy(app)

# store passwords as hash passwords in DB
bcrypt = Bcrypt(app)

# manage the app login system
login_manager = LoginManager(app) 

from market import routes