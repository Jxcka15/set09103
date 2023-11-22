from flask import Blueprint, render_template, request, jsonify
from extensions import db  # Adjust this import if necessary
from models import leaderboard  # Adjust this import if necessary

views = Blueprint('views', __name__)

@views.route("/home")
def home():
    return render_template("index.html")

@views.route("/leaderboard")
def show_leaderboard():
    top_scores = leaderboard.query.order_by(leaderboard.score.desc()).all()
    return render_template("leaderboard.html", top_scores=top_scores)

@views.route('/submit-score', methods=['POST'])
def submit_score():
    data = request.json
    new_score = leaderboard(name=data['name'], score=data['score'], date=data['date'])
    db.session.add(new_score)
    db.session.commit()
    return jsonify({'message': 'Score submitted successfully'})
