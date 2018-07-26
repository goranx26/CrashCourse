from car import Car
from electric_car import ElectricalCar

my_ride = Car('dodge', 'charger', 1970)
print(my_ride.get_descriptive_name())

wifes_ride = ElectricalCar('tesla', 'roadster', 2019)
print(wifes_ride.get_descriptive_name())
