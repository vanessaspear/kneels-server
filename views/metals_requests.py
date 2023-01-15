import json
import sqlite3
from models import Metal

def get_all_metals():
    """Returns all metal dictionaries"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM metals m
        """)

        metals = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            metal = Metal(row['id'], row['metal'], row['price'])

            metals.append(metal.__dict__)
    
    return metals

# Function with a single parameter
def get_single_metal(id):
    """Returns single metal based on id

    Args:
        id (int): metal id

    Returns:
        dictionary: selected metal
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM metals m
        WHERE m.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        metal = Metal(data['id'], data['metal'], data['price'])

    return metal.__dict__

def update_metal(id, new_metal):
    """Updates a metal dictionary

    Args:
        id (int): Primary key of metal to be updated
        new_metal (dict): Updated metal information
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE metals
            SET
                metal = ?,
                price = ?
        WHERE id = ?
        """, (new_metal['metal'], new_metal['price'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True