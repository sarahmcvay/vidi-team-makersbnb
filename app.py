import os
from lib.space import Space 
from lib.space_repository import SpaceRepository
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/create_space', methods=['GET'])
def get_create_space():
    return render_template('create_space.html')

@app.route('/create_space', methods=['POST'])
def post_create_space():
    space_name = request.form["space_name"]
    space_description = request.form["space_description"]
    cost_per_night = request.form["cost_per_night"]
    img_link = request.form["img_link"]
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = Space(None, space_name, cost_per_night, space_description, img_link, None)
    repository.create(space)
    return "Space added successfully"



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
