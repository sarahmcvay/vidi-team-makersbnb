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
    connection = get_flask_database_connection(app)
    return render_template('index.html')

@app.route('/create_space', methods=['GET'])
def get_create_space():
    return render_template('create_space.html')

@app.route('/create_space', methods=['POST'])
def post_create_space():
    name = request.form["name"]
    details = request.form["details"]
    price = request.form["price"]
    img_link = request.form["img_link"]
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = Space(None, name, price, details, img_link, None)
    repository.create(space)
    return "Space added successfully"

@app.route('/create_booking', methods=['GET'])
def get_create_booking():
    return render_template('create_booking.html')


@app.route('/browsing_spaces', methods=['GET'])
def get_spaces_browsing_page():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all() 
    return render_template('browsing_spaces.html', spaces = spaces)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
