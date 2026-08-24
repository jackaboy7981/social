# auth_service.py
# Business logic for the auth module. Called by this module's own controller,
# and (via interface/) by other modules' services.
from app.modules.auth.data_provider import auth_data_provider


async def login(email: str, password: str) -> dict:
    # placeholder business logic
    return {"message": "success"}


async def get_user_by_email(email: str) -> dict | None:
    return await auth_data_provider.get_user_by_email(email)
