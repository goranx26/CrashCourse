import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""
    def test_first_last_name(self):
        """Do names like 'Jimmy Gestapo' work?"""
        formatted_name = get_formatted_name('jimmy', 'gestapo')
        self.assertEqual(formatted_name, 'Jimmy Gestapo')

    def test_first_last_middle_name(self):
        """Do name like 'Maynard James Keenan" work?"""
        formatted_name = get_formatted_name('maynard', 'keenan', 'james')
        self.assertEqual(formatted_name, 'Maynard James Keenan')


unittest.main()
