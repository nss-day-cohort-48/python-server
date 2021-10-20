from models.location import Location
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
            a.customer_id,
            l.name location_name,
            l.address location_address
            
        from animal a
        Join Location l
        on l.id = a.location_id
        """)

        dataset = db_cursor.fetchall()
        animals = []

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            location = Location(
                row['location_id'], row['location_name'], row["location_address"])
            animal.location = location.__dict__
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
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                        data['status'], data['location_id'],
                        data['customer_id'])

        return json.dumps(animal.__dict__)


def create_animal(new_animal):
    """Adds the animal to the ANIMALS list

        Args:
            animal (dictionary): the post body from the request

        Returns:
            string: json formatted string
    """

    with sqlite3.connect('./kennel.db') as conn:
        db_cursor = conn.cursor()


        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            ( ?, ?, ?, ?, ? );
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], ))

        id = db_cursor.lastrowid

        new_animal['id'] = id

        return json.dumps(new_animal)


def delete_animal(id):
    """
    [summary]

    Args:
        id ([type]): [description]
    """
    with sqlite3.connect('./kennel.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        delete from Animal
        where id = ?
        """, (id, ))


def update_animal(id_of_animal, new_animal_dict):
    """
        [summary]

        Args:
            id_of_animal ([type]): [description]
            new_animal_dict ([type]): [description]
    """

    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
            Update Animal
            Set 
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
            where id = ?
        """, (
            new_animal_dict['name'],
            new_animal_dict['breed'],
            new_animal_dict['status'],
            new_animal_dict['location_id'],
            new_animal_dict['customer_id'],
            id_of_animal,
        ))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True


def get_animals_by_search(text):
    animals = json.loads(get_all_animals())
    animals = [animal for animal in animals if text.lower() in animal['name'].lower()]
    return json.dumps(animals)
