import unittest
from postcodes import PostCodeUK
from parameterized import parameterized

class TestPostCodeUK(unittest.TestCase):

    def setUp(self):
        pass

    @parameterized.expand(['AA9A 9AA', 'A9A 9AA', 'A9 9AA', 'A99 9AA', 'AA9 9AA', 'AA99 9AA'])
    def test_postcode_uk_init(self, postcode_format):
        postcode = PostCodeUK()
        assert postcode != None

