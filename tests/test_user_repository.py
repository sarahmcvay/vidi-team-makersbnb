from lib.user import User
from lib.user_repository import UserRepository
from werkzeug.security import check_password_hash

'''
Get all users
'''
def test_get_all_users(seed_db):
    repository = UserRepository(seed_db)

    users = repository.all()
    print(users)
    assert len(users) == 3
    assert users[0].name == 'test1'
    assert users[0].email == 'test1@email.com'
    assert check_password_hash(users[0].password, 'test1password')
    assert users[1].name == 'test2'
    assert users[1].email == 'test2@email.com'
    assert check_password_hash(users[1].password, 'test2password')
    assert users[2].name == 'test3'
    assert users[2].email == 'test3@email.com'
    assert check_password_hash(users[2].password, 'test3password')
'''
Get a single user
'''
def test_get_single_user(seed_db):
    repository = UserRepository(seed_db)
    user = repository.find(1)
    assert user.id == 1
    assert user.name == 'test1'
    assert user.email == 'test1@email.com'
'''
Create new User
'''
def test_create_new_user(seed_db):
    repository = UserRepository(seed_db)
    new_user = repository.create(User(None, 'test4', 'test4@email.com', 'test4password'))
    assert new_user.id == 4
    assert new_user.name == 'test4'
    assert new_user.email == 'test4@email.com'
    hashed_user = repository.find(4)
    assert check_password_hash(hashed_user.password, 'test4password')
    assert hashed_user.password != 'test4password'