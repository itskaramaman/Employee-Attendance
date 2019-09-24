from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from employee.forms.register import RegisterationForm
from employee import db
from employee.models.employee import Employee

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterationForm(request.form)
	if request.method == 'POST' and form.validate():
		name = request.form['name']
		email = request.form['email']
		address = request.form['address']
		password = request.form['password']
		new_emp = Employee(name, email, address, password)
		db.session.add(new_emp)
		db.session.commit()
		flash('You have been successfully registered', 'success')
		return redirect(url_for('home_bp.home'))
	return render_template('register.html',form=form)	
