import os
from lib.space import Space 
from lib.space_repository import SpaceRepository
from lib.user import User
from lib.user_repository import UserRepository
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
from functools import wraps 



app = Flask(__name__)
app.secret_key = "supersecretkey" 


def login_required(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return redirect('/login')
        return route(*args, **kwargs)
    return wrapper


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
    user = repository.login(name)

    if user is None:
        return render_template(
            'login.html', 
            error="Invalid email or password"), 401
        
    session['user_id'] = user.id

    return render_template('user_dashboard.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear() 
    return redirect(url_for('login_form')) 

@app.route('/create_space', methods=['GET'])
@login_required
def get_create_space():

    return render_template('create_space.html')

@app.route('/create_space', methods=['POST'])
@login_required
def post_create_space():

    user_id = session.get('user_id')

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
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template('show_space.html', space=space, user_id = user_id)

@app.route('/browsing_spaces', methods=['GET'])
@login_required
def get_spaces_browsing_page():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all() 
    return render_template('browsing_spaces.html', spaces = spaces)

@app.route('/booking_requested', methods=['POST'])
@login_required
def create_booking_request():
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    flag = request.form["flag"] 
    user_id = request.form["user_id"]
    space_id = request.form["space_id"]

    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)
    booking = Booking(None, start_date, end_date, flag, user_id, space_id)
    requested_booking = repository.create(booking)
    return redirect(f"/booking_requested/{requested_booking.id}")

@app.route('/booking_requested/<int:booking_id>', methods=['GET'])
@login_required
def get_booking_requested_page(booking_id):
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    booking_requested = booking_repository.find(booking_id)
    space_repository = SpaceRepository(connection)
    space_requested = space_repository.find(booking_requested.space_id)
    return render_template('booking_requested.html', booking_requested = booking_requested, space_requested = space_requested)


@app.route('/user_dashboard', methods=['GET'])
@login_required
def get_user_dashboard():
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.get_spaces_by_user_id(user_id)
    return render_template('user_dashboard.html', spaces=spaces)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
