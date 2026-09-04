# auth_utils.py
# Common helper functions for the auth module.
import re

from app.core.exceptions import InvalidEmailError

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_email(email: str) -> None:
    if not EMAIL_PATTERN.match(email):
        raise InvalidEmailError()
