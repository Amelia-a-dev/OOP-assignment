class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Boat:
    def move(self):
        return "Sailing ⛵"

# Create instances of each class
car = Car()
plane = Plane()
boat = Boat()

# Put them in a list to demonstrate polymorphism
vehicles = [car, plane, boat]

# Call the move method on each vehicle
for vehicle in vehicles:
    print(vehicle.move())
