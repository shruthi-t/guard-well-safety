from pydantic import BaseModel, ConfigDict
from typing import Optional


# Register
class VolunteerRegister(BaseModel):
    name: str
    mobile: str
    password: str
    address: Optional[str] = None


# Login
class VolunteerLogin(BaseModel):
    mobile: str
    password: str


# Response
class VolunteerResponse(BaseModel):
    id: int
    name: str
    mobile: str
    address: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


# JWT Token
class VolunteerToken(BaseModel):
    access_token: str
    token_type: str