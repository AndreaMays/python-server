EMPLOYEES = [
    {
      "id": 1,
      "name": "Yas Coleman",
      "address": "1234 Abc Drive",
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Jayse Shipman",
      "address": "5687 Flashman Court",
      "locationId": 2
    },
    {
      "id": 3,
      "name": "LaLa Herman",
      "address": "8000 Badass Way",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Lacey Sittrell",
      "address": "900 Coders Alley",
      "locationId": 2
    }
  ]

  # no "self" passed in because it doesn't have line 26 is not a class, its just a function
def get_all_employees():
    return EMPLOYEES

    # Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee