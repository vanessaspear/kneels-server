STYLES = [
    {
        "id": 1,
        "styles": "Classic",
        "price": 500
    },
    {
        "id": 2,
        "styles": "Modern",
        "price": 710
    },
    {
        "id": 3,
        "styles": "Vintage",
        "price": 965
    }
]

def get_all_styles():
    """Returns all style dictionaries"""
    return STYLES
    
# Function with a single parameter
def get_single_style(id):
    """"Returns a single style by provided id
    """
    # Variable to hold the found style, if it exists
    requested_style = None

    # Iterate the STYLES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for style in STYLES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if style["id"] == id:
            requested_style = style

    return requested_style
