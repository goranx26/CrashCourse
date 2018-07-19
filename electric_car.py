"""A set of Classes to represent electrical cars"""
from car import Car


class Battery():
    """A simple model of a battery for an electric car"""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Prints a description of the battery"""
        print("This car has a ", str(self.battery_size), "kWh battery")

    def get_range(self):
        """Prints the range of the current battery"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = 'This car can go ' + str(range) + ' miles on a full charge'
        print(message)


class ElectricalCar(Car):
    """Models the specifics of an electrical car"""

    def __init__(self, make, model, year):
        """
        Initializes the attributes of the parent class Car
        Then inits the attributes specific to the electrical car
        """
        super().__init__(make, model, year)
        self.battery = Battery()
