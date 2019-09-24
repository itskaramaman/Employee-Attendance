from employee import db
from datetime import datetime, date
from uuid import uuid4

class Attendance(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=uuid4())
    date = db.Column(db.DateTime, default=date.today(), nullable=False)
    punchin = db.Column(db.DateTime)
    punchout = db.Column(db.DateTime)
    employee_id = db.Column(db.String(36), db.ForeignKey('employee.id'), nullable=False)

    def __init__(self, punchin, punchout, employee_id):
        self.punchin = punchin
        self.punchout = punchout
        self.employee_id = employee_id

    def __repr__(self):
        return '<Attendance(id=%s, date="%s", punchin="%s", punchout="%s">' % (
            self.id, self.date, self.punchin, self.punchout)    