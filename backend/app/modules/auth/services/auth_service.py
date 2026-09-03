# auth_service.py
# Business logic for the auth module. Called by this module's own controller,
# and (via interface/) by other modules' services.
import bcrypt

from app.modules.auth.client import user_client
from app.modules.auth.data_provider import auth_data_provider


async def login(email: str, password: str) -> dict:
    # placeholder business logic
    return {"message": "success"}


async def register(
    email: str,
    username: str,
    phone_no: str,
    first_name: str,
    last_name: str,
    bio: str,
    password: str,
) -> dict:
    user = await user_client.create_user(
        email, username, phone_no, first_name, last_name, bio
    )

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"), bcrypt.gensalt(rounds=12)
    ).decode("utf-8")
    await auth_data_provider.create_credential(user["id"], password_hash)

    return user


async def get_user_by_email(email: str) -> dict | None:
    return await auth_data_provider.get_user_by_email(email)
