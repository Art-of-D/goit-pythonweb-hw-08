from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ContactBase(BaseModel):
    name: str = Field(max_length=50)
    email: str = Field(max_length=150)
    phone: str = Field(max_length=20)
    birthdate: str
    notes: Optional[str] = None


# class ContactUpdate(ContactBase):
#     done: Optional[bool] = False



# class ContactStatusUpdate(BaseModel):
#     done: bool


# class ContactResponse(ContactBase):
#     id: int
#     done: bool
#     created_at: Optional[datetime] = None
#     updated_at: Optional[datetime] = None

#     model_config = ConfigDict(from_attributes=True)