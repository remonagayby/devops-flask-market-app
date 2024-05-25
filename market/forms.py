from wtforms import Form, StringField, PasswordField, SubmitField

class RegisterForm(Form):
    username = StringField(label='User Name')
    email_address = StringField(label='Email')
    password1 = PasswordField(label='Password')
    password2 = PasswordField(label='Confirm Password')
    submit = SubmitField(label='Create Account')