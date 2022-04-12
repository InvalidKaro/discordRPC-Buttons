import datetime 
import json

def timestamp(days):
    tod = datetime.datetime.now()
    d = datetime.timedelta(days = days)
    a = tod - d
    timestamp = a.replace(tzinfo=datetime.timezone.utc).timestamp()

    return timestamp

def settings():
    with open("settings.json" , "r") as f:
        ss = json.load(f)

    return ss

def get_id():
    se = settings()
    return se["client-id"]