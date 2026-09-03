# auth_data_provider.py
# Owns all persistence access for the auth module (DB queries, cache, etc).
# Only auth_service should import from here.
from datetime import datetime, timezone

from sqlalchemy import text

from app.db.session import engine


async def get_user_by_email(email: str) -> dict | None:
    # placeholder until DB layer exists
    return None


async def create_credential(user_id: int, password_hash: str) -> dict:
    now = datetime.now(timezone.utc)

    query = text(
        """
        INSERT INTO credentials (user_id, password_hash, password_updated_on)
        VALUES (:user_id, :password_hash, :password_updated_on)
        RETURNING id
        """
    )

    async with engine.begin() as conn:
        result = await conn.execute(
            query,
            {
                "user_id": user_id,
                "password_hash": password_hash,
                "password_updated_on": now,
            },
        )
        row = result.one()

    return {"id": row.id}
