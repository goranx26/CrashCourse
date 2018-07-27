import unittest
from employees import give_raise

class TestEmployees(unittest.TestCase):
    """Tests for employees.py"""

    def SetUp(self):
        self.test_dude = Employee('Test', 'Dude', 5000)


    def test_give_default_raise(self):
        self.test_dude.give_raise()
        self.assertEqual(self.testdude.salary, 10000)

    def test_give_custom_raise(self):
        pass



