import os
from lib.space import Space 
from lib.space_repository import SpaceRepository
from lib.user import User
from lib.user_repository import UserRepository
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
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template('show_space.html', space=space)

@app.route('/create_booking', methods=['GET'])
@login_required
def get_create_booking():
    return render_template('create_booking.html')

@app.route('/browsing_spaces', methods=['GET'])
@login_required
def get_spaces_browsing_page():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all() 
    return render_template('browsing_spaces.html', spaces = spaces)

@app.route('/user_dashboard', methods=['GET'])
@login_required
def get_user_dashboard():
    return render_template('user_dashboard.html')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
