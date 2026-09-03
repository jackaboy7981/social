# users_data_provider.py
# Owns all persistence access for the users module (DB queries, cache, etc).
# Only users_service should import from here.
import uuid
from datetime import datetime, timezone

from sqlalchemy import text

from app.db.session import engine


async def create_user(
    email: str,
    username: str,
    phone_no: str,
    first_name: str,
    last_name: str,
    bio: str,
) -> dict:
    now = datetime.now(timezone.utc)
    ref_id = uuid.uuid4()

    query = text(
        """
        INSERT INTO users (
            email, username, phone_no, first_name, last_name, bio,
            created_on, updated_on, ref_id
        )
        VALUES (
            :email, :username, :phone_no, :first_name, :last_name, :bio,
            :created_on, :updated_on, :ref_id
        )
        RETURNING id, ref_id
        """
    )

    async with engine.begin() as conn:
        result = await conn.execute(
            query,
            {
                "email": email,
                "username": username,
                "phone_no": phone_no,
                "first_name": first_name,
                "last_name": last_name,
                "bio": bio,
                "created_on": now,
                "updated_on": now,
                "ref_id": ref_id,
            },
        )
        row = result.one()

    return {"id": row.id, "ref_id": str(row.ref_id)}
