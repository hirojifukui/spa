from datetime import datetime, date

from app import app
from app.models import Event

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DAY_LEN_EPOCH = 86400

def datetime_to_epoch(time, time_format=TIME_FORMAT):
  timestamp = datetime.strptime(str(time), time_format)
  epoch = int(timestamp.timestamp())
  return epoch

def epoch_to_datetime(time: int, time_format=TIME_FORMAT):
  t = datetime.fromtimestamp(time)
  return t.strftime(time_format)

def event_validation(event_dict):
  response_dict = {}
  
  if (event_dict['start_time'] > event_dict['end_time']):
    response_dict['success'] = 'false'
    response_dict['message'] = 'Invalid start or end time'
    return response_dict

  events_in_db = Event.objects(track=event_dict['track'])
  
  for db_event in events_in_db:
    if (event_dict['start_time'] <= db_event.start_time <= event_dict['end_time']) \
    or (event_dict['start_time'] <= db_event.end_time <= event_dict['end_time']) \
    or ((event_dict['start_time'] >= db_event.start_time) and (event_dict['end_time'] <= db_event.end_time)) \
    or ((event_dict['start_time'] <= db_event.start_time) and (event_dict['end_time'] >= db_event.end_time)):
      response_dict['success'] = 'false'
      response_dict['message'] = 'Selected time is in use'
      return response_dict
  response_dict['success'] = 'true'
  response_dict['message'] = 'confirmed'

  new_event = Event(name=event_dict['name'], start_time=event_dict['start_time'], \
                    end_time=event_dict['end_time'], track=event_dict['track'])
  new_event.save()
  return response_dict