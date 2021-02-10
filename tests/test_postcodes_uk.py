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
    def test_postcodes_uk_valid_formats(self, raw_postcode, area, district, sector, unit):
        postcode = PostCodeUK(raw_postcode.lower())
        self.assertEqual(postcode.raw_postcode, raw_postcode)
        self.assertEqual(postcode.full_postcode, raw_postcode)

        outward, inward = raw_postcode.split(' ')
        self.assertEqual(postcode.outward, outward)
        self.assertEqual(postcode.inward, inward)

        self.assertEqual(postcode.is_valid(), True)
        self.assertEqual(postcode.area, area)
        self.assertEqual(postcode.district, district)
        self.assertEqual(postcode.sector, sector)
        self.assertEqual(postcode.unit, unit)

    @parameterized.expand(['9A 9AA', '9A 9AA', '9 9AA', '99 9AA', '9 9AA', '99 9AA'])
    def test_postcodes_uk_invalid_area(self, raw_postcode):
        postcode = PostCodeUK(raw_postcode.lower())
        self.assertEqual(postcode.raw_postcode, raw_postcode)
        self.assertEqual(postcode.full_postcode, raw_postcode)

        outward, inward = raw_postcode.split(' ')
        self.assertEqual(postcode.outward, outward)
        self.assertEqual(postcode.inward, inward)

        self.assertEqual(postcode.is_valid(), False)
        self.assertEqual(postcode.errors, {'area': 'Invalid area format.'})

    @parameterized.expand(['A 9A', 'AA 9A', 'AAA 9A', 'A 9AA', 'AA 9AA', 'AAA 9AA'])
    def test_postcodes_uk_invalid_district(self, raw_postcode):
        postcode = PostCodeUK(raw_postcode.lower())
        self.assertEqual(postcode.raw_postcode, raw_postcode)
        self.assertEqual(postcode.full_postcode, raw_postcode)

        outward, inward = raw_postcode.split(' ')
        self.assertEqual(postcode.outward, outward)
        self.assertEqual(postcode.inward, inward)

        self.assertEqual(postcode.is_valid(), False)
        self.assertEqual(postcode.errors, {'district': 'Invalid district format.'})

    @parameterized.expand(['AA9A AA', 'A9A AA', 'A9 AA', 'A99 AA', 'AA9 AA', 'AA99 AA'])
    def test_postcodes_uk_invalid_sector(self, raw_postcode):
        postcode = PostCodeUK(raw_postcode.lower())
        self.assertEqual(postcode.raw_postcode, raw_postcode)
        self.assertEqual(postcode.full_postcode, raw_postcode)

        outward, inward = raw_postcode.split(' ')
        self.assertEqual(postcode.outward, outward)
        self.assertEqual(postcode.inward, inward)

        self.assertEqual(postcode.is_valid(), False)
        self.assertEqual(postcode.errors, {'sector': 'Invalid sector format.'})

    @parameterized.expand(['AA9A 9', 'A9A 9', 'A9 9', 'A99 9', 'AA9 9', 'AA99 9'])
    def test_postcodes_uk_invalid_unit(self, raw_postcode):
        postcode = PostCodeUK(raw_postcode.lower())
        self.assertEqual(postcode.raw_postcode, raw_postcode)
        self.assertEqual(postcode.full_postcode, raw_postcode)

        outward, inward = raw_postcode.split(' ')
        self.assertEqual(postcode.outward, outward)
        self.assertEqual(postcode.inward, inward)

        self.assertEqual(postcode.is_valid(), False)
        self.assertEqual(postcode.errors, {'unit': 'Invalid unit format.'})