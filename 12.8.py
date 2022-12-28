# Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)

result = isinstance(School_bus, Vehicle)
if result:
    print("School_bus is an instance of the Vehicle class")
else:
    print("School_bus is not an instance of the Vehicle class")
