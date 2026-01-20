from lib.space import Space
from lib.space_repository import SpaceRepository


def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [
        Space(1, 'space1', 10.00, 'great house', 'http123', 1),
        Space(2, 'space2', 20.00, 'ok house', 'http456', 2),
        Space(3, 'space3', 30.00, 'fun house', 'http789', 3)
    ]


def test_create_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    repository.create(Space(None,'space4', 40.00, 'cool house', 'http668', 4))
    result = repository.all()
    assert result == [
        Space(1, 'space1', 10.00, 'great house', 'http123', 1),
        Space(2, 'space2', 20.00, 'ok house', 'http456', 2),
        Space(3, 'space3', 30.00, 'fun house', 'http789', 3),
        Space(4, 'space4', 40.00, 'cool house', 'http668', 4)
    ]