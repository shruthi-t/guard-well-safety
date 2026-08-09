from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.contact import EmergencyContact
from models.user import User
from schemas.contact import ContactCreate, ContactResponse

router = APIRouter(
    prefix="/contacts",
    tags=["Emergency Contacts"]
)


# Add Contact
@router.post("/", response_model=ContactResponse)
def add_contact(contact: ContactCreate, db: Session = Depends(get_db)):

    # Check user exists
    user = db.query(User).filter(User.id == contact.user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    new_contact = EmergencyContact(
        user_id=contact.user_id,
        contact_name=contact.contact_name,
        contact_mobile=contact.contact_mobile
    )

    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)

    return new_contact


# Get Contacts by User
@router.get("/{user_id}", response_model=list[ContactResponse])
def get_contacts(user_id: int, db: Session = Depends(get_db)):

    contacts = db.query(EmergencyContact).filter(
        EmergencyContact.user_id == user_id
    ).all()

    return contacts