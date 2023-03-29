"""Flask app for chatbot"""

import ssl
import http.client
from flask import Flask, render_template, request
from flask_cors import CORS
import json

conn = http.client.HTTPSConnection("biogpt-1.cnvrg.stjude.org", 
                                   443, 
                                   context = ssl._create_unverified_context())

headers = {
    'Cnvrg-Api-Key': "4PFwBVg5GF3gUXZwcSPM3LPA",
    'Content-Type': "application/json"
    }

endpoint = "/api/v1/endpoints/j8zxksukv8slkbu3pfzo"

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