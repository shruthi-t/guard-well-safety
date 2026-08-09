from pydantic import BaseModel, ConfigDict
from datetime import datetime


# Create SOS
class EmergencyCreate(BaseModel):
    user_id: int
    latitude: float
    longitude: float


# Response
class EmergencyResponse(BaseModel):
    id: int
    user_id: int
    latitude: float
    longitude: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class ActiveEmergencyResponse(BaseModel):
    emergency_id: int
    user_name: str
    mobile: str
    latitude: float
    longitude: float
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)