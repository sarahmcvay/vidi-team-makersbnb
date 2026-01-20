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
        print("in create function")
        self._connection.execute('INSERT INTO spaces (name, price, details, img_link, user_id) VALUES (%s, %s, %s, %s, %s)', [space.name, space.price, space.details, space.img_link, space.user_id])
        return None