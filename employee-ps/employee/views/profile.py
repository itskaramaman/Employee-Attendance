from flask import Blueprint, render_template, session
from employee.models import Employee

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/profile')
def profile():
	emp = Employee.query.filter_by(id=session['id']).first()
	return render_template('profile.html', emp=emp)