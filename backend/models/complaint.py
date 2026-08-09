from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from database import Base


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    title = Column(String(150), nullable=False)

    description = Column(Text, nullable=False)

    proof = Column(String(255), nullable=True)

    status = Column(String(30), default="Pending")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )