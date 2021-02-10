import unittest
from postcodes import PostCodeUK
from parameterized import parameterized


class TestPostCodeUK(unittest.TestCase):

    def setUp(self):
        pass

    @parameterized.expand([['AA9A 9AA', 'AA', '9A', '9', 'AA'],
                           ['A9A 9AA', 'A', '9A', '9', 'AA'],
                           ['A9 9AA', 'A', '9', '9', 'AA'],
                           ['A99 9AA', 'A', '99', '9', 'AA'],
                           ['AA9 9AA', 'AA', '9', '9', 'AA'],
                           ['AA99 9AA', 'AA', '99', '9', 'AA']])
    def test_postcodes_uk_valid_formats(self, postcode, area, district, sector, unit):
        postcode = PostCodeUK(postcode.lower())
        self.assertEqual(postcode.is_valid(), True)
        self.assertEqual(postcode.area, area)
        self.assertEqual(postcode.district, district)
        self.assertEqual(postcode.sector, sector)
        self.assertEqual(postcode.unit, unit)
        self.assertEqual(postcode.postcode, postcode)
