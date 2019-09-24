from functools import wraps
from flask import flash, session, redirect, url_for

def is_loggedin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized please login', 'danger')
            return redirect(url_for('login_bp.login'))
    return wrap
