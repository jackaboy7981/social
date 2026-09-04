from fastapi import FastAPI

from app.core.router import register_routes
from app.core.handler import register_error_handlers

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


register_routes(app)
register_error_handlers(app)
