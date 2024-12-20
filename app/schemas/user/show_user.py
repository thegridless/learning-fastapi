from uuid import UUID
from app.schemas.tuned_model import TunedModel
from pydantic import EmailStr


class ShowUser(TunedModel):
    id: UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool
