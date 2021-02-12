import pytest
from postcodes.uk import PostCodeUK


def test_postcodes_uk_uppercase_normalization():
    raw_postcode = 'aa9a 9aa'
    postcode = PostCodeUK(raw_postcode)
    assert postcode.raw_postcode == raw_postcode
    assert postcode.full_postcode == 'AA9A 9AA'


def test_postcodes_uk_outward_and_inward_validations():
    raw_postcode = 'AA9A 9AA'
    outward, inward = raw_postcode.split(' ')
    postcode = PostCodeUK(raw_postcode)
    assert postcode.outward == outward
    assert postcode.inward == inward


@pytest.mark.parametrize('raw_postcode, area, district, sector, unit', [['AA9A 9AA', 'AA', '9A', '9', 'AA'],
                                                                        ['A9A 9AA', 'A', '9A', '9', 'AA'],
                                                                        ['A9 9AA', 'A', '9', '9', 'AA'],
                                                                        ['A99 9AA', 'A', '99', '9', 'AA'],
                                                                        ['AA9 9AA', 'AA', '9', '9', 'AA'],
                                                                        ['AA99 9AA', 'AA', '99', '9', 'AA']])
def test_postcodes_uk_valid_formats(raw_postcode, area, district, sector, unit):
    postcode = PostCodeUK(raw_postcode)
    assert postcode.raw_postcode == raw_postcode
    assert postcode.full_postcode == raw_postcode
    assert postcode.area == area
    assert postcode.district == district
    assert postcode.sector == sector
    assert postcode.unit == unit
    assert postcode.is_valid is True


@pytest.mark.parametrize('raw_postcode', ['9 9AA', '9A 9AA', '99 9AA',
                                          'AAA9A 9AA', 'AAAA9A 9AA', 'AAAAA9A 9AA',
                                          'AAA99 9AA', 'AAAA99 9AA', 'AAAAA99 9AA', ])
def test_postcodes_uk_invalid_area(raw_postcode):
    postcode = PostCodeUK(raw_postcode)
    assert postcode.raw_postcode == raw_postcode
    assert postcode.full_postcode == raw_postcode
    assert postcode.is_valid is False
    assert postcode.errors == {'area': 'Invalid area format.'}


@pytest.mark.parametrize('raw_postcode', ['A 9AA', 'AA 9AA'])
def test_postcodes_uk_invalid_district(raw_postcode):
    postcode = PostCodeUK(raw_postcode)
    assert postcode.raw_postcode == raw_postcode
    assert postcode.full_postcode == raw_postcode
    assert postcode.is_valid is False
    assert postcode.errors == {'district': 'Invalid district format.'}


@pytest.mark.parametrize('raw_postcode', ['AA9A AA', 'A9A AA', 'A9 AA', 'A99 AA', 'AA9 AA', 'AA99 AA'])
def test_postcodes_uk_invalid_sector(raw_postcode):
    postcode = PostCodeUK(raw_postcode)
    assert postcode.raw_postcode == raw_postcode
    assert postcode.full_postcode == raw_postcode
    assert postcode.is_valid is False
    assert postcode.errors == {'sector': 'Invalid sector format.'}


@pytest.mark.parametrize('raw_postcode', ['AA9A 9', 'A9A 9', 'A9 9', 'A99 9', 'AA9 9', 'AA99 9',
                                          'AA9A 9AAA', 'A9A 9AAA', 'A9 9AAA', 'A99 9AAA', 'AA9 9AAA', 'AA99 9AAA',
                                          'AA9A 9AAAA', 'A9A 9AAAA', 'A9 9AAAA', 'A99 9AAAA', 'AA9 9AAAA',
                                          'AA99 9AAAA'])
def test_postcodes_uk_invalid_unit(raw_postcode):
    postcode = PostCodeUK(raw_postcode)
    assert postcode.raw_postcode == raw_postcode
    assert postcode.full_postcode == raw_postcode
    assert postcode.is_valid is False
    assert postcode.errors == {'unit': 'Invalid unit format.'}

#
# def test_postcodes_uk_to_dict():
#     raw_postcode = 'AA9A 9AA'
#     outward, inward = raw_postcode.split(' ')
#     postcode = PostCodeUK(raw_postcode)
#     assert postcode.outward == outward
#     assert postcode.inward == inward