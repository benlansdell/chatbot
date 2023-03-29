# Start a flask web server running the search API.
#
# Only use for development purposes
# Use gunicorn for production

FLASK_APP=src/app FLASK_ENV=development FLASK_RUN_PORT=8765 flask run --host 0.0.0.0