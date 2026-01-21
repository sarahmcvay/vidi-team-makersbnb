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
    
    def find(self, space_id):
        rows = self._connection.execute(
            'SELECT * FROM spaces WHERE id = %s',
            [space_id]
        )
        row = rows[0]
        return Space(
            row["id"],
            row["name"],
            row["price"],
            row["details"],
            row["img_link"],
            row["user_id"]
        )

    
    def create(self, space):
        print("in create function")
        self._connection.execute('INSERT INTO spaces (name, price, details, img_link, user_id) VALUES (%s, %s, %s, %s, %s)', [space.name, space.price, space.details, space.img_link, space.user_id])
        return None
    
    def get_spaces_by_user_id(self, user_id):
        rows = self._connection.execute(
            'SELECT * FROM spaces WHERE user_id = %s',
            [user_id]
        )
        spaces = [] 
        for row in rows:
            item = Space(row["id"], row["name"], row["price"], row["details"], row["img_link"], row["user_id"])
            spaces.append(item)
        return spaces

    def get_space_id_by_user_id(self, user_id):
        rows = self._connection.execute(
            'SELECT id FROM spaces WHERE user_id = %s',
            [user_id]
        )
        space_ids = [] 
        for row in rows:
            space_ids.append(row["id"])
        return space_ids