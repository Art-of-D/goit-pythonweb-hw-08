from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from src.app.database.db import get_db
from src.app.response.schemas import ContactBase
from src.app.controllers.contacts import ContactsController
from src.app.database.models import Contact


router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=List[ContactBase])
async def read_contacts(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    contacts = ContactsController(db)
    contacts = await contacts.get_contacts(skip, limit)
    return contacts


@router.get("/{contact_id}", response_model=ContactBase)
async def read_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_controller = ContactsController(db)
    contact = await contact_controller.get_by_id(contact_id)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return contact


@router.post("/", response_model=ContactBase, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactBase, db: AsyncSession = Depends(get_db)):
    conctact_controller = ContactsController(db)
    contact = Contact(**body.model_dump())  # Convert Pydantic model to SQLAlchemy model
    conctact_controller.create_contact(contact)
    return contact


@router.put("/{contact_id}", response_model=ContactBase)
async def update_note(
    body: ContactBase, contact_id: int, db: AsyncSession = Depends(get_db)
):
    contact_controller = ContactsController(db)
    contact = await contact_controller.update_contact(contact_id, body)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return contact


@router.delete("/{contact_id}", response_model=ContactBase)
async def remove_conctact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_controller = ContactsController(db)
    contact = await contact_controller.delete_contact(contact_id)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return contact