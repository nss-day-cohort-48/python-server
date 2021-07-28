class Animal:
    """Animal class
    """
    def __init__(self, id, name, breed, status, location_id):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = location_id
        self.customers = []
        self.location = None
