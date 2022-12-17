from myApp import app, db
from myApp.models import Track

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