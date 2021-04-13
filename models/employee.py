class Employee():
    def __init__(self, id, name, address, locationId):
        self.id = id
        self.name = name
        self.address = address
        self.locationId = locationId

        new_employee = Employee(2, "Jayse Shipman", "5687 Flashman Court", 2)