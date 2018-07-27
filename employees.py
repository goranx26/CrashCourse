class Employee():
    """Class to create employees"""

    def __init__(self, fname, lname, salary):
        """Initialising with the given attributes"""
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def give_raise(self):
        """Raises the salary (standard raise = $5000)"""
        self.salary += 5000

    def give_custom_raise(self, payraise):
        self.salary += payraise




