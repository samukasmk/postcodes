import re

REGEX_AREA_VALIDATION = re.compile(r'^[A-Z]{1,2}$')
REGEX_DISTRICT_VALIDATION = re.compile(r'^[0-9][A-Z0-9]?$')
REGEX_SECTOR_VALIDATION = re.compile(r'^[0-9]$')
REGEX_UNIT_VALIDATION = re.compile(r'^[A-Z]{2}$')
REGEX_INSERT_SPACE_BEFORE_DIGITS = re.compile(r'([0-9]+)')
REGEX_INSERT_SPACE_AFTER_DIGITS = re.compile(r'([0-9]+)')
REGEX_SPLIT_SIDES_BY_SPACES = re.compile(r' +')

POSTCODE_VALIDATIONS = {'area': REGEX_AREA_VALIDATION,
                        'district': REGEX_DISTRICT_VALIDATION,
                        'sector': REGEX_SECTOR_VALIDATION,
                        'unit': REGEX_UNIT_VALIDATION}


class PostCodeUK:
    """Object to parse postal code to UK format."""

    def __init__(self, postcode):
        # define internal attributes
        self.__raw_postcode = postcode
        self.__full_postcode = postcode.upper()
        self.__outward = None
        self.__inward = None
        self.__attributes = {'area': None, 'district': None, 'sector': None, 'unit': None}
        self.__errors = {}

        # splits outward and inward sides
        self.__outward, self.__inward = self.split_sides_by_spaces(self.full_postcode)

        # splits area and district sides
        if self.outward:
            outward_to_split = self.insert_space_before_digits(self.outward)
            self.outward_splited = self.split_sides_by_spaces(outward_to_split)
            self.__attributes['area'], self.__attributes['district'] = self.outward_splited

        # splits sector and district unit
        if self.inward:
            if self.inward[0].isdigit():
                inward_to_split = self.insert_space_after_digits(self.inward)
            else:
                inward_to_split = ' ' + self.inward
            self.inward_splited = self.split_sides_by_spaces(inward_to_split)
            self.__attributes['sector'], self.__attributes['unit'] = self.inward_splited

        # parses postcode format in separated pieces
        for name in list(self.__attributes.keys()):
            regex_pattern = POSTCODE_VALIDATIONS[name]
            attribute_value = self.attributes.get(name)
            if not attribute_value or not regex_pattern.match(attribute_value):
                self.__errors[name] = f'Invalid {name} format.'

    def insert_space_before_digits(self, text_to_insert):
        return re.sub(r'([0-9]+)', r' \1', text_to_insert)

    def insert_space_after_digits(self, text_to_insert):
        return re.sub(r'([0-9]+)', r'\1 ', text_to_insert)

    def insert_space_at_beginning(self, text_to_insert):
        return ' ' + text_to_insert

    def split_sides_by_spaces(self, text_to_split):
        left_side = None
        right_side = None
        splited_sides = re.split(r' +', text_to_split)
        if splited_sides:
            left_side = splited_sides[0]
            if len(splited_sides) > 1:
                right_side = ''.join(splited_sides[1:])
        return left_side, right_side

    @property
    def regex_patterns(self):
        """Regexp patterns"""
        return self.__regex_patterns

    @property
    def raw_postcode(self):
        """Raw postcode text"""
        return self.__raw_postcode

    @property
    def full_postcode(self):
        """Full postcode text normalized"""
        return self.__full_postcode

    @property
    def outward(self):
        """Outward attribute"""
        return self.__outward

    @property
    def inward(self):
        """Inward attribute"""
        return self.__inward

    @property
    def attributes(self):
        """Postcode attributes"""
        return self.__attributes

    @property
    def area(self):
        """Area attribute"""
        return self.__attributes['area']

    @property
    def district(self):
        """District attribute"""
        return self.__attributes['district']

    @property
    def sector(self):
        """Sector attribute"""
        return self.__attributes['sector']

    @property
    def unit(self):
        """Unit attribute"""
        return self.__attributes['unit']

    @property
    def errors(self):
        """Errors dict"""
        return self.__errors

    @property
    def is_valid(self):
        """Validation status"""
        return not self.__errors
