class UsernameFormatInvalid(Exception):
    """Exception raised for username error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class PasswordFormatInvalid(Exception):
    """Exception raised for password error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class EmailFormatInvalid(Exception):
    """Exception raised for email error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

class UserStateInvalid(Exception):
    """Exception raised for user state error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

class FirstNameFormatInvalid(Exception):
    """Exception raised for first name error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

class LastNameFormatInvalid(Exception):
    """Exception raised for last name error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)