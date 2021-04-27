#Run pip install flask-blueprint
from flask import Blueprint
employer = Blueprint('employer',__name__)

@employer.route('/emp_dashboard')
def emp_dashboard():
	return "Employer Dashboard"