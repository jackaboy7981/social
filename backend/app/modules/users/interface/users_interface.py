# users_interface.py
# Provider-side boundary: where the users module exposes its own service
# functions for OTHER modules to call. Other modules should import from here
# (via their own client/) instead of importing users_service directly.
from app.modules.users.services import users_service


async def create_user(
    email: str,
    username: str,
    phone_no: str,
    first_name: str,
    last_name: str,
    bio: str,
) -> dict:
    return await users_service.create_user(
        email, username, phone_no, first_name, last_name, bio
    )
