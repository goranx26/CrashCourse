class Restaurant():
    """My first class"""

    def __init__(self, name, style, number_served=0):
        """initialize the name and type of food"""
        self.name = name
        self.style = style
        self.number_served = number_served

    def describe(self):
        """Prints out the info for the restaurant."""
        print("The restaurant is called", self.name, "and serves", self.style, "style food")

    def open_restaurant(self):
        """Shows the rest as open"""
        print("The restaurant", self.name, "is now open.")

    def increment_number_served(self, inc):
        """Adds inc to the number of served guests"""
        self.number_served += inc


class IcecreamStand(Restaurant):
    """My first class had a baby"""

    def __init__(self, name, style, number_served=0):
        super().__init__(name, style, number_served=0)
        self.flavours = ['vanilla', 'chocholate', 'indica', 'sativa']

    def get_flavours(self):
        print("Our flavours are:")
        i = 1
        for flavour in self.flavours:
            print(i, ".", flavour.title())
            i += 1