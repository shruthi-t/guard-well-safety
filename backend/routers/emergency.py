from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from models.emergency import Emergency
from schemas.emergency import EmergencyCreate, EmergencyResponse

router = APIRouter(
    prefix="/emergency",
    tags=["SOS Emergency"]
)


# SOS API
@router.post("/sos", response_model=EmergencyResponse)
def create_sos(
    emergency: EmergencyCreate,
    db: Session = Depends(get_db)
):

    # Check user exists
    user = db.query(User).filter(
        User.id == emergency.user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    new_emergency = Emergency(
        user_id=emergency.user_id,
        latitude=emergency.latitude,
        longitude=emergency.longitude,
        status="ACTIVE"
    )

    db.add(new_emergency)
    db.commit()
    db.refresh(new_emergency)

    return new_emergency


# View Emergency
@router.get("/{emergency_id}", response_model=EmergencyResponse)
def get_emergency(
    emergency_id: int,
    db: Session = Depends(get_db)
):

    emergency = db.query(Emergency).filter(
        Emergency.id == emergency_id
    ).first()

    if not emergency:
        raise HTTPException(
            status_code=404,
            detail="Emergency not found"
        )

    return emergency