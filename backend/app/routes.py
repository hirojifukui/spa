import json

from app import app, db, utils
from app.models import Event

from flask import request, jsonify
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World"


@app.route('/save_event', methods=['GET','POST'])
def save_event():
    test_event = Event(
        name='TEST',
        track='Track1',
        start_time=10,
        end_time=20
    )
    test_event.save()
    return jsonify(test_event.to_json())

@app.route('/add_event', methods=['POST'])
def add_event():
    in_data = request.data
    new_event = json.loads(in_data)

    return json.dumps(utils.event_validation(new_event))

@app.route('/reset_db',methods=['GET'])
def reset_db():
    Event.objects().delete()
    return

@app.route('/get_all_events', methods=['GET'])
def get_all_events():
    events = Event.objects()
    json_data = events.to_json()
    print(type(events))
    print('--------------')
    return json.loads(json_data)

@app.route('/get_today_events', methods=['POST'])
def get_today_events():
    in_data = request.data
    curr_date_obj = json.loads(in_data)
    curr_date_obj['date'] = utils.datetime_to_epoch(curr_date_obj['date'])
    today_events = Event.objects(start_time__gte=curr_date_obj['date'], end_time__lte=curr_date_obj['date'] + utils.DAY_LEN_EPOCH)
    return_dict =[]
    i = 0
    # print(curr_date_obj['date'])
    for event in today_events:
        # print(json.loads(today_events.to_json()))
        if event.start_time > curr_date_obj['date'] and event.end_time < (curr_date_obj['date'] + utils.DAY_LEN_EPOCH):
            return_dict.append(event.to_mongo())
        i += 1
    # print(return_dict)
    # print(json.dumps(return_dict))
    # return json.dumps(return_dict)
    return json.dumps(today_events.to_json())


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response