import os
from lib.space import Space 
from lib.space_repository import SpaceRepository
from lib.user import User
from lib.user_repository import UserRepository
from flask import Flask, request, render_template, session, redirect
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey" 

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = repository.find(name)

    if user is None:
        return render_template(
            'login.html', 
            error="Invalid email or password"), 401
        
    session['user_id'] = user.id

    return render_template('user_dashboard.html')


@app.route('/create_space', methods=['GET'])
def get_create_space():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login')
    return render_template('create_space.html')

@app.route('/create_space', methods=['POST'])
def post_create_space():

    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login')
    
    name = request.form["name"]
    details = request.form["details"]
    price = request.form["price"]
    img_link = request.form["img_link"]
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = Space(None, name, price, details, img_link, user_id)
    repository.create(space)
    return "Space added successfully"
  
@app.route('/show_space/<int:id>', methods=['GET'])
def show_space(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template('show_space.html', space=space)

@app.route('/create_booking', methods=['GET'])
def get_create_booking():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login')
    
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
