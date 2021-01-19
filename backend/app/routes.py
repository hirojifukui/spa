import json

from app import app, db, utils
from app.models import Event

from flask import request, jsonify

@app.route('/add_event', methods=['POST'])
def add_event():
    in_data = request.data
    new_event = json.loads(in_data)
    return json.dumps(utils.event_validation(new_event))

@app.route('/get_today_events', methods=['GET'])
def get_today_events():
    today = request.args.get('date')
    today_in_epoch = utils.datetime_to_epoch(today)
    today_events = Event.objects(start_time__gte=today_in_epoch, end_time__lte=today_in_epoch + utils.DAY_LEN_EPOCH)
    return_dict = []
    for event in today_events:
        if event.start_time > today_in_epoch and event.end_time < (today_in_epoch + utils.DAY_LEN_EPOCH):
            return_dict.append(event.to_mongo())
    return json.dumps(today_events.to_json())

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello, World"
# @app.route('/save_event', methods=['GET','POST'])
# def save_event():
#     test_event = Event(
#         name='TEST',
#         track='Track1',
#         start_time=10,
#         end_time=20
#     )
#     test_event.save()
#     return jsonify(test_event.to_json())
# @app.route('/reset_db',methods=['GET'])
# def reset_db():
#     Event.objects().delete()
#     return

# @app.route('/get_all_events', methods=['GET'])
# def get_all_events():
#     events = Event.objects()
#     json_data = events.to_json()
#     return json.loads(json_data)