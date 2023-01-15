import json
import sqlite3
from models import Order, Size, Metal, Style

def get_all_orders():
    """Returns all order dictionaries"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.style_id,
            o.size_id,
            m.metal,
            m.price metal_price,
            s.style,
            s.price style_price,
            sz.carets,
            sz.price size_price
        FROM orders o
        JOIN metals m 
            ON m.id = o.metal_id
        JOIN styles s 
            ON s.id = o.style_id
        JOIN sizes sz 
            ON sz.id = o.size_id
        """)

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(row['id'], row['metal_id'], row['style_id'], row['size_id'])
            metal = Metal(row['metal_id'], row['metal'], row['metal_price'])
            order.metal = metal.__dict__
            style = Style(row['style_id'], row['style'], row['style_price'])
            order.style = style.__dict__
            size = Size(row['size_id'], row['carets'], row['size_price'])
            order.size = size.__dict__

            orders.append(order.__dict__)

    return orders

# Function with a single parameter
def get_single_order(id):
    """"Returns a single order by provided id
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.style_id,
            o.size_id
        FROM orders o
        WHERE o.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        order = Order(data['id'], data['metal_id'], data['style_id'], data['size_id'])

        return order.__dict__

def create_order(new_order):
    """Adds a new order dictionary

    Args:
        order (dictionary): Information about the order

    Returns:
        dictionary: Returns the order dictionary with an ORDER id
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            ( metal_id, style_id, size_id )
        VALUES
            ( ?, ?, ?);
        """, (new_order['metal_id'], new_order['style_id'],
              new_order['size_id'], ))

        id = db_cursor.lastrowid

        new_order['id'] = id

    return new_order

def delete_order(id):
    """Deletes a single order

    Args:
        id (int): Order id
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM orders
        WHERE id = ?
        """, (id, ))

def update_order(id, new_order):
    """Iterate order list

    Args:
        id (int): Order id
        new_order (dictionary): Replacement order dictionary
    """
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
        