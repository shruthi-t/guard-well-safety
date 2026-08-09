from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from models.complaint import Complaint
from schemas.complaint import ComplaintCreate, ComplaintResponse

router = APIRouter(
    prefix="/complaints",
    tags=["Complaint Management"]
)


# Register Complaint
@router.post("/", response_model=ComplaintResponse)
def create_complaint(
    complaint: ComplaintCreate,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == complaint.user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    new_complaint = Complaint(
        user_id=complaint.user_id,
        title=complaint.title,
        description=complaint.description,
        proof=complaint.proof,
        status="Pending"
    )

    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)

    return new_complaint


# Complaint History
@router.get("/{user_id}", response_model=list[ComplaintResponse])
def complaint_history(
    user_id: int,
    db: Session = Depends(get_db)
):

    complaints = db.query(Complaint).filter(
        Complaint.user_id == user_id
    ).all()

    return complaints


# Complaint Details
@router.get("/details/{complaint_id}", response_model=ComplaintResponse)
def complaint_details(
    complaint_id: int,
    db: Session = Depends(get_db)
):

    complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if not complaint:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return complaint