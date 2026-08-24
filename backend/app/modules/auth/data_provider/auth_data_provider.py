# auth_data_provider.py
# Owns all persistence access for the auth module (DB queries, cache, etc).
# Only auth_service should import from here.


async def get_user_by_email(email: str) -> dict | None:
    # placeholder until DB layer exists
    return None
