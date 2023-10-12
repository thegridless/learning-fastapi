from fastapi import HTTPException
from pydentic import BaseModel, EmailStr, validator
from app.utils.utils import LETTER_MATCH_PATTERN


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    is_active: bool
    password: str

    @validator
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail="Invalid characters at name")
        return value

    @validator
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail="Invalid characters at surname")
        return value
