from flask import Blueprint, session, flash, redirect, url_for
from employee.views.login_check import is_loggedin

logout_bp = Blueprint('logout_bp', __name__)

@logout_bp.route('/logout')
@is_loggedin
def logout():
	session.clear()
	flash('You have succesfully logged out', 'success')
	return redirect(url_for('login_bp.login'))