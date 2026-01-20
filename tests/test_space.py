from lib.space import Space

"""
Space constructs with an id, name, cost, description, image link and user id
"""
def test_space_constructs():
    space = Space(1, "Test Name", 100, "Test Description", "Test Link", 2)
    assert space.id == 1
    assert space.name == "Test Name"
    assert space.price == 100.00
    assert space.details == "Test Description"
    assert space.img_link == "Test Link"
    assert space.user_id == 2

"""
We can format spaces to strings nicely
"""
def test_spaces_format_nicely():
    space = Space(1, "Test Name", 100, "Test Description", "Test Link", 2)
    assert str(space) == "Space(1, Test Name, 100, Test Description, Test Link, 2)"
    

"""
We can compare two identical spaces
And have them be equal
"""
def test_spaces_are_equal():
    space1 = Space(1, "Test Name", 100, "Test Description", "Test Link", 2)
    space2 = Space(1, "Test Name", 100, "Test Description", "Test Link", 2)
    assert space1 == space2