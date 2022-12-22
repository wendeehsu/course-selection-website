from myApp import app, db
import json
from myApp.models import Track, Course

@app.route("/track")
def track():
    data = []
    for row in Track.query.all():
        data += [{
            'id': row.id,
            'name': row.name
        }]
    
    return data

@app.route("/course")
def course():
    data = []
    for row in Course.query.all():
        print(row)
        data += [row.toObject()]

    return data