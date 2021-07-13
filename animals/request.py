ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
    }
]


def get_all_animals():
    """Return a list of animals

    Returns:
        [List]: list of dictionaries
    """
    return ANIMALS

def get_single_animal(id):
    """Gets a single animal from the list

    Args:
        id ([number]): The id of the animal

    Returns:
        [dictionary]: The selected animal
    """
    requested_animal = None
    for animal in ANIMALS:
        if animal['id'] == id:
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    max_id = ANIMALS[-1]['id']

    new_id = max_id + 1
    animal['id'] = new_id

    ANIMALS.append(animal)

    return animal
