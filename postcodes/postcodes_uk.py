import re

search_patterns = {'area': re.compile(r'^([A-Z]*).*'),
                   'district': re.compile(r'^[A-Z]*([0-9][A-Z0-9]*)'),
                   'sector': re.compile(r'.*[0-9].*([0-9])'),
                   'unit': re.compile(r'.*[0-9]([A-Z]*)$')}

validation_patterns = {'area': re.compile(r'^[A-Z]{1,2}$'),
                       'district': re.compile(r'^[0-9][A-Z0-9]?$'),
                       'sector': re.compile(r'^[0-9]$'),
                       'unit': re.compile(r'^[A-Z]{2}$')}


class PostCodeUK():
    """Object to parse postal code to UK format."""

    def __init__(self, postcode):
        self.__raw_postcode = postcode
        self.__full_postcode = self.__raw_postcode.upper()
        self.__attribute_values = {}
        self.__errors = {}

        for attribute in ['area', 'district', 'sector', 'unit']:
            # search attribute fragment in the full string
            attribute_value = self.get_first_regex_group(regex_pattern=search_patterns[attribute],
                                                         search_in_text=self.full_postcode)
            self.__attribute_values[attribute] = attribute_value

            # validate attribute fragment
            attribute_is_valid = False
            if attribute_value:
                attribute_is_valid = self.regex_is_matched(regex_pattern=validation_patterns[attribute],
                                                           search_in_text=attribute_value)
            if not attribute_value or attribute_is_valid is False:
                self.__errors[attribute] = f'Invalid {attribute} format.'

    def get_first_regex_group(self, regex_pattern, search_in_text):
        matched_search = regex_pattern.match(search_in_text)
        if matched_search and matched_search.groups():
            attribute_value = matched_search.groups()[0]
            if attribute_value:
                return attribute_value
        return None

    def regex_is_matched(self, regex_pattern, search_in_text):
        matched_search = regex_pattern.match(search_in_text)
        if matched_search and matched_search.group():
            return True
        return False

    @property
    def raw_postcode(self):
        """Raw postcode attribute"""
        return self.__raw_postcode

    @property
    def full_postcode(self):
        """Full postcode attribute"""
        return self.__full_postcode

    @property
    def area(self):
        """Area attribute"""
        return self.__attribute_values['area']

    @property
    def district(self):
        """District attribute"""
        return self.__attribute_values['district']

    @property
    def sector(self):
        """Sector attribute"""
        return self.__attribute_values['sector']

    @property
    def unit(self):
        """Unit attribute"""
        return self.__attribute_values['unit']

    @property
    def errors(self):
        """Inward code attribute"""
        return self.__errors

    @property
    def is_valid(self):
        """Valid status attribute"""
        return not self.__errors
