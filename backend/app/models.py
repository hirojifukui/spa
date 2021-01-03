from app import app, db

class Event(db.Document):
  name = db.StringField()
  start_time = db.IntField() 
  end_time = db.IntField()
  track = db.StringField()