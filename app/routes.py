from app import app
from app import config
from app.error import InvalidUsage
from flask import stream_with_context
from flask import Response
from flask import request
import requests

@app.route('/<device>/', methods=["GET", "POST"])
@app.route('/<device>/<path>', methods=["GET", "POST"])
def home(device, path = ""):
    
    try:
        device = config.DEVICES[device]
    except:
        raise InvalidUsage('This view is gone', status_code=410)
    
    url = device["protocole"] + "://" + device["host"] + "/" + path

    query = request.args.items()

    req = requests.get(url, params=query, stream = True)
    return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
