import sqlite3
import json
from models import Customer


def get_all_customers():
    """Get all customers

    Returns:
        string: a json formatted string
    """
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        """)

        # Initialize an empty list to hold all customer representations
        customers = []
        dataset = db_cursor.fetchall()

        # Iterate all rows of data returned from database
        for row in dataset:

            # Create an customer instance from the current row
            customer = Customer(row['id'], row['name'], row['address'], row['email'],
                                row['password'])

            customers.append(customer.__dict__)

    return json.dumps(customers)


def get_single_customer(id):
    """Get a single customer from the databased by id

    Args:
        id (number): the id being passed in the url

    Returns:
        string: a json formatted string
    """
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        # Create an customer instance from the current row
        customer = Customer(data['name'], data['address'], data['email'],
                            data['password'])
        customer.id = data['id']

        return json.dumps(customer.__dict__)
