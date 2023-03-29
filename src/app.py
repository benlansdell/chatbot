"""Flask app for chatbot"""

#############
## Imports ##
#############

from flask import Flask, render_template
from flask_cors import CORS

def create_app():
    """Create the Flask app
            
    Returns:
        The Flask App
    """

    app = Flask(__name__, template_folder='./templates') 
    CORS(app)

    @app.route('/')
    def index():

        return render_template('index.html')

    return app

app = create_app()