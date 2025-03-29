from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.app.database.models import Contact

class ContactsService:
  def __init__(self, session: AsyncSession):
    self.session = session

  async def create_contact(self, contact: Contact):
    if contact is None:
        raise ValueError("Contact cannot be None.")
    
    try:
        self.session.add(contact)
        self.session.commit()
    except Exception as e:
        self.session.rollback()
        raise RuntimeError(f"An error occurred while creating the contact: {e}")
    
    return contact

  async def get_contacts(self, skip: int = 0, limit: int = 10):
    stmt = select(Contact).offset(skip).limit(limit)
    result = await self.session.execute(stmt)
    if result is None:
        raise ValueError("No contacts found.")
    return result.scalars().all()
  
  async def get_by_id(self, id: int):
    result = await self.session.query(Contact).filter(Contact.id == id).first()
    if result is None:
        raise ValueError(f"Contact with the given ID {id} does not exist.")
    return result
  
  async def update_contact(self, id: int, contact: Contact):
    existing_contact = self.get_by_id(id).first()
    
    if existing_contact is None:
        raise ValueError("Contact with the given ID does not exist.")
    
    if contact.name:
        existing_contact.name = contact.name
    if contact.email:
        existing_contact.email = contact.email
    if contact.phone:
        existing_contact.phone = contact.phone
    if contact.birthdate:
        existing_contact.birthdate = contact.birthdate
    if contact.notes:
        existing_contact.notes = contact.notes
    
    try:
        await self.session.commit()
    except Exception as e:
        self.session.rollback()
        raise RuntimeError("Failed to update contact.") from e
    
    return existing_contact
  
  async def delete_contact(self, id: int):
    try:
        contact = self.get_by_id(id)
        if contact is None:
            raise ValueError(f"Contact with the given ID {id} does not exist.")
        await self.session.delete(contact)
        await self.session.commit()
        return contact
    except Exception as e:
        self.session.rollback()
        raise RuntimeError(f"Failed to delete contact. {e}") from e

  