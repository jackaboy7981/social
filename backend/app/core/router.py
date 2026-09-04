# router.py
# Registers every module's controller router onto the app.
from fastapi import FastAPI

from app.modules.auth.controller.auth_controller import router as auth_router


def register_routes(app: FastAPI) -> None:
    app.include_router(auth_router)
