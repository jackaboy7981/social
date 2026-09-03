# user_client.py
# auth module's client for calling into the users module's interface.
from app.modules.users.interface import users_interface


async def create_user(
    email: str,
    username: str,
    phone_no: str,
    first_name: str,
    last_name: str,
    bio: str,
) -> dict:
    return await users_interface.create_user(
        email, username, phone_no, first_name, last_name, bio
    )
