import pymongo
import time
import datetime
from pymongo import MongoClient # import mongo client to connect
# Creating instance of mongoclient
client = MongoClient("mongodb://localhost:27017/")
# Creating database
db =  client.apiDB
# employee = {"id": "101",
# "name": "Peter",
# "profession": "Software Engineer",
# }
# # Creating document
# employees = db.employees
# # Inserting data
# employees.insert_one(employee)
# # Fetching data
# pprint.pprint(employees.find_one())

def insert_req(method,receive_time,response_time):
    request={
    "method":method,
    "receive_time":receive_time,
    "response_time": response_time
    }
    stats=db.status
    stats.insert_one(request)
    print(stats.find_one())
def get_average_response_time():
    stats=db.status
    getStatsCursor = stats.find({"method": "GET"})
    postStatsCursor = stats.find({"method": "POST"})
    print("get")
    cg=0
    cp=0
    getResponse=0
    postResponse=0
    for getStats in getStatsCursor:
        getResponse+=getStats["response_time"]
        cg+=1
        print(getResponse)
    print(getResponse/cg)
    print("post")
    for postStats in postStatsCursor:
        postResponse+=postStats["response_time"]
        cp+=1
        print(postResponse)
    print(postResponse/cp)
    avg_response_time={
    "GET":getResponse/cg,
    "POST":postResponse/cp
    }
    return avg_response_time

def get_request_details_hourly():
    stats=db.status
    current_time=time.time()
    getStatsCursor = stats.find({"method": "GET"})
    postStatsCursor = stats.find({"method": "POST"})
    print("get")
    cg=0
    cp=0
    getResponse=0
    postResponse=0
    one_hour = datetime.timedelta(hours=1)
    today = datetime.datetime.now()
    for getStats in getStatsCursor:
        print(getStats["receive_time"])
        print(datetime.datetime.strptime(getStats["receive_time"],'%Y-%m-%d %H:%M:%S'))
        req_date=datetime.datetime.strptime(getStats["receive_time"],'%Y-%m-%d %H:%M:%S')
        # print(current_time)
        # print(getStats["receive_time"]-current_time)
        print("times")
        if today-req_date<one_hour:
            getResponse+=getStats["response_time"]
            cg+=1
            print(getResponse)
            print(today-req_date)
    print(getResponse/cg)
    print("post")
    for postStats in postStatsCursor:
        print(postStats["receive_time"])
        # print(current_time)
        req_date=datetime.datetime.strptime(getStats["receive_time"],'%Y-%m-%d %H:%M:%S')
        # print(postStats["receive_time"]-current_time)
        print("times")
        if today-req_date<one_hour:
            postResponse+=postStats["response_time"]
            cp+=1
            print(postResponse)
            print(postResponse/cp)
    avg_response_time_hourly={
    "GET":getResponse/cg,
    "POST":postResponse/cp,
    "#Get":cg,
    "#POST":cp
    }
    return avg_response_time_hourly

def get_request_details_daily():
    stats=db.status
    current_time=time.time()
    getStatsCursor = stats.find({"method": "GET"})
    postStatsCursor = stats.find({"method": "POST"})
    print("get")
    cg=0
    cp=0
    getResponse=0
    postResponse=0
    one_day = datetime.timedelta(days=1)
    today = datetime.datetime.now()
    for getStats in getStatsCursor:
        print(getStats["receive_time"])
        print(datetime.datetime.strptime(getStats["receive_time"],'%Y-%m-%d %H:%M:%S'))
        req_date=datetime.datetime.strptime(getStats["receive_time"],'%Y-%m-%d %H:%M:%S')
        # print(current_time)
        # print(getStats["receive_time"]-current_time)
        print("times")
        if today-req_date<one_day:
            getResponse+=getStats["response_time"]
            cg+=1
            print(getResponse)
            print(today-req_date)
    print(getResponse/cg)
    print("post")
    for postStats in postStatsCursor:
        print(postStats["receive_time"])
        # print(current_time)
        req_date=datetime.datetime.strptime(getStats["receive_time"],'%Y-%m-%d %H:%M:%S')
        # print(postStats["receive_time"]-current_time)
        print("times")
        if today-req_date<one_day:
            postResponse+=postStats["response_time"]
            cp+=1
            print(postResponse)
            print(postResponse/cp)
    avg_response_time_daily={
    "GET":getResponse/cg,
    "POST":postResponse/cp,
    "#Get":cg,
    "#POST":cp
    }
    return avg_response_time_daily
