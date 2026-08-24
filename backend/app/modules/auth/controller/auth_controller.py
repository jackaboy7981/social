# auth_controller.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.modules.auth.schemas.auth_schemas import LoginRequest
from app.modules.auth.services import auth_service

router = APIRouter(prefix="/v1/auth")


@router.post("/login")
async def login(request: LoginRequest):
    result = await auth_service.login(request.email, request.password)
    return JSONResponse(status_code=200, content=result)
