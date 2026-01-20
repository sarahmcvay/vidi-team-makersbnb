from lib.user import User

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
    
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * FROM users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["name"], row["email"], row["password"])
    
    def create(self, user):
        rows = self._connection.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id', [
            user.name, user.email, user.password])
        row = rows[0]
        user.id = row["id"]
        return user