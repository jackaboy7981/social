from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class RegisterRequest(BaseModel):
    email: str
    username: str
    phone_no: str
    first_name: str
    last_name: str
    bio: str
    password: str
