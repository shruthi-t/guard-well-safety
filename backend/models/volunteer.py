from sqlalchemy import Column, Integer, String
from database import Base


class Volunteer(Base):
    __tablename__ = "volunteers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    mobile = Column(String(20), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    address = Column(String(255), nullable=True)