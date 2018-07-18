class Restaurant():
    """My first class"""

    def __init__(self, name, style,number_served=0):
        """initialize the name and type of food"""
        self.name = name
        self.style = style
        self.number_served = number_served

    def describe(self):
        """Prints out the info for the restaurant."""
        print("The restaurant is called",self.name,"and serves",self.style,"style food")

    def open_restaurant(self):
        """Shows the rest as open"""
        print("The restaurant",self.name,"is now open.")
    
    def increment_number_served(self,inc):
        """Adds inc to the number of served guests"""
        self.number_served += inc

rest1 = Restaurant('Chong Li\'s dog chop','Chinese')
rest2 = Restaurant('Oves grill','Mosbricka')
rest3 = Restaurant('Pacos MexMix','Texican')

rest1.describe()
rest1.open_restaurant()
rest1.increment_number_served(10)
print("We have served " + str(rest1.number_served))
rest2.describe()
rest2.open_restaurant()
rest3.describe()
rest3.open_restaurant()

