from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func

from database import Base


class Tracking(Base):
    __tablename__ = "tracking"

    id = Column(Integer, primary_key=True, index=True)

    emergency_id = Column(
        Integer,
        ForeignKey("emergencies.id", ondelete="CASCADE"),
        nullable=False
    )

    latitude = Column(Float, nullable=False)

    longitude = Column(Float, nullable=False)

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )