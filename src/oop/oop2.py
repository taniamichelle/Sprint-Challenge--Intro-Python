# GroundVehicle class 
class GroundVehicle():
    # change it so the num_wheels defaults to 4 if not specified
    def __init__(self, name = 'Bob', num_wheels = 4):
        self.name = name
        self.num_wheels = num_wheels

    # add method drive() that returns "vroooom".
    def drive(self):
        return ("vroooom")  

# instantiate instance of GroundVehicle to test
g = GroundVehicle("Fred")
print(g.name)
print(g.num_wheels)
print(g.drive())

# Subclass Motorcycle from GroundVehicle.
class Motorcycle(GroundVehicle):
    # when you instantiate a Motorcycle, it should automatically set 
    # num_wheels to 2 by passing it to the constructor of its superclass.
    def __init__(self, name = 'Rosie', num_wheels = 2):
        super().__init__(name, num_wheels)
        self.num_wheels = num_wheels

    # Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
    def drive(self):
        return ("BRAAAP!!")

# instantiate instance of Motorcycle to test
m = Motorcycle("Jillian")
print(m.name)
print(m.num_wheels)
print(m.drive())

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
for v in vehicles:
    print(v.drive())
