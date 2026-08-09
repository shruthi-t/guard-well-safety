from pydantic import BaseModel
from datetime import datetime


# Update Location
class TrackingCreate(BaseModel):
    emergency_id: int
    latitude: float
    longitude: float


# Response
class TrackingResponse(BaseModel):
    id: int
    emergency_id: int
    latitude: float
    longitude: float
    timestamp: datetime

    class Config:
        from_attributes = True