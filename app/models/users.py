from app.services.database import Base
from sqlalchemy import Column, String, Integer, Date, Boolean, UUID


class User(Base):
    __tablename__ = "users"
    user_id = Column(UUID, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
