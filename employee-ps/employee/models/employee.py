from employee import db
from uuid import uuid4
from employee.models.attendance import Attendance
from passlib.hash import sha256_crypt

class Employee(db.Model):
	id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), nullable=False)
	address = db.Column(db.String(500))
	attendance = db.relationship('Attendance', backref='employee', lazy=True)
	password = db.Column(db.String(100), nullable=False)
    

	def __init__(self,name, email, address, password):
		self.name = name
		self.email = email
		self.address = address
		self.password = sha256_crypt.hash(password)

	def __repr__(self):
		return "<Employee(id=%s, name='%s', email='%s', address='%s, password=%s)>" % (
            self.id, self.name, self.email, self.address, self.password)	
