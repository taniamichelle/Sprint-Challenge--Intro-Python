# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    '''
    this is the Vehicle base (parent) class
    '''
    pass

class FlightVehicle(Vehicle):
    '''
    this is the FlightVehicle class, subclass of Vehicle
    '''
    pass

class Starship(FlightVehicle):
    '''
    this is the Starship class, subclass of FlightVehicle
    '''
    pass

class Airplane(FlightVehicle):
    '''
    this is the Airplane class, subclass of Flightvehicle
    '''
    pass

class GroundVehicle(Vehicle):
    '''
    this is the GroundVehicle class, subclass of Vehicle
    '''
    pass

class Car(GroundVehicle):
    '''
    this is the Car class, subclass of GroundVehicle
    '''
    pass

class Motorcycle(GroundVehicle):
    '''
    this is the Motorcycle class, subclass of GroundVehicle
    '''
    pass 