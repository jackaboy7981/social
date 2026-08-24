from fastapi import FastAPI

from app.modules.auth.controller.auth_controller import router as auth_router

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(auth_router)
