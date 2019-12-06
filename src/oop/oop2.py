# GroundVehicle class 
class GroundVehicle():
    # change it so the num_wheels defaults to 4 if not specified
    def __init__(self, name = 'Bob', num_wheels = 4):
        self.name = name
        self.num_wheels = num_wheels

    # add method drive() that returns "vroooom".
    def drive(self):
        return ("vroooom")  

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

# TODO: Go through the vehicles list and print the result of calling drive() on each.
# print(GroundVehicle().drive())
# print(GroundVehicle(3).drive())
# print(Motorcycle(5).drive())
# print(GroundVehicle(4).drive())
# print(Motorcycle().drive())
for v in vehicles:
    print(v.drive())
# vehicles2 = vehicles
# vehicles = iter(vehicles)
# start_next = GroundVehicle.drive()
# while (1):
#     val = next(vehicles, 'end')
#     if val == 'end':
#         print('list end')
#         break
#     else:
#         print(val)
# start_for = GroundVehicle.drive()
# for i in vehicles2:
#     print(i)