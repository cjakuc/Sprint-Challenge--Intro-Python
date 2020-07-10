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

# Base class Vehicle
class Vehicle:
    def __init__ (self):
        pass

# FlightVehichlce inherits from Vehicle
class FlightVehicle(Vehicle):
    def __init__ (self):
        super().__init__()
        pass

# Starship inherits from FlightVehicle
class Starship(FlightVehicle):
    def __init__ (self):
        super().__init__()
        pass

# Airplane inherits from FlightVehicle
class Airplane(FlightVehicle):
    def __init__ (self):
        super().__init__()
        pass

# GroundVehicle inherits from Vehicle
class GroundVehicle(Vehicle):
    def __init__ (self):
        super().__init__()
        pass

# Car inherits from GroundVehicle
class Car(GroundVehicle):
    def __init__ (self):
        super().__init__()
        pass

# Motorcycle inherits from GroundVehicle
class Motorcycle(GroundVehicle):
    def __init__ (self):
        super().__init__()
        pass