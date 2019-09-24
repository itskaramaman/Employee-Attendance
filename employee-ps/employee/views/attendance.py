from flask import Blueprint, render_template, request, render_template, session, flash
from employee.models import Attendance
from datetime import datetime, date
from employee import db


attendance_bp = Blueprint('attendance_bp', __name__)


# attendance page 
@attendance_bp.route('/attendance')
def attendance():
	return render_template('attendance.html')


# punchin function
@attendance_bp.route('/attendance/punchin')
def punchin():
	result = Attendance.query.filter_by(employee_id = session['id']).filter_by(date = date.today()).first()
	day = date.today().strftime("%A")
	if day == 'Saturday' or day == 'Sunday':
		flash('Today is a Weekoff', 'dark')
		return render_template('attendance.html')
	if result == None:
		new_attendance = Attendance(datetime.utcnow(), datetime.utcnow(), session['id'])
		db.session.add(new_attendance)
		db.session.commit()
		flash('You have just punched in.', 'success')
		return render_template('attendance.html')
	else:
		flash('You have already punched in at '+str(result.punchin), 'info')
		return render_template('attendance.html')	


# punchout function
@attendance_bp.route('/attendance/punchout')
def punchout():
	day = date.today().strftime("%A")
	if day == 'Saturday' or day == 'Sunday':
		flash('Today is a Weekoff', 'dark')
		return render_template('attendance.html')
	result = Attendance.query.filter_by(employee_id=session['id']).filter_by(date=date.today()).first()
	if result != None:
		result.punchout = datetime.utcnow()
		db.session.commit()
		flash('You have punched out successfully at '+str(result.punchout), 'success')
		return render_template('attendance.html')
	else:
		flash('You have not punched in yet', 'warning')
		return render_template('attendance.html')	