# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def info(self):
        print(
            f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}")


class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.info())
