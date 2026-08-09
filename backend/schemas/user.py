from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional


# -----------------------------
# User Registration Schema
# -----------------------------
class UserRegister(BaseModel):
    name: str
    mobile: str
    email: Optional[EmailStr] = None
    password: str


# -----------------------------
# User Login Schema
# -----------------------------
class UserLogin(BaseModel):
    mobile_or_email: str
    password: str


# -----------------------------
# User Response Schema
# -----------------------------
class UserResponse(BaseModel):
    id: int
    name: str
    mobile: str
    email: Optional[EmailStr] = None
    role: str

    model_config = ConfigDict(from_attributes=True)


# -----------------------------
# JWT Token Schema
# -----------------------------
class Token(BaseModel):
    access_token: str
    token_type: str