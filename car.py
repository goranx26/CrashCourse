class Car():
    def __init__(self,make,model,year):
        """Init attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a nicely formatted name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Prints the car's mileage"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileage):
        """Set the meter to specified miles"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant\'t roll back the meter")

    def increment_odometer(self,miles):
        """Add given amount to the odometer"""
        self.odometer_reading += miles

my_new_car = Car('ford', 'mustang', 1969)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(666)
my_new_car.read_odometer()

my_used_car = Car('opel','ascona',1980)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(2000)
my_used_car.update_odometer(500)
my_used_car.read_odometer()
print("Incrementing miles")
my_used_car.increment_odometer(500)
my_used_car.read_odometer()

