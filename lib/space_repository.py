from lib.space import Space 

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["price"], row["details"], row["img_link"], row["user_id"])
            spaces.append(item)
        return spaces
    
    def create(self, space):
        