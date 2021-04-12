CUSTOMERS = [
    {
      "id": 1,
      "name": "Al Roker",
      "address": "7002 Chestnut Ct"
    },
    {
      "id": 2,
      "name": "Whitney Houston",
      "address": "80 Queens Place"
    },
    {
      "id": 3,
      "name": "Shelea Frazier",
      "address": "9025 Singers Pk Drive"
    },
    {
      "id": 4,
      "name": "Luther Vandross",
      "address": "1000 King Road"
    }
  ]

def get_all_customers():
    return CUSTOMERS

    # Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    # Get the id value of the last animal in the list
    #"max_id" would equal 3 
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list (append is like the "push" to javascript arrays)
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer
