import json

def create_simple_meeting(subject, startDate, endDate, location, body):
    info = dict()
    if(subject != ""):
        info["subject"] = subject
    if(startDate != ""):
        info["startDate"] = startDate
    if(endDate != ""):
        info["endDate"] = endDate
    if(body != ""):
        info["body"] = body
    if(location != ""):
        info["location"] = location
    print(json.dumps(info))