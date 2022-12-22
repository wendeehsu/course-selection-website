from myApp import db
import enum
import json

# Database schema:
# https://dbdiagram.io/d/639cae0f99cb1f3b55a1e7e4

def courseLevel(value):
    if value == 1:
        return 'Beginner'
    if value == 2:
        return 'Intermediate'
    return 'Advanced'

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    code = db.Column(db.String(50))
    semester = db.Column(db.String(50))
    level = db.Column(db.Integer)
    timeslot_start = db.Column(db.Time)
    timeslot_end = db.Column(db.Time)
    weekday = db.Column(db.Integer) # change to enum
    mode = db.Column(db.Integer)    # change to enum
    overview = db.Column(db.String(50))
    location = db.Column(db.String(50))

    def toObject(self):
        return {
            'id': self.id,
            'name': self.name,
            'level': self.level,
            'timeslot_start': json.dumps(self.timeslot_start, default=str).replace('\"',''),
            'timeslot_end': json.dumps(self.timeslot_end, default=str).replace('\"',''),
            'overview': self.overview,
            'location': self.location
        }
