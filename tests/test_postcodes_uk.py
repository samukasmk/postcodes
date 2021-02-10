import unittest
from postcodes import PostCodeUK


class TestPostCodeUK(unittest.TestCase):

    def setUp(self):
        pass

    def test_postcode_uk_init(self):
        postcode = PostCodeUK()
        assert postcode != None
