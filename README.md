# postcodes
Library to parse postal code format

This is the another one validation libraries of postcodes in the United Kingdom.

The main goal of this package and difference of the others is to show in exactly part of postcode is wrong and need to be fixup.

## Installation
Instaling with pip (from github)

```
pip install -e git://github.com/samukasmk/postcodes.git@v0.1.1#egg=postcodes
```

On the future we will provides at pypi.org

## Using library for validations

### Validating a correct postcode in python

This example below validates a correct postcode from Facebook `'W1T 1FB'`

```python
>>> from postcodes.uk import PostCodeUK

>>> postcode = PostCodeUK('W1T 1FB')
>>> postcode.is_valid
True

>>> postcode.outward
"W1T"
>>> postcode.inward
"1FB"

>>> postcode.area
"W"
>>> postcode.district
"1T"
>>> postcode.sector
"1"
>>> postcode.unit
"FB"

>>> postcode.to_dict()
{'postcode': 'W1T 1FB',
 'is_valid': True,
 'attributes': {'area': 'W',
                'district': '1T',
                'sector': '1',
                'unit': 'FB'},
 'sides': {'outward': 'W1T',
           'inward': '1FB'},
 'errors': {}}
```

### Validating a invalid postcode in python

This example is it is similar to the previous using Facebook postcode but missing last 'B' from 'FB' area part

```python
>>> from postcodes.uk import PostCodeUK

>>> postcode = PostCodeUK('W1T 1F')
>>> postcode.is_valid
False

>>> postcode.errors
{'unit': 'Invalid unit format.'}

>>> postcode.outward
"W1T"
>>> postcode.inward
"1F"

>>> postcode.area
"W"
>>> postcode.district
"1T"
>>> postcode.sector
"1"
>>> postcode.unit
"F"

>>> postcode.to_dict()
{'postcode': 'W1T 1F',
 'is_valid': False,
 'attributes': {'area': 'W',
                'district': '1T',
                'sector': '1',
                'unit': 'F'},
 'sides': {'outward': 'W1T',
           'inward': '1F'},
 'errors': {'unit': 'Invalid unit format.'}}
```


### Validating a invalid postcode from Facebook but missing space
The space is very important to determine which part of postcode is wrong.
So it will no work without spaces because the lib will considerates all string with outward side.
The example of missing spaces below:

```python
>>> from postcodes.uk import PostCodeUK

>>> postcode = PostCodeUK('W1T1FB')
>>> postcode.is_valid
False

>>> postcode.errors
{'missing_space': 'Missing space in the postcode',
 'district': 'Invalid district format.',
 'sector': 'Invalid sector format.',
 'unit': 'Invalid unit format.'}

>>> postcode.outward
"W1T1FB"
>>> postcode.inward
None

>>> postcode.area
"W"
>>> postcode.district
"1T1FB"
>>> postcode.sector
None
>>> postcode.unit
None

>>> postcode.to_dict()
{'postcode': 'W1T1FB',
 'is_valid': False,
 'attributes': {'area': 'W',
                'district': '1T1FB',
                'sector': None,
                'unit': None},
 'sides': {'outward': 'W1T1FB',
           'inward': None},
 'errors': {'missing_space': 'Missing space in the postcode',
            'district': 'Invalid district format.',
            'sector': 'Invalid sector format.',
            'unit': 'Invalid unit format.'}}
```
## Advanced usage

For advanced usage you can use the `PostCodeUK` class to validate specific parts of postcode.

```python
>>> from postcodes.parsers.uk import PostCodeUK

>>>  # validating only the area part of Buckingham Palace postcode
>>> PostCodeUK.validate_postcode_attribute('area', 'SW')
True

>>>  # validating only the district part of Buckingham Palace postcode
>>> PostCodeUK.validate_postcode_attribute('district', '1A')
True

>>>  # validating only the sector part of Buckingham Palace postcode
>> > PostCodeUK.validate_postcode_attribute('sector', '1')
True

>>>  # validating only the unit part of Buckingham Palace postcode
>>> PostCodeUK.validate_postcode_attribute('unit', 'AA')
True
```

## Using Command line script for validations

If you want a command line solution for consulting in your terminal
or integrate with bash scripts you can use command line created on
pip install process to validate postcodes

```
postcodes --help
usage: postcodes [-h] -p [POSTCODES ...] [-r REGION_FORMAT] [-o {json,text}]

A command line to parses postcodes.

optional arguments:
  -h, --help            show this help message and exit
  -p [POSTCODES ...], --postcodes [POSTCODES ...]
                        The post code to analise.
  -r REGION_FORMAT, --region-format REGION_FORMAT
                        The region format.
  -o {json,text}, --output-format {json,text}
                        The region format.
```

The command line provides two types of output `json` or `text` and many values for the argument `--postcodes`.

### Validating postcodes in command line on json output

This example below validates a correct postcode from Facebook `'W1T 1FB'` on the json output


```
$ postcodes --postcodes 'W1T 1FB' --output-format json
{
    "W1T 1FB": {
        "attributes": {
            "area": "W",
            "district": "1T",
            "sector": "1",
            "unit": "FB"
        },
        "errors": {},
        "is_valid": true,
        "postcode": "W1T 1FB",
        "sides": {
            "inward": "1FB",
            "outward": "W1T"
        }
    }
}
```

**Exit code: 0** (with success)

#### Validating two correct postcodes in command line on json output

The another example of validating two correct postcodes of Buckingham Palace `'SW1A 1AA'` and Facebook `'W1T 1FB'` together

```
$ postcodes --postcodes 'SW1A 1AA' 'W1T 1FB' --output-format json
{
    "SW1A 1AA": {
        "attributes": {
            "area": "SW",
            "district": "1A",
            "sector": "1",
            "unit": "AA"
        },
        "errors": {},
        "is_valid": true,
        "postcode": "SW1A 1AA",
        "sides": {
            "inward": "1AA",
            "outward": "SW1A"
        }
    },
    "W1T 1FB": {
        "attributes": {
            "area": "W",
            "district": "1T",
            "sector": "1",
            "unit": "FB"
        },
        "errors": {},
        "is_valid": true,
        "postcode": "W1T 1FB",
        "sides": {
            "inward": "1FB",
            "outward": "W1T"
        }
    }
}
```

**Exit code: 0** (with success)


#### Validating two postcodes in command line on json format but one correct and another incorrect

The another example of validating together two postcodes of Buckingham Palace `'SW1A 1AA'` and wrong Facebook `'W1T 1F'` missing last `B`

```
$ postcodes --postcodes 'SW1A 1AA' 'W1T 1F' --output-format json
{
    "SW1A 1AA": {
        "attributes": {
            "area": "SW",
            "district": "1A",
            "sector": "1",
            "unit": "AA"
        },
        "errors": {},
        "is_valid": true,
        "postcode": "SW1A 1AA",
        "sides": {
            "inward": "1AA",
            "outward": "SW1A"
        }
    },
    "W1T 1F": {
        "attributes": {
            "area": "W",
            "district": "1T",
            "sector": "1",
            "unit": "F"
        },
        "errors": {
            "unit": "Invalid unit format."
        },
        "is_valid": false,
        "postcode": "W1T 1F",
        "sides": {
            "inward": "1F",
            "outward": "W1T"
        }
    }
}
```

**Exit code: 1** (with error because of the second the is incorrect)

### Validating postcodes in command line on text output

This example below validates a correct postcode from Facebook `'W1T 1FB'` on the text output

```
$ postcodes -p 'W1T 1FB'
Parsing postcode validations...

---
Postcode (W1T 1FB) format is: VALID
  Attributes:
    -> area: W
    -> district: 1T
    -> sector: 1
    -> unit: FB

---
Results:
  -> Valid postcodes: (W1T 1FB)
```

**Exit code: 0** (with success)

#### Validating two correct postcodes in command line on text output

The another example of validating two correct postcodes of Buckingham Palace `'SW1A 1AA'` and Facebook `'W1T 1FB'` together

```
$ postcodes -p 'SW1A 1AA' 'W1T 1FB'
Parsing postcode validations...

---
Postcode (SW1A 1AA) format is: VALID
  Attributes:
    -> area: SW
    -> district: 1A
    -> sector: 1
    -> unit: AA

---
Postcode (W1T 1FB) format is: VALID
  Attributes:
    -> area: W
    -> district: 1T
    -> sector: 1
    -> unit: FB

---
Results:
  -> Valid postcodes: (SW1A 1AA), (W1T 1FB)
```

**Exit code: 0** (with success)

#### Validating two postcodes in command line on text format but one correct and another incorrect

The another example of validating together two correct postcodes of (Buckingham Palace `'SW1A 1AA'`) and (National Savings `'DH99 1NS'`) and two **wrong postcodes** (Facebook `'W1T 1F'` missing last `B`) and (The Guardian `'N1 9G'` missing last `U`)

```
$ postcodes -p 'SW1A 1AA' 'DH99 1NS' 'W1T 1F' 'N1 9G'
Parsing postcode validations...

---
Postcode (SW1A 1AA) format is: VALID
  Attributes:
    -> area: SW
    -> district: 1A
    -> sector: 1
    -> unit: AA

---
Postcode (DH99 1NS) format is: VALID
  Attributes:
    -> area: DH
    -> district: 99
    -> sector: 1
    -> unit: NS

---
Postcode (W1T 1F) format is: INVALID
  Errors:
    -> Invalid unit format.
  Attributes:
    -> area: W
    -> district: 1T
    -> sector: 1
    -> unit: F(invalid format)

---
Postcode (N1 9G) format is: INVALID
  Errors:
    -> Invalid unit format.
  Attributes:
    -> area: N
    -> district: 1
    -> sector: 9
    -> unit: G(invalid format)

---
Results:
  -> Valid postcodes: (SW1A 1AA), (DH99 1NS)
  -> Invalid postcodes: (W1T 1F), (N1 9G)
```

**Exit code: 1** (with error because of the two incorrect postcodes)

## Docker support

The library provides a docker image to use the command line script without install the library in your local machine.

### Building the docker image

To build the docker image you can use the command below:

```shell
docker-compose build postcodes
```

### Running command line script by docker container

To run postcode script by docker-compose tool just add parameters after service name like:

**Displaying help arguments:**

```shell
docker-compose run postcodes --help
```

```
usage: postcodes [-h] -p [POSTCODES ...] [-r {UK}] [-o {json,text}]

A command line to parses postcodes.

options:
  -h, --help            show this help message and exit
  -p [POSTCODES ...], --postcodes [POSTCODES ...]
                        The post code to analise.
  -r {UK}, --region-format {UK}
                        The region format.
  -o {json,text}, --output-format {json,text}
                        The region format.
```


**Validating a correct Buckingham Palace postcode:**

```commandline
docker-compose run postcodes -p 'SW1A 1AA' --output-format json
```

```
Parsing postcode validations...

---
Postcode (SW1A 1AA) format is: VALID
  Attributes:
    -> area: SW
    -> district: 1A
    -> sector: 1
    -> unit: AA

---
Results:
  -> Valid postcodes: (SW1A 1AA)
```


**Validating Buckingham Palace postcode but and set out as json:**

```commandline
docker-compose run postcodes -p 'SW1A 1AA' --output-format json
```

```
{
    "SW1A 1AA": {
        "attributes": {
            "area": "SW",
            "district": "1A",
            "sector": "1",
            "unit": "AA"
        },
        "errors": {},
        "is_valid": true,
        "postcode": "SW1A 1AA",
        "sides": {
            "inward": "1AA",
            "outward": "SW1A"
        }
    }
}
```

## Development

### Running tests

The unit tests of this library are based on `pytest` module from python.

To run the tests you can use the command below:

```shell
docker-compose run tests
```

```
============================================ test session starts =============================================
platform linux -- Python 3.12.2, pytest-8.2.2, pluggy-1.5.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/app
configfile: pyproject.toml
plugins: flakes-4.0.5, cov-5.0.0
collected 52 items                                                                                            

tests/test_postcodes_uk.py::test_postcodes_uk_uppercase_normalization PASSED                            [  1%]
tests/test_postcodes_uk.py::test_postcodes_uk_outward_and_inward_validations PASSED                     [  3%]
tests/test_postcodes_uk.py::test_postcodes_uk_valid_formats[AA9A 9AA-AA-9A-9-AA] PASSED                 [  5%]
tests/test_postcodes_uk.py::test_postcodes_uk_valid_formats[A9A 9AA-A-9A-9-AA] PASSED                   [  7%]
tests/test_postcodes_uk.py::test_postcodes_uk_valid_formats[A9 9AA-A-9-9-AA] PASSED                     [  9%]
tests/test_postcodes_uk.py::test_postcodes_uk_valid_formats[A99 9AA-A-99-9-AA] PASSED                   [ 11%]
tests/test_postcodes_uk.py::test_postcodes_uk_valid_formats[AA9 9AA-AA-9-9-AA] PASSED                   [ 13%]
tests/test_postcodes_uk.py::test_postcodes_uk_valid_formats[AA99 9AA-AA-99-9-AA] PASSED                 [ 15%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_area[9 9AA] PASSED                                [ 17%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_area[9A 9AA] PASSED                               [ 19%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_area[99 9AA] PASSED                               [ 21%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_area[AAA9A 9AA] PASSED                            [ 23%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_area[AAAA9A 9AA] PASSED                           [ 25%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_area[AAAAA9A 9AA] PASSED                          [ 26%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_area[AAA99 9AA] PASSED                            [ 28%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_area[AAAA99 9AA] PASSED                           [ 30%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_area[AAAAA99 9AA] PASSED                          [ 32%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_district[A 9AA] PASSED                            [ 34%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_district[AA 9AA] PASSED                           [ 36%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_sector[AA9A AA] PASSED                            [ 38%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_sector[A9A AA] PASSED                             [ 40%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_sector[A9 AA] PASSED                              [ 42%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_sector[A99 AA] PASSED                             [ 44%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_sector[AA9 AA] PASSED                             [ 46%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_sector[AA99 AA] PASSED                            [ 48%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[AA9A 9] PASSED                               [ 50%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[A9A 9] PASSED                                [ 51%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[A9 9] PASSED                                 [ 53%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[A99 9] PASSED                                [ 55%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[AA9 9] PASSED                                [ 57%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[AA99 9] PASSED                               [ 59%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[AA9A 9AAA] PASSED                            [ 61%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[A9A 9AAA] PASSED                             [ 63%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[A9 9AAA] PASSED                              [ 65%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[A99 9AAA] PASSED                             [ 67%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[AA9 9AAA] PASSED                             [ 69%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[AA99 9AAA] PASSED                            [ 71%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[AA9A 9AAAA] PASSED                           [ 73%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[A9A 9AAAA] PASSED                            [ 75%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[A9 9AAAA] PASSED                             [ 76%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[A99 9AAAA] PASSED                            [ 78%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[AA9 9AAAA] PASSED                            [ 80%]
tests/test_postcodes_uk.py::test_postcodes_uk_invalid_unit[AA99 9AAAA] PASSED                           [ 82%]
tests/test_postcodes_uk.py::test_postcodes_uk_to_dict_with_valid_postcode PASSED                        [ 84%]
tests/test_postcodes_uk.py::test_postcodes_uk_to_dict_with_invalid_area PASSED                          [ 86%]
tests/test_postcodes_uk.py::test_postcodes_uk_to_dict_with_invalid_district PASSED                      [ 88%]
tests/test_postcodes_uk.py::test_postcodes_uk_to_dict_with_invalid_sector PASSED                        [ 90%]
tests/test_postcodes_uk.py::test_postcodes_uk_to_dict_with_invalid_unit PASSED                          [ 92%]
tests/test_postcodes_uk.py::test_postcodes_uk_to_dict_with_invalid_combined_area_and_unit PASSED        [ 94%]
tests/test_postcodes_uk.py::test_postcodes_uk_to_dict_with_invalid_combined_district_and_sector PASSED  [ 96%]
tests/test_postcodes_uk.py::test_postcodes_uk_to_dict_with_missing_separator_letter PASSED              [ 98%]
tests/test_postcodes_uk.py::test_postcodes_uk_to_dict_with_missing_separator_digit PASSED               [100%]

============================================= 52 passed in 0.05s ==============================================
```
