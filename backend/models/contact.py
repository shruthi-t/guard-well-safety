from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    contact_name = Column(String(100), nullable=False)

    contact_mobile = Column(String(20), nullable=False)