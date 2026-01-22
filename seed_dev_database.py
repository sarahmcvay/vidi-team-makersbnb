from lib.database_connection import DatabaseConnection
from werkzeug.security import generate_password_hash

def run_seed(connection):
	connection.seed("seeds/makersbnb.sql")

	users_to_seed = [
	('test1', 'test1@email.com', 'test1password'), 
	('test2', 'test2@email.com', 'test2password'), 
	('test3', 'test3@email.com', 'test3password') ] 

	for name, email, password in users_to_seed: 
		hashed_password = generate_password_hash(password) 
		connection.execute( 'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', [name, email, hashed_password] )

if __name__ == '__main__':
	connection = DatabaseConnection(test_mode=False)
	connection.connect()
	run_seed(connection)
