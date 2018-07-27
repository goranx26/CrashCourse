import unittest
from employees import Employee

class TestEmployees(unittest.TestCase):
    """Tests for employees.py"""

    def SetUp(self):
        test_dude = Employee('Test', 'Dude', 5000)


    def test_give_default_raise(self):
        test_dude.give_raise()
        self.assertEqual(test_dude.salary, 10000)


    def test_give_custom_raise(self):
        test_dude.give_raise(10000)
        self.assertEqual(test_dude.salary, 15000)


unittest.main()
