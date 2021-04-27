#Run pip install flask-blueprint
from flask import Blueprint
candidate = Blueprint('candidate',__name__)

@candidate.route('/can_dashboard')
def can_dashboard():
	return "Candidate Dashboard"