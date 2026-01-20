from lib.user import User

"""
User constructs with an id, name, email and password
"""
def test_user_constructs():
    user = User(1, "Test User", "Test Email", "Test Password")
    assert user.id == 1
    assert user.name == "Test User"
    assert user.email == "Test Email"
    assert user.password == "Test Password"

"""
We can format users to strings nicely
"""
def test_users_format_nicely():
    user = User(1, "Test User", "Test Email", "Test Password")
    assert str(user) == "User(1, Test User, Test Email, Test Password)"

"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Test User", "Test Email", "Test Password")
    user2 = User(1, "Test User", "Test Email", "Test Password")
    assert user1 == user2