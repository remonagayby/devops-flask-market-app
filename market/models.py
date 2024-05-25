from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
      id = db.Column(db.Integer(), primary_key=True)
      user_name = db.Column(db.String(length=30), nullable=False, unique=True)
      email_address = db.Column(db.String(length=50), nullable=False, unique=True)
      password = db.Column(db.String(length=60), nullable=False)
      budget = db.Column(db.Integer(), nullable=False, default=1000)
      items = db.relationship('Item', backref='owned_user', lazy=True)

      @property
      def prettier_budget(self):
            if len(str(self.budget)) >= 4:
                  return "${:,.2f}".format(self.budget)
            else:
                  return f'${self.budget}'

      @property
      def password_hash(self):
            return self.password_hash

      @password_hash.setter
      def password_hash(self, password_plain_text):
            self.password = bcrypt.generate_password_hash(password_plain_text).decode('utf-8')

      def check_password_correction(self, attempt_password):
            return bcrypt.check_password_hash(self.password, attempt_password)


class Item(db.Model):
      id = db.Column(db.Integer(), primary_key=True)
      name = db.Column(db.String(length=30), nullable=False, unique = True)
      price = db.Column(db.Integer(), nullable=False) 
      barcode = db.Column(db.String(length=12), nullable=False, unique = True)
      description= db.Column(db.String(length=1024), nullable=False, unique = True)
      owner = db.Column(db.Integer(), db.ForeignKey('user.id'))


      def __repr__(self):
            return f'Item {self.name}'