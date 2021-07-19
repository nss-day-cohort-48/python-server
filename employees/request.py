import sqlite3
import json

from models import Employee

EMPLOYEES = [
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


def get_all_employees():
    """Return a list of employees

    Returns:
        [List]: list of dictionaries
    """
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        select
            e.id,
            e.name,
            e.address,
            e.location_id
        from employee e
        """)

        dataset = db_cursor.fetchall()
        employees = []

        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)


def get_single_employee(id):
    """Gets a single employee from the list

    Args:
        id ([number]): The id of the employee

    Returns:
        [dictionary]: The selected employee
    """
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        select
            e.id,
            e.name,
            e.address,
            e.location_id
        from employee e
        WHERE e.id = ?

        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'],
                            data['address'], data['location_id'])

        return json.dumps(employee.__dict__)
