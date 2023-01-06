ORDERS = [
    {
        "id": 1,
        "metalId": 1,
        "sizeId": 2,
        "styleId": 1
    }
]

def get_all_orders():
    """Returns all order dictionaries"""
    return ORDERS

# Function with a single parameter
def get_single_order(id):
    """"Returns a single order by provided id
    """
    # Variable to hold the found order, if it exists
    requested_order = None

    # Iterate the ORDERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
    """Adds a new order dictionary

    Args:
        order (dictionary): Information about the order

    Returns:
        dictionary: Returns the order dictionary with an ORDER id
    """
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order
    