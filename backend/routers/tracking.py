from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.tracking import Tracking
from models.emergency import Emergency
from schemas.tracking import TrackingCreate, TrackingResponse

router = APIRouter(
    prefix="/tracking",
    tags=["Live Tracking"]
)


# Update Location
@router.post("/update", response_model=TrackingResponse)
def update_location(
    tracking: TrackingCreate,
    db: Session = Depends(get_db)
):

    emergency = db.query(Emergency).filter(
        Emergency.id == tracking.emergency_id
    ).first()

    if not emergency:
        raise HTTPException(
            status_code=404,
            detail="Emergency not found"
        )

    new_tracking = Tracking(
        emergency_id=tracking.emergency_id,
        latitude=tracking.latitude,
        longitude=tracking.longitude
    )

    db.add(new_tracking)
    db.commit()
    db.refresh(new_tracking)

    return new_tracking


# Tracking History
@router.get("/{emergency_id}", response_model=list[TrackingResponse])
def get_tracking(
    emergency_id: int,
    db: Session = Depends(get_db)
):

    tracking = db.query(Tracking).filter(
        Tracking.emergency_id == emergency_id
    ).all()

    return tracking


# Latest Location
@router.get("/latest/{emergency_id}", response_model=TrackingResponse)
def latest_location(
    emergency_id: int,
    db: Session = Depends(get_db)
):

    latest = (
        db.query(Tracking)
        .filter(Tracking.emergency_id == emergency_id)
        .order_by(Tracking.timestamp.desc())
        .first()
    )

    if not latest:
        raise HTTPException(
            status_code=404,
            detail="Location not found"
        )

    return latest