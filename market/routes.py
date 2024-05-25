from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market import db
from market.forms import RegisterForm


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
                            password = form.password1.data)
         db.session.add(user_to_create)
         db.session.commit()
         return redirect(url_for('market_page'))
    if form.errors != {}:  # if there is no errors from the validations
         for err_msg in form.errors.values():
              flash(f'There is an error creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)