import sqlite3
import json
from models import Employee

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

def create_employee(employee):
    # Get the id value of the last animal in the list
    #"max_id" would equal 3 
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list (append is like the "push" to javascript arrays)
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee

def delete_employee(id):
    # Initial -1 value for animal index, in case one isn't found
    employee_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item and the animal. So enumerate() lets you access two things at once.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Store the current index.
            employee_index = index

    # If the animal was found, use pop(int) to remove it from list. ".pop" pass it an index and thats what gets removed
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

      # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        """)

        
        # Initialize an empty list to hold all animal representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id'])

            employees.append(employee.__dict__)
        return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.adress,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, )) 
  
        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                            data['location_id'])

        return json.dumps(employee.__dict__)      