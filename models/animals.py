class Animal:
    """Animal class
    """
    def __init__(self, id, name, breed, status, location_id, customer_id=None):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id
        self.location = None


new_animal = Animal(id=1, name="Snickers", breed="Dog",
                 location_id=4, status="Recreation")
print(new_animal.id)
