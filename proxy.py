from flask import Flask
from flask import Response
from flask import stream_with_context
from flask import jsonify

import requests
import yaml

with open('settings.yaml', 'r') as f:
    settings = yaml.load(f)

app = Flask(__name__)

class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidAPIUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/<device>/', methods=["GET", "POST"])
@app.route('/<device>/<path>', methods=["GET", "POST"])
def home(device, path = ""):
    
    try:
        device = settings["devices"][device]
    except:
        raise InvalidAPIUsage('This view is gone', status_code=410)
    
    url = device["protocole"] + "://" + device["host"] + "/" + path

    req = requests.get(url, stream = True)
    return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
