import unittest
from city_functions import country_info


class CountryTestCase(unittest.TestCase):
    """Tests for city_functions.py"""
    def test_city_country(self):
        """Test output from country_info"""
        formatted_string = country_info('santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')


unittest.main()
