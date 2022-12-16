from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/course_selection"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route("/track")
def course():
    print("result")
    data = []

    for row in Track.query.all():
        data += [{
            'id': row.id,
            'name': row.name
        }]
    
    return data


if __name__ == "__main__":
    app.run(debug=True)