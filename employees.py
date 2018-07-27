class Employee():
    """Class to create employees"""

    def __init__(self, fname, lname, salary):
        """Initialising with the given attributes"""
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def give_raise(self, payraise='5000'):
        """Raises the salary (standard raise = $5000)"""
        self.salary += payraise



