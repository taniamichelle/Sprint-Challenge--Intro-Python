# GroundVehicle class 
class GroundVehicle():
    # change it so the num_wheels defaults to 4 if not specified
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels
        self.num_wheels  = 4

    # add method drive() that returns "vroooom".
    def drive(self):
        print("vroooom.")  


# Subclass Motorcycle from GroundVehicle.
class Motorcycle(GroundVehicle):
    # when you instantiate a Motorcycle, it should automatically set 
    # num_wheels to 2 by passing it to the constructor of its superclass.
    def __init__(self, num_wheels):
        super().__init__(num_wheels)
        self.num_wheels = 2       

    # Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
    def drive(self):
        print("BRAAAP!!")

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# TODO: Go through the vehicles list and print the result of calling drive() on each.

