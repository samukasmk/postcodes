import re


class PostCodeUK:
    """Object to parse postal code to UK format."""

    def __init__(self, postcode):
        # define internal attributes
        self.__regex_patterns = {'area': re.compile(r'^([A-Z]{1,2})'),
                                 'district': re.compile(r'([0-9][A-Z0-9]?)$'),
                                 'sector': re.compile(r'^([0-9])'),
                                 'unit': re.compile(r'([A-Z]{2})$')}
        self.__raw_postcode = postcode
        self.__full_postcode = self.__raw_postcode.upper()
        self.__outward = None
        self.__inward = None
        self.__attributes = {'area': None, 'district': None, 'sector': None, 'unit': None}
        self.__errors = {}

        # parses postcode format
        self.__validate_postcode_sides()
        self.__validate_postcode_attributes()

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

    def __validate_postcode_sides(self):
        """Splits full postcode in 2 sides (outward and inward)"""
        postcode_sides = self.__full_postcode.split(' ')
        if len(postcode_sides) == 2:
            self.__outward, self.__inward = postcode_sides
        else:
            self.__errors['missing_space'] = 'Postcode is missing space.'
            return

    def __validate_postcode_attributes(self):
        """Validates postcode formats in separated sides as
           (area and district in outward str) and (sector and unit inward str)
        """
        for postcode_side, attributes in [[self.outward, ['area', 'district']],
                                          [self.inward, ['sector', 'unit']]]:
            for name in attributes:
                self.__attributes[name] = self.__get_first_regex_group(regex_pattern=self.regex_patterns[name],
                                                                       search_in_text=postcode_side)
                if not self.__attributes[name]:
                    self.__errors[name] = f'Invalid {name} format.'

    @staticmethod
    def __get_first_regex_group(regex_pattern, search_in_text):
        """Search regex in text and return first group matched"""
        matched_search = regex_pattern.search(search_in_text)
        if matched_search and matched_search.groups():
            attribute_value = matched_search.groups()[0]
            if attribute_value:
                return attribute_value
        return None
