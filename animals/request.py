import sqlite3
import json

from models import Animal

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]


def get_all_animals():
    """Return a list of animals

    Returns:
        [List]: list of dictionaries
    """
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            
        from animal a
        """)

        dataset = db_cursor.fetchall()
        animals = []

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)


def get_single_animal(id):
    """Gets a single animal from the list

    Args:
        id ([number]): The id of the animal

    Returns:
        [dictionary]: The selected animal
    """
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        or a.name = ?
        """, (id, "snickers"))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                        data['status'], data['location_id'],
                        data['customer_id'])

        return json.dumps(animal.__dict__)


def create_animal(animal):
    max_id = ANIMALS[-1]['id']

    new_id = max_id + 1
    animal['id'] = new_id

    ANIMALS.append(animal)

    return animal


def delete_animal(id):
    """
    [summary]

    Args:
        id ([type]): [description]
    """
    animal_index = -1

    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            animal_index = index
            break

    if animal_index >= 0:
        ANIMALS.pop(animal_index)


def update_animal(id_of_animal, new_animal_dict):
    """
        [summary]

        Args:
            id_of_animal ([type]): [description]
            new_animal_dict ([type]): [description]
    """

    for index, animal in enumerate(ANIMALS):
        # iterating the list
        if animal['id'] == id_of_animal:
            # when we find the correct animal (id matches arg)
            # reassign value of item at current index to equal
            # new animal dict arg
            ANIMALS[index] = new_animal_dict
            break
