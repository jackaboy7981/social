# auth_controller.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.auth_schemas import LoginRequest

router = APIRouter(prefix="/auth")


@router.post("/login")
async def login(request: LoginRequest):
    # basic layout for login endpoint
    print(request)
    return JSONResponse(status_code=200, content={"message": "success"})
