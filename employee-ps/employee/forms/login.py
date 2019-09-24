from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
	email = StringField('Email', [validators.Length(min=1, max=100)])
	password = PasswordField('Password', [validators.Length(min=1), validators.DataRequired()])