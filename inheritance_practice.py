class Vehicle:
    def __init__(self):
        self.wheels = 0
        self.steering = ""
        self.power = ""
        
    def drive(self):
        print("Vroom")

class Bike(Vehicle):
    def __init__(self):
        self.make = "Schwinn"
        
    def drive(self):
        print("ching ching")
        
class Rollerblades(Vehicle):
    def __init__(self):
        self.make = "2PM"
        
class Car(Vehicle):
    def __init__(self):
        self.make = "Honda"
        
        
my_car = Car()
my_car.wheels = 4
my_car.power = "gas"
my_car.steering = "wheel"
my_car.drive()

a_bike = Bike()
a_bike.wheels = 2
a_bike.power = "peddling"
a_bike.steering = "handlebars"
a_bike.drive()
