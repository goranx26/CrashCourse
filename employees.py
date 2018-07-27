class Employee(self, fname, lname, salary):
    """Class to create employees"""

    def __init__(self):
        """Initialising with the given attributes"""
        fname = self.fname
        lname = self.lname
        salary = self.salary

    def give_raise(self, raise=5000):
        """Raises the salary (standard raise = $5000)"""
        salary += raise



