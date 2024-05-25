from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market import db
from market.forms import RegisterForm, LoginForm
from flask_login import login_user

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
        items = Item.query.all()
        return render_template('market.html', items=items)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
         user_to_create = User(user_name = form.username.data,
                            email_address = form.email_address.data,
                            password_hash = form.password1.data)
         db.session.add(user_to_create)
         db.session.commit()
         return redirect(url_for('market_page'))
    if form.errors != {}:  # if there is no errors from the validations
         for err_msg in form.errors.values():
              flash(f'There is an error creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login_page():
     form = LoginForm()
     # check if the username & password are exists
     if form.validate_on_submit():
          attempt_user = User.query.filter_by(user_name=form.username.data).first()
          if attempt_user and attempt_user.check_password_correction(
               attempt_password = form.password.data
          ):
               login_user(attempt_user)
               flash(f'Success! Welcome {attempt_user.user_name}', category='success')
               return redirect(url_for('market_page'))
          else:
               flash('Invalid User Name or Password', category='danger')
     return render_template('login.html', form=form)