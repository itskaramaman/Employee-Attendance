from wtforms import Form, StringField, TextAreaField, PasswordField, validators

class RegisterationForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=100)])
	email = StringField('Email', [validators.Length(min=1, max=100)])
	address = TextAreaField('Address', [validators.Length(max=500)])
	password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message="Password didn't matched.")])
	confirm = PasswordField('Confirm Password')