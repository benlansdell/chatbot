"""Flask app for chatbot"""

import ssl
import http.client
from flask import Flask, render_template, request
from flask_cors import CORS
import json

from secrets import *

def create_app():
    """Create the Flask app
            
    Returns:
        The Flask App
    """

    app = Flask(__name__, template_folder='./templates') 
    CORS(app, resources={r"/query/": {"origins": "*"}})
    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/query/', methods = ['POST', 'GET'])
    def query():
        data = "{\"input_params\": \"" + request.json + "\"}"
        conn.request("POST", endpoint, data, headers)
        res = conn.getresponse()
        data = res.read()
        resp = json.loads(data)
        return resp['prediction']

    return app

app = create_app()