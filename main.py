from flask import Flask
from flask import Response
from flask import request
from datetime import datetime
import time
import ast
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/process/<path_id>', methods = ['GET','POST'])
def api_hello(path_id):
    receive_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    start=time.time()
    dict=request.headers
    headers={}
    body=""
    path="/process/"+path_id
    print(path)
    if request.method== 'GET':
        headers=get_headers_get(dict)
        body="INVALID"
    elif request.method=='POST':
        print(dict['Content-Type'])
        print("content type printed")
        body=get_request_data(request)
        headers=get_headers_post(dict)
    time.sleep(1)#15--30
    duration=time.time()-start
    print(duration)
    data = {
        'method'  : request.method,
        'request-path' : path,
        'headers' : headers,
        'query parameters' : request.args,
        'body':body,
        'time': receive_time,
        'duration': time.strftime("%H:%M:%S", time.gmtime(duration))
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    js =json.dumps(message)
    resp = Response(js, status=404, mimetype='application/json')
    return resp


def get_headers_get(dict):
    headers={
    "Cache-Control":dict['Cache-Control'],
    "User-Agent": dict["User-Agent"],
    "Accept":dict["Accept"],
    "Host":dict["Host"],
    "Accept-Encoding": dict["Accept-Encoding"],
    "Connection": dict["Connection"]
    }
    return headers
def get_headers_post(dict):
    headers={
    "Cache-Control":dict['Cache-Control'],
    "User-Agent": dict["User-Agent"],
    "Content-Type":dict['Content-Type'],
    "Accept":dict["Accept"],
    "Host":dict["Host"],
    "Accept-Encoding": dict["Accept-Encoding"],
    "Connection": dict["Connection"]
    }
    return headers
def get_request_data(request):
    if request.headers['Content-Type'] == 'text/plain':
        print( "Text Message: ")
        msg=str(request.data)
        return msg

    elif request.headers['Content-Type'] == 'application/xml':
        print( "XML Message: ")
        s=str(request.data)
        print(s)
        s1=s.replace("\\r\\n"," ")
        print(s1)
        return s1
    elif request.headers['Content-Type'] == 'text/xml':
        print( "text\XML Message: ")
        s=str(request.data)
        print(s)
        s1=s.replace("\\r\\n"," ")
        print(s1)
        return s1
    elif request.headers['Content-Type'] == 'application/json':
        s= "JSON Message: " + json.dumps(request.json)
        return s
    else:
        return "415 Unsupported Media Type"



if __name__ == '__main__':
       app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
