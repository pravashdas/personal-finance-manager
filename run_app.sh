#!/bin/bash

# Export the Flask application environment variable
export FLASK_APP=app.py

# Run the Flask application
flask run --host=0.0.0.0
