from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from employee.forms import LoginForm
from employee.models import Employee

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		email_credential = request.form['email']
		password_credential = request.form['password']
		result =  Employee.query.filter_by(email=email_credential).first()
		if result == None:
			flash('Wrong Credentials', 'danger')
			return redirect(url_for('login_bp.login'))
		else:
			if password_credential != result.password:
				flash('Wrong Credentials', 'danger')
				return redirect(url_for('login_bp.login'))
			else:
				session['logged_in'] = True
				session['name'] = result.name
				session['id'] = result.id
				flash('Welcome, '+session['name'], 'success')		
				return redirect(url_for('home_bp.home'))
	return render_template('login.html', form = form)	
