# auth_controller.py
from typing import Annotated

from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse

from app.modules.auth.schemas.auth_schemas import LoginRequest, RegisterRequest
from app.modules.auth.services import auth_service

router = APIRouter(prefix="/v1/auth")


# POST /v1/auth/login
# Body: JSON { email, password }
# Authenticates a user with email + password.
@router.post("/login")
async def login(request: LoginRequest):
    result = await auth_service.login(request.email, request.password)
    return JSONResponse(status_code=200, content=result)


# POST /v1/auth/register
# Body: multipart/form-data { email, username, phone_no, first_name, last_name, bio, password }
# Creates a user (users module) then hashes the password and stores it in credentials.
# Returns { id, ref_id } of the created user.
@router.post("/register")
async def register(request: Annotated[RegisterRequest, Form()]):
    result = await auth_service.register(
        request.email,
        request.username,
        request.phone_no,
        request.first_name,
        request.last_name,
        request.bio,
        request.password,
    )
    return JSONResponse(status_code=200, content=result)
