class PlateNumberFormatInvalid(Exception):
    """Exception raised for username error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

class CarStatusInvalid(Exception):
    """Exception raised for username error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)