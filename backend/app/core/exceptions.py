"""Application-level custom exceptions."""


class AppException(Exception):
    """Base exception for application errors."""

    def __init__(self, message: str, status_code: int, error_code: int) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_code = error_code


class InvalidEmailError(AppException):
    """Raised when an email address is not in a valid format."""

    def __init__(self) -> None:
        super().__init__(
            message="The email is not a valid email",
            status_code=400,
            error_code=1000,
        )


class DuplicateEmailError(AppException):
    """Raised when a user with the given email already exists."""

    def __init__(self) -> None:
        super().__init__(
            message="A user with this email already exists",
            status_code=409,
            error_code=1001,
        )


class DuplicateUsernameError(AppException):
    """Raised when a user with the given username already exists."""

    def __init__(self) -> None:
        super().__init__(
            message="A user with this username already exists",
            status_code=409,
            error_code=1002,
        )


class DuplicatePhoneNoError(AppException):
    """Raised when a user with the given phone number already exists."""

    def __init__(self) -> None:
        super().__init__(
            message="A user with this phone number already exists",
            status_code=409,
            error_code=1003,
        )
