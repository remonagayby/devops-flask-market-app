from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create db config, a dictionary which access some new key, values from us
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# create an instance from sql Alchemy
db = SQLAlchemy(app)

from market import routes