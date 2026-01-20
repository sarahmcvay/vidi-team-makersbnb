class Space:
    def __init__(self, id, name, price, description, img_link, user_id):
        self.id = id 
        self.name = name
        self.price = price
        self.description = description
        self.img_link = img_link
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.price}, {self.description}, {self.img_link}, {self.user_id})"
    

