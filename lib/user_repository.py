from lib.user import User
from werkzeug.security import generate_password_hash, check_password_hash


class UserRepository:
    def __init__(self, conection):
        self._connection = conection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["id"], row["name"], row["email"], row["password"])
            users.append(item)
        return users
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * FROM users WHERE id = %s', [id])
        row = rows[0]
        return User(row["id"], row["name"], row["email"], row["password"])
    
    def create(self, user):
        hashed_password = generate_password_hash(user.password)
        rows = self._connection.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id', [
		    user.name, user.email, hashed_password])
        row = rows[0]
        user.id = row["id"]
        return user
    
    def login(self, email, submitted_password):
        rows = self._connection.execute(
		    'SELECT * FROM users WHERE email = %s', [email])
        row = rows[0]
        if check_password_hash(row["password"], submitted_password): 
            return User(row["id"], row["name"], row["email"], row["password"])