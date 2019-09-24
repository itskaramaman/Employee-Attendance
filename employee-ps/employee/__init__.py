from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# engine = create_engine('postgresql+psycopg2://murderer:murderer@localhost:5000/testDatabase')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://murderer:murderer@localhost:5432/testDatabase';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'shhhh'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from employee.views import home_bp
app.register_blueprint(home_bp)
from employee.views import register_bp 
app.register_blueprint(register_bp)
from employee.views import login_bp
app.register_blueprint(login_bp)
from employee.views import logout_bp
app.register_blueprint(logout_bp)
from employee.views import attendance_bp
app.register_blueprint(attendance_bp)
from employee.views import profile_bp
app.register_blueprint(profile_bp)