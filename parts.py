from abc import ABC, abstractmethod


class Wheel:
    x = ''
    count = 0

    def __init__(self):
        self.wheelAmount = 0

    def amount(x):
        if x in ["car"]:
            count = 4
        else:
            count = 2
        return count


class Vehicle(ABC):

    @abstractmethod
    def __init__(self, vehicle, name):
        self.vehicle = vehicle
        self.owner = name

    @abstractmethod
    def owner(self):
        pass
    @abstractmethod
    def get_speed(self, vehicle):
        pass
    @abstractmethod
    def color(self):
        pass
    @abstractmethod
    def get_engine(self):
        pass

class Engine:

    def __init__(self):
        self.engine = 0

    def does_vehicle_have_engine(x):
        if x in ["car"]:
            return 1
        else:
            return 0