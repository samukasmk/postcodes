class PostCodeUK():
    """Object to parse postal code to UK format."""

    def __init__(self, postcode):
        self.__postcode = None
        self.__outward = None
        self.__inward = None
        self.__area = None
        self.__district = None
        self.__sector = None
        self.__unit = None

    @property
    def postcode(self):
        """Raw postcode attribute"""
        return self.__postcode

    @property
    def outward(self):
        """Outward code attribute"""
        return self.__outward

    @property
    def inward(self):
        """Inward code attribute"""
        return self.__inward

    @property
    def area(self):
        """Area attribute"""
        return self.__area

    @property
    def district(self):
        """District attribute"""
        return self.__district

    @property
    def sector(self):
        """Sector attribute"""
        return self.__sector

    @property
    def unit(self):
        """Unit attribute"""
        return self.__unit

    def is_valid(self):
        """Valid status attribute"""
        pass
