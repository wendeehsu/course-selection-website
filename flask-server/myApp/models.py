from myApp import db
import enum
import json

# Database schema:
# https://dbdiagram.io/d/639cae0f99cb1f3b55a1e7e4

class Track:
    def __init__(self,obj):
        self.id = obj.id
        self.name = obj.name
    
    def toObject(self):
        return {'id':self.id, 'name': self.name}

class Course:
    def __init__(self,obj):
        self.id = obj.id
        self.name = obj.name
        self.code = obj.code
        self.semester = obj.semester
        self.weekday = self.getWeekday(obj.weekday)
        self.level = self.courseLevel(obj.level)
        self.timeslot_start = self.getTime(obj.timeslot_start)
        self.timeslot_end = self.getTime(obj.timeslot_end)
        self.overview = obj.overview
        self.location = obj.location
        self.mode = self.getMode(obj.mode)
        self.instructor = {'id': obj.instructor_id, 'name': obj.instructor_name}

    def getTime(self,value):
        if value == None:
            return None
        return json.dumps(value, default=str).replace('\"','')

    def courseLevel(self,value):
        dic = {'1':'Beginner', '2':'Intermediate', '3': 'Advanced'}
        return dic[str(value)]
    
    def getWeekday(self,value):
        if value == None:
            return value
        dic = {'1':'Monday', '2':'Tuesday', '3':'Wednesday',\
                '4':'Thursday','5':'Friday'}
        return dic[str(value)]
    
    def getMode(self,value):
        dic = {'1':'In-Person', '2':'Hybrid', '3':'Online'}
        return dic[str(value)]

    def toObject(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'semester': self.semester,
            'weekday': self.weekday,
            'level': self.level,
            'timeslot_start': self.timeslot_start,
            'timeslot_end': self.timeslot_end,
            'overview': self.overview,
            'location': self.location,
            'mode': self.mode,
            'instructor': self.instructor
        }
