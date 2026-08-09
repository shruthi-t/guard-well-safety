from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Create Complaint
class ComplaintCreate(BaseModel):
    user_id: int
    title: str
    description: str
    proof: Optional[str] = None


# Response
class ComplaintResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    proof: Optional[str]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True