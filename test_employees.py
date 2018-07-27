import unittest
from employees import Employee


class TestEmployees(unittest.TestCase):
    """Tests for employees.py"""

    def SetUp(self):
        fname = 'Test'
        lname = 'Dude'
        salary = 5000
        self.test_dude = Employee(fname, lname, salary)

    def test_give_default_raise(self):
        self.test_dude.give_raise()
        self.assertEqual(self.test_dude.salary, 10000)

    def test_give_custom_raise(self):
        self.test_dude.give_raise(10000)
        self.assertEqual(self.test_dude.salary, 15000)


unittest.main()

