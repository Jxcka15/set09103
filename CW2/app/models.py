from extensions import db

class leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    score = db.Column(db.Integer)
    date = db.Column(db.String(10))
