# users_service.py
# Business logic for the users module. Called by this module's own controller,
# and (via interface/) by other modules' services.
from app.modules.users.data_provider import users_data_provider


async def create_user(
    email: str,
    username: str,
    phone_no: str,
    first_name: str,
    last_name: str,
    bio: str,
) -> dict:
    return await users_data_provider.create_user(
        email, username, phone_no, first_name, last_name, bio
    )
