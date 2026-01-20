from lib.user import User
from lib.user_repository import UserRepository

'''
Get all users
'''
def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    users = repository.all()
    assert users == [
        User(1, 'test1', 'test1@email.com', 'test1password'),
        User(2, 'test2', 'test2@email.com', 'test2password'),
        User(3, 'test3', 'test3@email.com', 'test3password'),
    ]

'''
Get a single user
'''

def test_get_single_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    user = repository.find(1)

    assert user == User(1, 'test1', 'test1@email.com', 'test1password')

'''
Create new User
'''

def test_create_new_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    user = repository.create(User(None, 'test4', 'test4@email.com', 'test4password'))
    assert user == User(4, 'test4', 'test4@email.com', 'test4password')

    users = repository.all()
    assert users == [
        User(1, 'test1', 'test1@email.com', 'test1password'),
        User(2, 'test2', 'test2@email.com', 'test2password'),
        User(3, 'test3', 'test3@email.com', 'test3password'),
        User(4, 'test4', 'test4@email.com', 'test4password'),
    ]