from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from models.user import User
from models.volunteer import Volunteer
from models.emergency import Emergency

from schemas.volunteer import (
    VolunteerRegister,
    VolunteerLogin,
    VolunteerResponse,
    VolunteerToken,
)

from schemas.emergency import ActiveEmergencyResponse

from security import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter(
    prefix="/volunteer",
    tags=["Volunteer"]
)


# ----------------------------------------------------
# Volunteer Registration
# ----------------------------------------------------
@router.post("/register", response_model=VolunteerResponse)
def register_volunteer(
    volunteer: VolunteerRegister,
    db: Session = Depends(get_db)
):

    existing = db.query(Volunteer).filter(
        Volunteer.mobile == volunteer.mobile
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Volunteer already exists"
        )

    new_volunteer = Volunteer(
        name=volunteer.name,
        mobile=volunteer.mobile,
        password=hash_password(volunteer.password),
        address=volunteer.address,
    )

    db.add(new_volunteer)
    db.commit()
    db.refresh(new_volunteer)

    return new_volunteer


# ----------------------------------------------------
# Volunteer Login
# ----------------------------------------------------
@router.post("/login", response_model=VolunteerToken)
def login_volunteer(
    volunteer: VolunteerLogin,
    db: Session = Depends(get_db)
):

    db_volunteer = db.query(Volunteer).filter(
        Volunteer.mobile == volunteer.mobile
    ).first()

    if not db_volunteer:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        volunteer.password,
        db_volunteer.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "volunteer_id": db_volunteer.id,
            "mobile": db_volunteer.mobile,
            "role": "volunteer"
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ----------------------------------------------------
# View Active Emergencies
# ----------------------------------------------------
@router.get("/emergencies", response_model=list[ActiveEmergencyResponse])
def active_emergencies(db: Session = Depends(get_db)):

    emergencies = (
        db.query(Emergency, User)
        .join(User, Emergency.user_id == User.id)
        .filter(Emergency.status == "ACTIVE")
        .all()
    )

    response = []

    for emergency, user in emergencies:
        response.append({
            "emergency_id": emergency.id,
            "user_name": user.name,
            "mobile": user.mobile,
            "latitude": emergency.latitude,
            "longitude": emergency.longitude,
            "status": emergency.status,
            "created_at": emergency.created_at,
        })

    return response


# ----------------------------------------------------
# Resolve Emergency
# ----------------------------------------------------
@router.put("/resolve/{emergency_id}")
def resolve_emergency(
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

    emergency.status = "RESOLVED"

    db.commit()

    return {
        "message": "Emergency resolved successfully"
    }