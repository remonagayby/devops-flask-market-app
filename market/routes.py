from market import app
from flask import render_template, redirect, url_for, flash, request, Flask, jsonify
from visits import load_visits, save_visits  # Importing load_visits and save_visits from visits.py
from market.models import Item, User
from market import db
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home_page():
    increment_visits()
    return render_template('home.html')

@app.route("/market", methods=['GET', 'POST'])
@login_required
def market_page():
        purchase_form = PurchaseItemForm()
        sell_form = SellItemForm()
        # purchase item logic
        if request.method == 'POST':
          purchased_item = request.form.get('purchased_item')
          p_item_object = Item.query.filter_by(name=purchased_item).first()
          if current_user.can_purchase(p_item_object):
               p_item_object.buy(current_user)
               flash(f'Congratulations! You\'ve purchased {p_item_object.name} for {p_item_object.price}$')
          else:
               flash(f'Unfortunately! You don\'t have enough money to purchase {p_item_object.name}')
          
        # sell item logic
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
          if current_user.can_sell(s_item_object):
               s_item_object.sell(current_user)
               flash(f'Congratulations! You\'ve sold {p_item_object.name} back to market')
          else:
               flash(f'Something went wrong with selling {s_item_object.name}', category='danger')


          return redirect(url_for('market_page'))
                     
        if request.method == 'GET':
          items = Item.query.filter_by(owner=None)
          owned_items = Item.query.filter_by(owner=current_user.id)
          return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, sell_form=sell_form)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
         user_to_create = User(user_name = form.username.data,
                            email_address = form.email_address.data,
                            password_hash = form.password1.data)
         db.session.add(user_to_create)
         db.session.commit()
         login_user(user_to_create)
         flash(f'Account Created Successfully!, You\'re Now Logged in as {user_to_create.user_name}', category='success')
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

@app.route('/visits')
def get_visits():
    visits = load_visits()
    return jsonify({'visits': visits})

def increment_visits():
    visits = load_visits()
    visits += 1
    save_visits(visits)
    return jsonify({'message': 'Visits incremented successfully!'})
