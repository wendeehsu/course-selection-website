from myApp import app, db
import json
from myApp.models import Track, Course

@app.route("/track")
def track():
    data = []
    query = db.engine.execute('SELECT * FROM track')
    for i in query:
        data += [Track(i).toObject()]

    return data

@app.route("/course")
def course():
    data = []
    query = db.engine.execute("""
        SELECT a.*,c.id as instructor_id,c.name as instructor_name
        FROM course a
        LEFT JOIN instructor_course b on a.id=b.course_id
        LEFT JOIN instructor c on b.instructor_id=c.id
    """)
    for i in query:
        data += [Course(i).toObject()]

    return data